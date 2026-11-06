"""Giữ nhãn đã có trong CSV và gán nhãn cho review mới."""

import csv
import re
from collections import Counter, defaultdict, deque
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "data" / "raw" / "commentdienmayxanh.csv"
TARGET = ROOT / "data" / "labeled" / "reviews_spam_ham.csv"
FIELDS = ["category", "product", "review", "rating", "label"]
SOURCE_FIELDS = ["phan_loai", "san_pham", "noi_dung", "so_sao"]
REVIEW_FIELDS = ["category", "product", "review", "rating"]

PHONE = re.compile(r"(?<!\d)(?:\+?84|0)(?:[\s.\-]*\d){9,10}(?!\d)")
LINK = re.compile(r"(?:https?://|www\.|\b\w+\.(?:com|vn|net|org)\b)", re.I)
REPEATED_CHAR = re.compile(r"([^\W\d_])\1{4,}", re.I | re.UNICODE)
OK_ONLY = re.compile(r"(?:ok)+|oki|oke|okay", re.I)
SINGLE_WORD = re.compile(r"\w+", re.UNICODE)
MANUAL_SPAM = {
    "sản phẩm ư", "dung p", "ok la", "ok nha", "it test",
}


def normalized(text):
    return re.sub(r"\s+", " ", text.casefold()).strip()


def is_spam(text):
    clean = normalized(text)
    letters = re.sub(r"[^\w]", "", clean, flags=re.UNICODE)
    if not letters or len(letters) < 2:
        return True
    # Review chỉ có một từ/chuỗi số không cung cấp đủ nội dung, kể cả "Tốt".
    if len(SINGLE_WORD.findall(clean)) == 1:
        return True
    if clean.strip(" .,!?:;…") in MANUAL_SPAM:
        return True
    # Các câu chỉ có "ok" và biến thể ngắn, kể cả dấu câu/emoji, đều là spam.
    words_only = re.sub(r"[^\w]+", " ", clean, flags=re.UNICODE).strip()
    if OK_ONLY.fullmatch(words_only):
        return True
    if PHONE.search(clean) or LINK.search(clean):
        return True
    if REPEATED_CHAR.search(clean):
        return True
    words = clean.split()
    if len(words) >= 3 and len(set(words)) == 1:
        return True
    return False


def write_reviews(path, rows):
    with path.open("w", encoding="utf-8-sig", newline="") as target:
        writer = csv.DictWriter(target, fieldnames=FIELDS)
        writer.writeheader()
        writer.writerows(rows)


def read_csv(path, required_fields):
    with path.open("r", encoding="utf-8-sig", newline="") as source:
        reader = csv.DictReader(source)
        if not set(required_fields).issubset(reader.fieldnames or []):
            raise ValueError(f"{path} cần có các cột: {', '.join(required_fields)}")
        rows = list(reader)
    if any(row[field] is None for row in rows for field in required_fields):
        raise ValueError(f"{path} có dòng thiếu cột hoặc giá trị")
    return rows


def review_key(row):
    return tuple(row[field] for field in REVIEW_FIELDS)


def preserve_existing_labels(labeled, existing):
    """Giữ nhãn spam cũ và áp dụng quy tắc mới cho cả review đã có."""
    saved = defaultdict(deque)
    for row in existing:
        if row["label"] not in {"0", "1"}:
            raise ValueError(f"Nhãn không hợp lệ trong {TARGET}: {row['label']!r}")
        saved[review_key(row)].append(int(row["label"]))

    reused = 0
    upgraded = 0
    for row in labeled:
        labels = saved[review_key(row)]
        if labels:
            previous = labels.popleft()
            upgraded += row["label"] > previous
            row["label"] = max(row["label"], previous)
            reused += 1
    return reused, upgraded


def label_reviews(rows):
    """Gán nhãn theo nội dung và tỷ lệ lặp trong cùng sản phẩm."""
    product_counts = Counter(row["san_pham"] for row in rows)
    review_counts = Counter(
        (row["san_pham"], normalized(row["noi_dung"])) for row in rows
    )
    labeled = []
    for row in rows:
        review = row["noi_dung"]
        product = row["san_pham"]
        repeated = review_counts[(product, normalized(review))]
        suspicious_duplicate = (
            repeated >= 4 and repeated / product_counts[product] >= 0.10
        )
        labeled.append(
            {
                "category": row["phan_loai"],
                "product": product,
                "review": review,
                "rating": row["so_sao"],
                "label": int(is_spam(review) or suspicious_duplicate),
            }
        )

    return labeled


def main():
    rows = read_csv(SOURCE, SOURCE_FIELDS)
    labeled = label_reviews(rows)
    existing = read_csv(TARGET, FIELDS) if TARGET.exists() else []
    reused, upgraded = preserve_existing_labels(labeled, existing)

    TARGET.parent.mkdir(parents=True, exist_ok=True)
    write_reviews(TARGET, labeled)

    print(f"Total: {len(labeled)} reviews, {sum(row['label'] for row in labeled)} spam; "
          f"matched {reused} existing reviews, upgraded {upgraded} labels; "
          f"classified {len(labeled) - reused} new reviews -> {TARGET}")


if __name__ == "__main__":
    main()
