"""Huấn luyện FastText từ đầu; không lưu model hay dữ liệu trung gian."""
from pathlib import Path
from tempfile import TemporaryDirectory

import fasttext


def train_model(train):
    # FastText nhận đường dẫn tệp; tệp tạm tự xóa sau khi huấn luyện.
    with TemporaryDirectory() as folder:
        train_file = Path(folder) / "train.txt"
        with train_file.open("w", encoding="utf-8") as f:
            for text, label in zip(train["text"], train["label"]):
                f.write(f"__label__{label} {text}\n")

        model = fasttext.train_supervised(
            input=str(train_file),
            lr=0.3,
            epoch=35,
            dim=50,
            wordNgrams=2,
            minn=2,
            maxn=5,
            minCount=1,
            bucket=50000,
            loss="softmax",
            thread=1,
            seed=42,
            verbose=0,
        )
    return model


def predict_test(model, texts):
    # Dùng danh sách và k=1 để tương thích fasttext-wheel với NumPy 2.
    labels, _ = model.predict(list(texts), k=1)
    return [int(label[0].replace("__label__", "")) for label in labels]
