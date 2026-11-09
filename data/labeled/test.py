# So sánh giữa AI gán và người gán nhãn -> tính tỉ lệ khớp

import pandas as pd

FILE_AI    = "data/labeled/1000_sample_dau_may_gan_nhan.csv"  # AI gán nhãn
FILE_HUMAN = "data/labeled/1000_sample_dau_tu_gan_nhan.csv"   # Người gán nhãn

# Đọc 2 file
df_ai    = pd.read_csv(FILE_AI,    encoding="utf-8-sig")
df_human = pd.read_csv(FILE_HUMAN, encoding="utf-8-sig")

# Lấy nhãn từ cột label
label_ai    = df_ai["label"].astype(int)
label_human = df_human["label"].astype(int)

# So sánh theo từng dòng (cùng thứ tự)
match   = label_ai == label_human
n_total = len(match)
n_match = match.sum()
n_diff  = n_total - n_match
ratio   = n_match / n_total

print(f"Tổng số mẫu        : {n_total}")
print(f"Số dòng khớp nhãn  : {n_match}")
print(f"Số dòng không khớp : {n_diff}")
print(f"Tỉ lệ khớp         : {ratio:.2%}")

# In các dòng không khớp
if n_diff > 0:
    diff_idx = df_ai[~match].index
    print(f"\nCác dòng không khớp (index, nội dung, label_ai, label_người):")
    for i in diff_idx:
        print(f"  [{i}] label_ai={label_ai[i]}  label_người={label_human[i]}  nội_dung={str(df_ai.loc[i,'noi_dung'])[:80]}")
