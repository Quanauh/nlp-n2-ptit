# 📂 Data — Phát hiện Review Spam/Ham trên Điện máy xanh

Thư mục này chứa toàn bộ dữ liệu cho bài toán **phân loại review spam/ham** từ website [Điện máy xanh](https://www.dienmayxanh.com), được tổ chức theo ba giai đoạn: **thu thập thô → gán nhãn → tiền xử lý**.

---

## 🗂️ Cấu trúc thư mục

```
data/
├── raw/
│   └── commentdienmayxanh.csv      # Dữ liệu gốc thu thập từ web
├── labeled/
│   ├── reviews_spam_ham.csv        # Dữ liệu đã gán nhãn đầy đủ
│   ├── 1.csv                       # Lô gán nhãn thủ công #1 (249 mẫu)
│   ├── 2.csv                       # Lô gán nhãn thủ công #2 (249 mẫu)
│   ├── 3.csv                       # Lô gán nhãn AI + người kiểm tra (250 mẫu)
│   ├── 4.csv                       # Lô gán nhãn thủ công #4 (249 mẫu)
│   ├── RULE_LABELING.md            # Bộ quy tắc gán nhãn (guideline)
│   └── test.py                     # Script so sánh nhãn AI và nhãn người
└── processed/
    └── processed.csv               # Dữ liệu đã tiền xử lý, chia train/test
```

---

## 1. `raw/` — Dữ liệu thô

**File:** `commentdienmayxanh.csv` · 2.6 MB

Dữ liệu được thu thập (crawl) trực tiếp từ trang đánh giá sản phẩm của [Điện máy xanh](https://www.dienmayxanh.com).

| Cột | Mô tả |
|---|---|
| `phan_loai` | Danh mục sản phẩm |
| `san_pham` | Tên sản phẩm cụ thể |
| `nguoi_danh_gia` | Tên người viết review |
| `so_sao` | Số sao đánh giá (1–5) |
| `noi_dung` | Nội dung review |
| `link` | URL trang đánh giá gốc |

### Thống kê

| Chỉ số | Giá trị |
|---|---|
| **Tổng số review** | 10.238 |
| **Số danh mục sản phẩm** | 10 |

| Danh mục | Số review |
|---|---|
| Điều hòa | 1.677 |
| Máy giặt | 1.627 |
| Nồi cơm điện | 1.625 |
| Tủ lạnh | 1.610 |
| Máy lọc nước | 1.265 |
| Tivi | 931 |
| Máy sấy quần áo | 724 |
| Khác | 392 |
| Máy lọc không khí | 219 |
| Camera giám sát | 168 |

---

## 2. `labeled/` — Dữ liệu đã gán nhãn

### 2.1 `reviews_spam_ham.csv` — Tập nhãn đầy đủ · 1.6 MB

File chính chứa toàn bộ 10.238 review đã được gán nhãn Spam/Ham.

| Cột | Mô tả |
|---|---|
| `category` | Danh mục sản phẩm |
| `product` | Tên sản phẩm |
| `review` | Nội dung review |
| `rating` | Số sao (1–5) |
| `label` | Nhãn: `0` = HAM, `1` = SPAM |

### Phân phối nhãn

| Nhãn | Số lượng | Tỉ lệ |
|---|---|---|
| **HAM (0)** — Review thật | 9.304 | ~90,9% |
| **SPAM (1)** — Review rác | 934 | ~9,1% |
| **Tổng** | **10.238** | 100% |

> ⚠️ **Dữ liệu mất cân bằng (imbalanced):** tỉ lệ SPAM chỉ chiếm ~9%. Cần lưu ý khi huấn luyện mô hình (oversampling, class weight, v.v.).

---

### 2.2 Các lô gán nhãn thủ công (`1.csv`, `2.csv`, `3.csv`, `4.csv`)

Mỗi file là một **lô (batch) nhỏ ~250 mẫu** dùng để gán nhãn thủ công / kiểm tra chất lượng. Được dùng trong quy trình kiểm soát chất lượng (QC) và đánh giá Cohen's Kappa.

| File | Số dòng | Cột đặc biệt | Ghi chú |
|---|---|---|---|
| `1.csv` | 249 | — | Lô gán nhãn thủ công, chưa có cột label trong file gốc |
| `2.csv` | 249 | — | Lô gán nhãn thủ công |
| `3.csv` | 250 | `label`, `label_ai` | Lô AI gán nhãn trước, người kiểm tra sau |
| `4.csv` | 249 | `label` | Lô gán nhãn thủ công |

---

### 2.3 `RULE_LABELING.md` — Bộ quy tắc gán nhãn

Tài liệu hướng dẫn gán nhãn chi tiết, bao gồm:

- **Định nghĩa nhãn** HAM/SPAM
- **4 nhóm rule SPAM** (A: Quảng cáo · B: Không liên quan · C: Giả mạo/bot · D: Phá hoại)
- **9 rule HAM** (review thật, review ngắn, hỏi về sản phẩm, v.v.)
- **Danh sách edge cases** xử lý các trường hợp biên
- **Thứ tự ưu tiên** khi xung đột giữa các rule
- **Quy trình QC:** 2 người gán/review, Cohen's Kappa ≥ 0.75, 20–30 mẫu vàng mỗi lô

---

### 2.4 `test.py` — Script so sánh nhãn

Script Python đọc file `3.csv` và tính **tỉ lệ khớp** giữa nhãn do AI gán (`label_ai`) và nhãn do người kiểm tra (`label`).

```bash
python data/labeled/test.py
```

---

## 3. `processed/` — Dữ liệu đã tiền xử lý

**File:** `processed.csv` · 1.4 MB

Tập con đã qua bước làm sạch và chuẩn hóa, sẵn sàng đưa vào huấn luyện mô hình.

| Cột | Mô tả |
|---|---|
| `category` | Danh mục sản phẩm |
| `product` | Tên sản phẩm |
| `review` | Nội dung review gốc |
| `rating` | Số sao (1–5) |
| `label` | Nhãn: `0` = HAM, `1` = SPAM |
| `clean_text` | Văn bản đã làm sạch: lowercase, chuẩn hóa số → `numtoken` |
| `split` | Phân chia: `train` / `test` |

### Thống kê

| Tập | Tổng | HAM (0) | SPAM (1) |
|---|---|---|---|
| **train** | 3.856 | 3.181 (82,5%) | 675 (17,5%) |
| **test** | 964 | 795 (82,5%) | 169 (17,5%) |
| **Tổng** | **4.820** | **3.976** | **844** |

> 📌 **Lưu ý:** Tập `processed` chỉ chứa **4.820 / 10.238 mẫu** từ tập labeled — đây là tập con đã được lọc/xử lý. Tỉ lệ chia train/test là **80:20**, phân tầng (stratified) theo nhãn.

### Các bước tiền xử lý đã áp dụng

- Chuyển văn bản về **chữ thường** (lowercase)
- Chuẩn hóa **số → `numtoken`** (ví dụ: "2 tuần" → "numtoken tuần")
- Giữ nguyên dấu câu tiếng Việt, tách token cơ bản

---

## 📊 Tổng quan nhanh

| Giai đoạn | File | Số mẫu | Nhãn |
|---|---|---|---|
| **Raw** | `raw/commentdienmayxanh.csv` | 10.238 | ✗ |
| **Labeled** | `labeled/reviews_spam_ham.csv` | 10.238 | ✓ (HAM/SPAM) |
| **Processed** | `processed/processed.csv` | 4.820 | ✓ + train/test split |

---

## 📌 Ghi chú

- Nguồn dữ liệu: **[Điện máy xanh](https://www.dienmayxanh.com)** — dữ liệu chỉ dùng cho mục đích **nghiên cứu học thuật**.
- Nhãn gán theo bộ rule tại [`labeled/RULE_LABELING.md`](labeled/RULE_LABELING.md).
- Mọi thay đổi về quy tắc gán nhãn phải được cập nhật vào `RULE_LABELING.md` kèm version (v1.0, v1.1...).
