# Rule gắn nhãn Spam/Ham

**Nhãn:** HAM = 0, SPAM = 1

## 1. Nguyên tắc

1. Gán nhãn theo **mục đích** của review, không theo cảm xúc. Chê gay gắt, viết dở, viết tắt vẫn là HAM.
2. Chỉ dùng thông tin có trong cột nội dung comment.
3. **Nghi ngờ mà thiếu bằng chứng thì gán HAM.**

## 2. Rule SPAM (gán 1 nếu thỏa một trong các rule)

| Rule | Điều kiện | Ví dụ |
|---|---|---|
| **S1. Quảng cáo / dẫn khách** | Có SĐT, Zalo, email, link ngoài whitelist, hoặc kêu gọi mua/ib/inbox/liên hệ, hoặc quảng cáo shop khác | "Liên hệ 09xx giá rẻ hơn", "Bên mình bán rẻ hơn, ib em" |
| **S2. Nội dung rác** | Không liên quan mua hàng, chuỗi vô nghĩa, hoặc tuyển dụng/vay/cờ bạc/người lớn | "Hôm nay trời đẹp", "asdfgh", "......." |
| **S3. Sai sản phẩm rõ ràng** | Nói cụ thể về mặt hàng khác danh mục so với `phan_loai` | Mục tủ lạnh nhưng review "pin điện thoại trâu" |

## 3. Rule HAM (gán 0)

| Rule | Điều kiện | Ví dụ |
|---|---|---|
| **H1** | Có nhận xét thực tế về sản phẩm, giao hàng, nhân viên, bảo hành (kể cả chê gay gắt) | "Máy giặt kêu to, nhân viên tư vấn dở" |
| **H2** | Ngắn, chung chung, đúng ngữ cảnh (kể cả lặp nhiều) | "Tốt", "ok", "giao nhanh" |
| **H3** | Không dấu, teencode, sai chính tả | "sp xai dc, ko co van de" |
| **H4** | Câu hỏi về sản phẩm | "Máy này bảo hành mấy năm?" |
| **H5** | So sánh khách quan với nơi khác, không kêu gọi mua | "Xem bên khác giá cao hơn nên mua ở đây" |
| **H6** | Mặc định: không đủ bằng chứng gán SPAM | |

## 4. Thứ tự kiểm tra

1. Có S1 hoặc S2 → **SPAM**
2. Có S3 rõ ràng → **SPAM** (mơ hồ hoặc nghi người dùng nhầm → HAM)
3. Còn lại → **HAM**

Review vừa có đánh giá thật vừa có quảng cáo → **SPAM** (theo S1).

## 5. Vai trò các cột

| Cột | Cách dùng |
|---|---|
| `noi_dung` | Căn cứ chính cho mọi rule |
| `phan_loai`, `san_pham` | Kiểm tra S3, đếm lặp S4 |
| `so_sao` | Chỉ tham khảo. Sao lệch nội dung **không** tự là SPAM |
| `nguoi_danh_gia` | Không dùng làm bằng chứng (tên không phải ID duy nhất) |
| `link` | Giả định là URL sản phẩm, **không** dùng làm dấu hiệu spam |

## 6. Các edge case hay gặp 

| Tình huống | Nhãn |
|---|---|
| "ok", "tốt" | HAM |
| Khen hoa mỹ nhưng có chi tiết thật | HAM |
| SĐT cá nhân để quảng cáo kêu gọi sang trang khác | SPAM (S1) |
| Nêu tên shop khác để so sánh giá, không kèm SĐT/link/ib | HAM |
| Review chỉ nói giao hàng/nhân viên | HAM |
| Review tiếng nước ngoài | Dịch rồi gán theo nội dung |
| `noi_dung` rỗng | Loại khỏi tập |
|chỉ có emoji ví dụ  "👍" | SPAM |
| Gọi tổng đài/link chính thức của Điện máy xanh | HAM (lập whitelist trước) |

## 7 Whitelist cho rule S1


1. Domain
dienmayxanh.com	Website Điện máy xan
thegioididong.com	Cùng hệ thống Mobile World
bachhoaxanh.com	Cùng hệ thống
mwg.vn	Công ty mẹ (Mobile World)

2. Tổng đài
Các đầu số tổng đài chính thức của Điện máy XANH gồm:
• Tổng đài tư vấn mua hàng: 1900 232 461 
• Tổng đài bảo hành và hỗ trợ kỹ thuật: 1900 232 465 
• Tổng đài giải quyết khiếu nại: 1800 1063 
• Tổng đài đặt lịch dịch vụ (Thợ Điện máy XANH): 1900 232 463 