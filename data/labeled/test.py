# So sánh giữa AI gán và người gán nhãn -> tính tỉ lệ khớp

import pandas as pd


def compare_ai_human(df: pd.DataFrame) -> pd.DataFrame:
    """
    So sánh nhãn AI gán (cột `label_ai`) và nhãn người gán (cột `label`).
    Thêm cột `match` (1 = khớp, 0 = không khớp).
    """
    df = df.copy()
    df["label_ai"] = df["label_ai"].astype(int)
    df["label"] = df["label"].astype(int)
    df["match"] = (df["label_ai"] == df["label"]).astype(int)

    n_match = int(df["match"].sum())
    n_total = len(df)
    ratio = n_match / n_total if n_total else 0.0

    print(f"  So sánh nhãn AI gán và nhãn người gán: "
          f"{n_match:,}/{n_total:,} dòng khớp nhãn ({ratio:.1%})")
    return df


if __name__ == "__main__":
    df = pd.read_csv("data/labeled/3.csv", encoding="utf-8-sig")
    compare_ai_human(df)