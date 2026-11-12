#!/usr/bin/env python3
"""Gán nhãn HAM/SPAM cho CSV bằng DeepSeek API.

Script chỉ dùng thư viện chuẩn Python, tự lưu checkpoint sau mỗi lô và
có thể tiếp tục sau khi bị gián đoạn.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import os
import random
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path
from typing import Any


SCRIPT_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = SCRIPT_DIR.parent.parent
DEFAULT_INPUT = PROJECT_ROOT / "data" / "raw" / "raw_7k2.csv"
DEFAULT_RULES = SCRIPT_DIR / "RULE_LABELING.md"
DEFAULT_OUTPUT = SCRIPT_DIR / "raw_7k2_deepseek_labeled.csv"

REQUIRED_COLUMNS = {
    "phan_loai",
    "san_pham",
    "nguoi_danh_gia",
    "so_sao",
    "noi_dung",
    "link",
}
VALID_RULES = {"S1", "S2", "S3", "H1", "H2", "H3", "H4", "H5", "H6"}


class LabelingError(RuntimeError):
    """Lỗi gán nhãn có thể hiển thị trực tiếp cho người dùng."""


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Gán nhãn raw_7k2.csv theo RULE_LABELING.md bằng DeepSeek API."
    )
    parser.add_argument("--input", type=Path, default=DEFAULT_INPUT, help="CSV đầu vào")
    parser.add_argument("--rules", type=Path, default=DEFAULT_RULES, help="File quy tắc")
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT, help="CSV kết quả")
    parser.add_argument(
        "--checkpoint",
        type=Path,
        default=None,
        help="File checkpoint JSONL (mặc định: <output>.checkpoint.jsonl)",
    )
    parser.add_argument(
        "--model",
        default=os.environ.get("DEEPSEEK_MODEL", "deepseek-flash"),
        help="Model DeepSeek (mặc định: deepseek-flash)",
    )
    parser.add_argument(
        "--base-url",
        default=os.environ.get("DEEPSEEK_BASE_URL", "https://api.deepseek.com"),
        help="Base URL của DeepSeek API",
    )
    parser.add_argument("--batch-size", type=int, default=20, help="Số review mỗi request")
    parser.add_argument("--max-retries", type=int, default=5, help="Số lần thử lại mỗi request")
    parser.add_argument("--timeout", type=float, default=120.0, help="Timeout request (giây)")
    parser.add_argument(
        "--limit",
        type=int,
        default=None,
        help="Chỉ gán N dòng đầu tiên (dùng để chạy thử)",
    )
    parser.add_argument(
        "--overwrite",
        action="store_true",
        help="Gán lại từ đầu và ghi đè output/checkpoint hiện có",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Kiểm tra input/prompt, không gọi API và không ghi file",
    )
    return parser.parse_args()


def resolve_path(path: Path) -> Path:
    return path if path.is_absolute() else (Path.cwd() / path).resolve()


def read_input(path: Path) -> tuple[list[str], list[dict[str, str]]]:
    if not path.is_file():
        raise LabelingError(f"Không tìm thấy CSV đầu vào: {path}")

    with path.open("r", encoding="utf-8-sig", newline="") as file:
        reader = csv.DictReader(file)
        if not reader.fieldnames:
            raise LabelingError("CSV đầu vào không có header.")
        missing = REQUIRED_COLUMNS.difference(reader.fieldnames)
        if missing:
            raise LabelingError(f"CSV thiếu các cột: {', '.join(sorted(missing))}")
        rows = [dict(row) for row in reader]
        return list(reader.fieldnames), rows


def read_rules(path: Path) -> str:
    if not path.is_file():
        raise LabelingError(f"Không tìm thấy file quy tắc: {path}")
    text = path.read_text(encoding="utf-8").strip()
    if not text:
        raise LabelingError("File quy tắc đang rỗng.")
    return text


def row_hash(row: dict[str, str]) -> str:
    serialized = json.dumps(row, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(serialized.encode("utf-8")).hexdigest()


def checkpoint_path_for(output: Path, explicit: Path | None) -> Path:
    if explicit is not None:
        return resolve_path(explicit)
    return output.with_name(output.name + ".checkpoint.jsonl")


def load_checkpoint(
    path: Path, rows_by_index: dict[int, dict[str, str]]
) -> dict[int, dict[str, Any]]:
    completed: dict[int, dict[str, Any]] = {}
    if not path.exists():
        return completed

    with path.open("r", encoding="utf-8") as file:
        for line_number, line in enumerate(file, 1):
            line = line.strip()
            if not line:
                continue
            try:
                item = json.loads(line)
                index = int(item["row_index"])
                label = int(item["label"])
            except (KeyError, TypeError, ValueError, json.JSONDecodeError) as exc:
                raise LabelingError(
                    f"Checkpoint hỏng tại dòng {line_number}: {path}"
                ) from exc

            row = rows_by_index.get(index)
            if row is None:
                continue
            if item.get("row_hash") != row_hash(row):
                continue
            if label not in (0, 1):
                raise LabelingError(f"Nhãn không hợp lệ trong checkpoint dòng {line_number}.")
            completed[index] = item
    return completed


def append_checkpoint(path: Path, results: list[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as file:
        for result in results:
            file.write(json.dumps(result, ensure_ascii=False, separators=(",", ":")) + "\n")
        file.flush()
        os.fsync(file.fileno())


def build_system_prompt(rules: str) -> str:
    return f"""Bạn là chuyên gia gán nhãn review tiếng Việt.

Hãy tuân thủ TUYỆT ĐỐI bộ quy tắc sau:

--- BẮT ĐẦU RULE_LABELING ---
{rules}
--- KẾT THÚC RULE_LABELING ---

Yêu cầu:
- Xử lý từng review độc lập.
- Chỉ dùng noi_dung làm bằng chứng chính; chỉ dùng phan_loai và san_pham để xét S3.
- Nếu nghi ngờ mà không đủ bằng chứng SPAM thì gán HAM (0).
- Trả về đúng JSON object, không markdown, không thêm văn bản ngoài JSON.
- Mỗi id phải xuất hiện đúng một lần và giữ nguyên id đầu vào.
- label chỉ là số 0 hoặc 1.
- rule là một trong: S1, S2, S3, H1, H2, H3, H4, H5, H6.
- reason là giải thích ngắn gọn bằng tiếng Việt, không quá 20 từ.

JSON output mẫu:
{{"items":[{{"id":12,"label":0,"rule":"H2","reason":"Nhận xét ngắn, đúng ngữ cảnh sản phẩm"}}]}}
"""


def build_user_prompt(batch: list[tuple[int, dict[str, str]]]) -> str:
    reviews = [
        {
            "id": index,
            "phan_loai": row["phan_loai"],
            "san_pham": row["san_pham"],
            "noi_dung": row["noi_dung"],
        }
        for index, row in batch
    ]
    return "Hãy gán nhãn các review sau và trả về JSON:\n" + json.dumps(
        reviews, ensure_ascii=False, separators=(",", ":")
    )


def post_chat_completion(
    *,
    api_key: str,
    base_url: str,
    model: str,
    system_prompt: str,
    user_prompt: str,
    timeout: float,
) -> tuple[dict[str, Any], dict[str, Any]]:
    endpoint = base_url.rstrip("/") + "/chat/completions"
    payload = {
        "model": model,
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
        "response_format": {"type": "json_object"},
        "thinking": {"type": "disabled"},
        "reasoning_effort": "none",
        "temperature": 0,
        "max_tokens": 4096,
        "stream": False,
    }
    request = urllib.request.Request(
        endpoint,
        data=json.dumps(payload, ensure_ascii=False).encode("utf-8"),
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
            "Accept": "application/json",
            "User-Agent": "nlp2-deepseek-labeler/1.0",
        },
        method="POST",
    )

    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            body = response.read().decode("utf-8")
    except urllib.error.HTTPError as exc:
        detail = exc.read().decode("utf-8", errors="replace")
        retry_after = exc.headers.get("Retry-After")
        error = LabelingError(f"DeepSeek HTTP {exc.code}: {detail[:500]}")
        setattr(error, "retry_after", retry_after)
        raise error from exc
    except urllib.error.URLError as exc:
        raise LabelingError(f"Không kết nối được DeepSeek API: {exc.reason}") from exc
    except TimeoutError as exc:
        raise LabelingError(f"DeepSeek API quá thời gian chờ ({timeout:g}s).") from exc

    try:
        response_data = json.loads(body)
        choice = response_data["choices"][0]
        content = choice["message"]["content"]
        finish_reason = choice.get("finish_reason")
        if finish_reason != "stop":
            raise LabelingError(f"DeepSeek dừng bất thường: finish_reason={finish_reason!r}")
        if not isinstance(content, str) or not content.strip():
            raise LabelingError("DeepSeek trả về content rỗng.")
        parsed = json.loads(content)
    except (KeyError, IndexError, TypeError, json.JSONDecodeError) as exc:
        raise LabelingError(f"Response DeepSeek không đúng định dạng: {body[:500]}") from exc

    return parsed, response_data.get("usage", {})


def validate_response(
    parsed: dict[str, Any], batch: list[tuple[int, dict[str, str]]]
) -> list[dict[str, Any]]:
    if not isinstance(parsed, dict) or not isinstance(parsed.get("items"), list):
        raise LabelingError("JSON phải có dạng {\"items\": [...]}.")

    expected_ids = {index for index, _ in batch}
    rows_by_index = dict(batch)
    results: dict[int, dict[str, Any]] = {}

    for item in parsed["items"]:
        if not isinstance(item, dict):
            raise LabelingError("Mỗi phần tử trong items phải là object.")
        try:
            index = int(item["id"])
            label = int(item["label"])
        except (KeyError, TypeError, ValueError) as exc:
            raise LabelingError("Mỗi item phải có id và label hợp lệ.") from exc

        if index not in expected_ids:
            raise LabelingError(f"DeepSeek trả về id không có trong lô: {index}")
        if index in results:
            raise LabelingError(f"DeepSeek trả về id trùng lặp: {index}")
        if label not in (0, 1):
            raise LabelingError(f"Nhãn của id {index} không phải 0/1: {label}")

        rule = str(item.get("rule", "")).upper().strip()
        reason = str(item.get("reason", "")).strip()
        if rule not in VALID_RULES:
            raise LabelingError(f"Rule của id {index} không hợp lệ: {rule!r}")
        if label == 1 and not rule.startswith("S"):
            raise LabelingError(f"Id {index}: label=1 nhưng rule={rule}")
        if label == 0 and not rule.startswith("H"):
            raise LabelingError(f"Id {index}: label=0 nhưng rule={rule}")
        if not reason:
            raise LabelingError(f"Id {index} thiếu reason.")

        results[index] = {
            "row_index": index,
            "row_hash": row_hash(rows_by_index[index]),
            "label": label,
            "rule": rule,
            "reason": reason,
        }

    missing = expected_ids.difference(results)
    if missing:
        raise LabelingError(f"DeepSeek thiếu các id: {sorted(missing)}")
    return [results[index] for index, _ in batch]


def retry_delay(attempt: int, error: Exception) -> float:
    retry_after = getattr(error, "retry_after", None)
    if retry_after:
        try:
            return min(float(retry_after), 60.0)
        except ValueError:
            pass
    return min(2 ** (attempt - 1) + random.random(), 60.0)


def request_batch(
    *,
    batch: list[tuple[int, dict[str, str]]],
    api_key: str,
    base_url: str,
    model: str,
    system_prompt: str,
    timeout: float,
    max_retries: int,
) -> tuple[list[dict[str, Any]], dict[str, Any]]:
    last_error: Exception | None = None
    for attempt in range(1, max_retries + 1):
        try:
            parsed, usage = post_chat_completion(
                api_key=api_key,
                base_url=base_url,
                model=model,
                system_prompt=system_prompt,
                user_prompt=build_user_prompt(batch),
                timeout=timeout,
            )
            return validate_response(parsed, batch), usage
        except LabelingError as exc:
            last_error = exc
            if attempt == max_retries:
                break
            delay = retry_delay(attempt, exc)
            print(
                f"  Lỗi lần {attempt}/{max_retries}: {exc}. "
                f"Thử lại sau {delay:.1f}s...",
                file=sys.stderr,
                flush=True,
            )
            time.sleep(delay)

    assert last_error is not None
    raise LabelingError(str(last_error))


def label_with_fallback(
    *,
    batch: list[tuple[int, dict[str, str]]],
    api_key: str,
    base_url: str,
    model: str,
    system_prompt: str,
    timeout: float,
    max_retries: int,
) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    try:
        results, usage = request_batch(
            batch=batch,
            api_key=api_key,
            base_url=base_url,
            model=model,
            system_prompt=system_prompt,
            timeout=timeout,
            max_retries=max_retries,
        )
        return results, [usage]
    except LabelingError:
        if len(batch) == 1:
            raise
        middle = len(batch) // 2
        print(
            f"  Tách lô {len(batch)} thành {middle} + {len(batch) - middle} dòng...",
            file=sys.stderr,
            flush=True,
        )
        left_results, left_usage = label_with_fallback(
            batch=batch[:middle],
            api_key=api_key,
            base_url=base_url,
            model=model,
            system_prompt=system_prompt,
            timeout=timeout,
            max_retries=max_retries,
        )
        right_results, right_usage = label_with_fallback(
            batch=batch[middle:],
            api_key=api_key,
            base_url=base_url,
            model=model,
            system_prompt=system_prompt,
            timeout=timeout,
            max_retries=max_retries,
        )
        return left_results + right_results, left_usage + right_usage


def write_output(
    path: Path,
    fieldnames: list[str],
    indexed_rows: list[tuple[int, dict[str, str]]],
    completed: dict[int, dict[str, Any]],
) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(path.name + ".tmp")
    output_fields = [field for field in fieldnames if field != "label"] + ["label"]

    with temporary.open("w", encoding="utf-8-sig", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=output_fields, extrasaction="ignore")
        writer.writeheader()
        for index, row in indexed_rows:
            output_row = dict(row)
            output_row["label"] = completed[index]["label"]
            writer.writerow(output_row)
    os.replace(temporary, path)


def sum_usage(usages: list[dict[str, Any]]) -> dict[str, int]:
    totals = {"prompt_tokens": 0, "completion_tokens": 0, "total_tokens": 0}
    for usage in usages:
        for key in totals:
            value = usage.get(key, 0)
            if isinstance(value, int):
                totals[key] += value
    return totals


def main() -> int:
    args = parse_args()
    if args.batch_size < 1:
        raise LabelingError("--batch-size phải lớn hơn 0.")
    if args.max_retries < 1:
        raise LabelingError("--max-retries phải lớn hơn 0.")
    if args.limit is not None and args.limit < 1:
        raise LabelingError("--limit phải lớn hơn 0.")

    input_path = resolve_path(args.input)
    rules_path = resolve_path(args.rules)
    output_path = resolve_path(args.output)
    checkpoint_path = checkpoint_path_for(output_path, args.checkpoint)

    fieldnames, rows = read_input(input_path)
    rules = read_rules(rules_path)

    # RULE_LABELING quy định loại noi_dung rỗng khỏi tập.
    indexed_rows = [
        (index, row)
        for index, row in enumerate(rows)
        if (row.get("noi_dung") or "").strip()
    ]
    empty_count = len(rows) - len(indexed_rows)
    if args.limit is not None:
        indexed_rows = indexed_rows[: args.limit]

    print(f"Input       : {input_path}")
    print(f"Rules       : {rules_path}")
    print(f"Output      : {output_path}")
    print(f"Checkpoint  : {checkpoint_path}")
    print(f"Model       : {args.model}")
    print(f"Số dòng      : {len(indexed_rows)}" + (f" (loại {empty_count} dòng rỗng)" if empty_count else ""))

    system_prompt = build_system_prompt(rules)
    if args.dry_run:
        sample = indexed_rows[: min(args.batch_size, len(indexed_rows))]
        print(f"Dry-run OK  : system prompt {len(system_prompt)} ký tự")
        print(f"               user prompt mẫu {len(build_user_prompt(sample))} ký tự")
        return 0

    api_key = os.environ.get("DEEPSEEK_API_KEY", "").strip()
    if not api_key:
        raise LabelingError(
            "Thiếu biến môi trường DEEPSEEK_API_KEY. "
            "Hãy chạy: export DEEPSEEK_API_KEY='khóa-của-bạn'"
        )

    if args.overwrite:
        output_path.unlink(missing_ok=True)
        checkpoint_path.unlink(missing_ok=True)
    elif output_path.exists() and not checkpoint_path.exists():
        raise LabelingError(
            f"Output đã tồn tại nhưng không có checkpoint: {output_path}. "
            "Dùng --overwrite nếu muốn gán lại."
        )

    rows_by_index = dict(indexed_rows)
    completed = load_checkpoint(checkpoint_path, rows_by_index)
    pending = [(index, row) for index, row in indexed_rows if index not in completed]
    print(f"Đã hoàn thành : {len(completed)}/{len(indexed_rows)}")

    all_usages: list[dict[str, Any]] = []
    for offset in range(0, len(pending), args.batch_size):
        batch = pending[offset : offset + args.batch_size]
        print(
            f"Gán lô {offset // args.batch_size + 1}/"
            f"{(len(pending) + args.batch_size - 1) // args.batch_size} "
            f"({len(batch)} dòng)...",
            flush=True,
        )
        results, usages = label_with_fallback(
            batch=batch,
            api_key=api_key,
            base_url=args.base_url,
            model=args.model,
            system_prompt=system_prompt,
            timeout=args.timeout,
            max_retries=args.max_retries,
        )
        append_checkpoint(checkpoint_path, results)
        completed.update({int(item["row_index"]): item for item in results})
        all_usages.extend(usages)
        print(f"  Tiến độ: {len(completed)}/{len(indexed_rows)}", flush=True)

    missing = [index for index, _ in indexed_rows if index not in completed]
    if missing:
        raise LabelingError(f"Chưa gán xong {len(missing)} dòng; checkpoint đã được giữ lại.")

    write_output(output_path, fieldnames, indexed_rows, completed)
    labels = [int(completed[index]["label"]) for index, _ in indexed_rows]
    usage = sum_usage(all_usages)
    print("\nHoàn tất.")
    print(f"HAM (0)     : {labels.count(0)}")
    print(f"SPAM (1)    : {labels.count(1)}")
    print(f"Token API   : {usage['total_tokens']} (chỉ tính lần chạy này)")
    print(f"CSV kết quả : {output_path}")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except KeyboardInterrupt:
        print("\nĐã dừng. Chạy lại cùng lệnh để tiếp tục từ checkpoint.", file=sys.stderr)
        raise SystemExit(130)
    except LabelingError as exc:
        print(f"Lỗi: {exc}", file=sys.stderr)
        raise SystemExit(1)
