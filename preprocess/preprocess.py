"""
BƯỚC 1 — TIỀN XỬ LÍ DỮ LIỆU
===========================

Đầu vào : data/labeled/reviews_spam_ham_filtered_augmented.csv
Đầu ra  : data/processed/processed.csv
          (các cột: category, product, review, rating, label, clean_text, split)

Các việc được làm:
  1. Làm sạch văn bản tiếng Việt (chuẩn hoá Unicode, chữ thường, thay URL/SĐT/số
     bằng token đặc biệt, rút gọn ký tự lặp, tách dấu câu, chuẩn hoá teencode).
  2. Loại bỏ câu trùng lặp (sau khi làm sạch).
  3. Chia train/test (80/20, phân tầng theo nhãn) — làm Ở ĐÂY để cả 3 cách trích
     chọn đặc trưng (BoW, TF-IDF, WE) dùng CHUNG một cách chia -> so sánh công bằng.

Vì sao phải bỏ trùng TRƯỚC khi chia?
  Bộ dữ liệu có ~56% dòng trùng lặp ("Tốt" ~450 lần, "Ok" ~340 lần...). Nếu chia
  ngẫu nhiên theo dòng, cùng một câu sẽ nằm ở cả train lẫn test -> mô hình chỉ cần
  "học thuộc" là đoán đúng, điểm test bị thổi phồng (rò rỉ dữ liệu / data leakage).

Nhãn: label = 1 -> spam, label = 0 -> ham.

Chạy:  python preprocess/preprocess.py
"""

import argparse
import re
import unicodedata
from pathlib import Path

import pandas as pd
from sklearn.model_selection import train_test_split

ROOT = Path(__file__).resolve().parents[1]
RAW_PATH = ROOT / "data" / "labeled" / "reviews_spam_ham_filtered_augmented.csv"
OUT_PATH = ROOT / "data" / "processed" / "processed.csv"

# ---------------------------------------------------------------------------
# Làm sạch văn bản
# ---------------------------------------------------------------------------

# Teencode / viết tắt hay gặp trong bình luận thương mại điện tử
TEENCODE = {
    "ko": "không", "k": "không", "kh": "không", "khong": "không", "hok": "không",
    "hông": "không", "kg": "không", "khg": "không",
    "dc": "được", "đc": "được", "duoc": "được", "dk": "được", "đk": "được",
    "sp": "sản phẩm",
    "oke": "ok", "okie": "ok", "okela": "ok", "oki": "ok", "okay": "ok", "okê": "ok",
    "nv": "nhân viên", "dmx": "điện máy xanh", "bh": "bảo hành",
    "j": "gì", "mk": "mình", "mik": "mình", "mn": "mọi người",
    "vs": "với", "r": "rồi", "rùi": "rồi",
    "tks": "cảm ơn", "thanks": "cảm ơn", "thank": "cảm ơn",
}

URL_RE = re.compile(
    r"(https?://\S+|www\.\S+|\b\S+\.(?:com|vn|net|vip|xyz|info|org|shop|top|online)\S*)",
    flags=re.IGNORECASE)
EMAIL_RE = re.compile(r"\b[\w.+-]+@[\w-]+\.[\w.-]+\b")
PHONE_RE = re.compile(r"(?:\+?84|0)(?:[\s.\-]?\d){8,10}")             # SĐT Việt Nam
NUMBER_RE = re.compile(r"\d+(?:[.,]\d+)*(?:k|tr|đ|d|vnd|vnđ)?\b")     # 500k, 5tr, 30...
REPEAT_CHAR_RE = re.compile(r"(\w)\1{2,}")                           # "tốttttt" -> "tốt"
PUNCT_RE = re.compile(r"([^\w\s])")
MULTI_SPACE_RE = re.compile(r"\s+")


def clean_text(text) -> str:
    """Làm sạch một bình luận. Trả về chuỗi các token cách nhau bởi dấu cách."""
    if not isinstance(text, str):
        text = "" if pd.isna(text) else str(text)

    text = unicodedata.normalize("NFC", text)   # đồng nhất 2 kiểu gõ dấu tiếng Việt
    text = text.lower()

    # Thay thông tin "đặc thù" bằng token chung: mô hình học được "có SĐT / có link"
    # thay vì học thuộc từng con số cụ thể.
    text = URL_RE.sub(" urltoken ", text)
    text = EMAIL_RE.sub(" emailtoken ", text)
    text = PHONE_RE.sub(" phonetoken ", text)
    text = NUMBER_RE.sub(" numtoken ", text)

    text = REPEAT_CHAR_RE.sub(r"\1", text)
    # Giữ dấu câu như token riêng: bình luận chỉ có "." hay "!!!" cũng là tín hiệu spam
    text = PUNCT_RE.sub(r" \1 ", text)

    tokens = [TEENCODE.get(tok, tok) for tok in text.split()]
    text = MULTI_SPACE_RE.sub(" ", " ".join(tokens)).strip()
    return text if text else "emptytoken"


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    ap = argparse.ArgumentParser(description="Tiền xử lí dữ liệu spam/ham")
    ap.add_argument("--input", default=str(RAW_PATH))
    ap.add_argument("--output", default=str(OUT_PATH))
    ap.add_argument("--test-size", type=float, default=0.2)
    ap.add_argument("--seed", type=int, default=42)
    args = ap.parse_args()

    # utf-8-sig: file gốc có BOM -> nếu không, tên cột đầu bị đọc thành '\ufeffcategory'
    df = pd.read_csv(args.input, encoding="utf-8-sig")
    print(f"Đọc dữ liệu gốc: {len(df):,} dòng, {df.shape[1]} cột")
    print(f"  Giá trị thiếu:\n{df.isna().sum().to_string()}")
    df = df.dropna(subset=["review", "label"]).copy()
    df["label"] = df["label"].astype(int)
    print(f"  Phân bố nhãn gốc: ham={int((df.label == 0).sum()):,}  "
          f"spam={int((df.label == 1).sum()):,}")

    # 1. Làm sạch
    df["clean_text"] = df["review"].map(clean_text)

    # 2. Xử lý câu có nhãn mâu thuẫn (cùng clean_text nhưng khác nhãn) -> nhãn đa số
    n_lab = df.groupby("clean_text")["label"].nunique()
    conflict = n_lab[n_lab > 1].index
    if len(conflict):
        majority = (df[df.clean_text.isin(conflict)]
                    .groupby("clean_text")["label"]
                    .agg(lambda s: s.value_counts().idxmax()))
        mask = df.clean_text.isin(conflict)
        df.loc[mask, "label"] = df.loc[mask, "clean_text"].map(majority)
        print(f"  {len(conflict)} câu có nhãn mâu thuẫn -> lấy nhãn đa số")

    # 3. Bỏ trùng lặp
    n_before = len(df)
    df = df.drop_duplicates("clean_text").reset_index(drop=True)
    print(f"Bỏ trùng lặp: {n_before:,} -> {len(df):,} dòng "
          f"(loại {n_before - len(df):,} dòng = {(n_before - len(df)) / n_before:.1%})")

    # 4. Chia train/test phân tầng theo nhãn
    train_idx, test_idx = train_test_split(
        df.index, test_size=args.test_size, stratify=df["label"], random_state=args.seed)
    df["split"] = "train"
    df.loc[test_idx, "split"] = "test"

    for split in ["train", "test"]:
        part = df[df.split == split]
        print(f"  {split:5s}: {len(part):5,} mẫu | ham={int((part.label == 0).sum()):,} "
              f"spam={int((part.label == 1).sum()):,} "
              f"(tỉ lệ spam {part.label.mean():.1%})")

    n_tok = df["clean_text"].str.split().str.len()
    print(f"Độ dài câu sau làm sạch (số token): trung bình {n_tok.mean():.1f}, "
          f"trung vị {n_tok.median():.0f}, lớn nhất {n_tok.max()}")

    out = Path(args.output)
    out.parent.mkdir(parents=True, exist_ok=True)
    cols = ["category", "product", "review", "rating", "label", "clean_text", "split"]
    df[cols].to_csv(out, index=False, encoding="utf-8-sig")
    print(f"\n✔ Đã lưu dữ liệu sau tiền xử lí: {out}")

    print("\nVí dụ trước / sau làm sạch:")
    for _, r in df.sample(6, random_state=1).iterrows():
        print(f"  [{'spam' if r.label else 'ham '}] {r.review[:70]!r}")
        print(f"          -> {r.clean_text[:70]!r}")


if __name__ == "__main__":
    main()
