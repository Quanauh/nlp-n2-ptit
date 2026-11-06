"""Đọc, làm sạch và chia dữ liệu; nhãn 0 = ham, 1 = spam."""
import re
import unicodedata

import pandas as pd
from sklearn.model_selection import train_test_split


def clean_text(text):
    text = unicodedata.normalize("NFC", str(text)).lower()
    text = text.replace("__label__", " ")
    text = re.sub(r"([.,!?;:()\"/])", r" \1 ", text)
    # Giữ dấu tiếng Việt, số, emoji và nhận xét ngắn.
    return re.sub(r"\s+", " ", text).strip() or "empty_review_token"


def load_data(csv_path):
    df = pd.read_csv(csv_path, keep_default_na=False)
    if not {"review", "label"}.issubset(df.columns):
        raise ValueError("CSV cần có hai cột review và label.")

    df["label"] = pd.to_numeric(df["label"], errors="raise")
    if not df["label"].isin([0, 1]).all():
        raise ValueError("Nhãn phải là 0 (ham) hoặc 1 (spam).")
    df["label"] = df["label"].astype(int)
    df["text"] = df["review"].apply(clean_text)

    # Tách câu có nhãn mâu thuẫn, không tự quyết định sửa nhãn.
    conflict = df.groupby("text")["label"].transform("nunique") > 1
    df = df.loc[~conflict].drop_duplicates("text")

    if df["label"].nunique() != 2 or df["label"].value_counts().min() < 5:
        raise ValueError("Cần ít nhất 5 câu riêng biệt mỗi lớp sau xử lý.")

    # Loại trùng trước khi chia để cùng câu không nằm ở cả train và test.
    return train_test_split(
        df,
        test_size=0.2,
        stratify=df["label"],
        random_state=42,
    )
