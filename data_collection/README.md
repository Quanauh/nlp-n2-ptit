# Thu thập đánh giá Điện Máy Xanh

Thư mục này chứa mã thu thập và tệp CSV nguồn `data/raw/commentdienmayxanh.csv`. CSV có 10.238 đánh giá với các cột `phan_loai`, `san_pham`, `nguoi_danh_gia`, `so_sao`, `noi_dung`, `link`. Bộ dữ liệu đã gán nhãn tương ứng nằm ở `data/labeled/reviews_spam_ham.csv`.

## Chạy crawler

Từ thư mục gốc của repo:

```bash
pip install selenium webdriver-manager pandas
python data_collection/main.py
```

Cần cài Chrome. Chương trình mở trình duyệt; hãy mở trang sản phẩm Điện Máy Xanh trong cửa sổ đó, xử lý captcha nếu xuất hiện, rồi nhấn Enter trong terminal để thu thập. Có thể lặp lại với các sản phẩm khác và nhập `0` để ghi CSV rồi thoát.

Crawler giữ ID bình luận để tránh lấy trùng trong một lần chạy. Khi lưu, nó nối thêm vào CSV nguồn; nếu chạy lại vào ngày khác, cần kiểm tra trùng lặp trước khi dùng dữ liệu mới để huấn luyện. Các bộ chọn CSS và thao tác phân trang phụ thuộc giao diện hiện tại của trang web.
