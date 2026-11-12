# Gán nhãn tự động bằng DeepSeek

Script `label_with_deepseek.py` đọc `raw_7k2.csv`, áp dụng toàn bộ nội dung
trong `RULE_LABELING.md`, sau đó tạo CSV mới có thêm cột `label`:

- `0`: HAM
- `1`: SPAM

API key chỉ được đọc từ biến môi trường, không lưu trong source code hay
CSV.

## 1. Kiểm tra trước khi gọi API

Từ thư mục gốc project `nlp-n2-ptit`, chạy:

```bash
python data/labeled/label_with_deepseek.py --dry-run
```

## 2. Chạy thử 20 dòng

```bash
export DEEPSEEK_API_KEY='dán-api-key-của-bạn-vào-đây'

python data/labeled/label_with_deepseek.py \
  --limit 20 \
  --output data/labeled/raw_7k2_deepseek_test20.csv
```

Kiểm tra file test trước khi chạy toàn bộ.

## 3. Gán nhãn toàn bộ 7.200 dòng

```bash
python data/labeled/label_with_deepseek.py
```

Kết quả mặc định:

```text
data/labeled/raw_7k2_deepseek_labeled.csv
```

Script gửi 20 review trong mỗi request. Có thể thay đổi kích thước lô:

```bash
python data/labeled/label_with_deepseek.py --batch-size 10
```

## Tiếp tục sau khi gián đoạn

Kết quả từng lô được ghi ngay vào file checkpoint:

```text
data/labeled/raw_7k2_deepseek_labeled.csv.checkpoint.jsonl
```

Nếu mất mạng, hết quota hoặc nhấn `Ctrl+C`, chỉ cần chạy lại đúng lệnh
cũ. Script tự bỏ qua các dòng đã hoàn thành.

Muốn xóa tiến độ cũ và gán lại từ đầu:

```bash
python data/labeled/label_with_deepseek.py --overwrite
```

## Tùy chọn model

Mặc định script dùng `deepseek-flash`. Có thể đổi model bằng tham số hoặc
biến môi trường:

```bash
python data/labeled/label_with_deepseek.py --model deepseek-v4-pro

# hoặc
export DEEPSEEK_MODEL='deepseek-v4-pro'
python data/labeled/label_with_deepseek.py
```

## Kiểm tra chất lượng

Checkpoint lưu thêm `rule` và `reason` cho từng dòng để dễ audit. Nên kiểm
tra thủ công một mẫu ngẫu nhiên và toàn bộ các dòng `label=1` trước khi
dùng dữ liệu để huấn luyện.
