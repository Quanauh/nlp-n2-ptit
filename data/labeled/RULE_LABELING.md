# Bộ RULE gắn nhãn Spam/Ham cho review Điện máy xanh

## 1. Nguyên tắc chung

- **Gán nhãn theo mục đích của review, không theo cảm xúc.** Chê sản phẩm, chê dịch vụ, văn phong kém đều **không** phải spam.
- **Xét cả ngữ cảnh**: sản phẩm đang được review, số sao, thông tin người dùng (nếu có). Không chỉ đọc mỗi câu chữ.
- **Một review chỉ có một nhãn.** Nếu thỏa nhiều rule, lấy nhãn theo độ ưu tiên.

## 2. Định nghĩa nhãn

| Nhãn | Ý nghĩa |
|---|---|
| **HAM (0)** | Review thật, phản ánh trải nghiệm/ý kiến về sản phẩm, dịch vụ mua tại Điện máy xanh |
| **SPAM (1)** | Review không nhằm đánh giá sản phẩm, hoặc là nội dung quảng cáo, giả mạo, lặp, phá hoại |

## 3. Rule gắn nhãn SPAM

### Nhóm A: Quảng cáo, dẫn dắt khách hàng (SPAM chắc chắn)

| Rule | Mô tả | Ví dụ |
|---|---|---|
| A1 | Chứa **SĐT, Zalo, email, link** không liên quan đến việc đánh giá sản phẩm | "Liên hệ 09xx xxx xxx giá rẻ hơn" |
| A2 | **Quảng cáo cửa hàng/sản phẩm/dịch vụ khác** (đối thủ, shop online, bảo hành, sửa chữa) | "Bên mình bán máy này rẻ hơn, ib em" |
| A3 | Kêu gọi **mua/ib/inbox/theo dõi/tham gia nhóm** | "Ai cần mua ib mình nhé" |
| A4 | Tuyển dụng, cho vay, đầu tư, cờ bạc, nội dung người lớn | "Việc nhẹ lương cao, add Zalo..." |

### Nhóm B: Nội dung không liên quan

| Rule | Mô tả | Ví dụ |
|---|---|---|
| B1 | Nội dung **hoàn toàn không liên quan** sản phẩm/dịch vụ | "Hôm nay trời đẹp quá" |
| B2 | Review **sai sản phẩm** rõ ràng (nói về mặt hàng khác danh mục, ví dụ trang tủ lạnh mà review điện thoại) | Chi tiết cụ thể và mâu thuẫn rõ |
| B3 | **Chuỗi ký tự vô nghĩa**, gõ bừa, copy dán đoạn văn không liên quan | "asdfghjkl", "......." |
| B4 | Văn bản **sao chép nguyên đoạn** từ trang mô tả sản phẩm/bài viết khác | Dán nguyên thông số kỹ thuật |

### Nhóm C: Hành vi giả mạo, thao túng

| Rule | Mô tả | Ví dụ |
|---|---|---|
| C1 | **Cùng nội dung/mẫu** đăng nhiều lần (cùng user hoặc nhiều user, nhiều sản phẩm). Ngưỡng tham khảo: ≥ 3 lần cùng user hoặc cụm ≥ 5 bản. **Ngoại lệ:** review ngắn phổ biến (xem H3) | Cùng một đoạn khen chung chung đăng trên 10 sản phẩm |
| C2 | **Review seeding/khen quá mức chung chung**, mẫu câu quảng bá như văn bản marketing, đăng dồn dập | "Sản phẩm tuyệt vời, shop uy tín nhất vịnh Bắc Bộ, mọi người nên mua ngay" |
| C3 | **Review đối thủ/bôi nhọ có tổ chức**: công kích hàng loạt, lặp một nội dung tiêu cực kèm dấu hiệu bot | Nhiều tài khoản mới cùng chê một câu |
| C4 | Dấu hiệu **bot**: nhiều review trong thời gian rất ngắn, câu mẫu máy móc | 20 review trong 1 phút |
| C5 | **Mâu thuẫn rõ ràng giữa số sao và nội dung** kèm dấu hiệu bất thường khác (cần kết hợp thêm rule) | 1 sao nhưng nội dung quảng cáo |

### Nhóm D: Phá hoại, vi phạm

| Rule | Mô tả |
|---|---|
| D1 | Nội dung **xúc phạm, thù ghét, quấy rối** không liên quan đến đánh giá (lưu ý: chê gay gắt về sản phẩm vẫn là HAM) |
| D2 | **Lộ thông tin cá nhân** của người khác nhằm quấy rối |
| D3 | **Lừa đảo, phishing, link độc hại** |

## 4. Rule gắn nhãn HAM

| Rule | Mô tả | Ví dụ |
|---|---|---|
| H1 | Có **nhận xét thực tế** về sản phẩm: chất lượng, hiệu năng, giao hàng, lắp đặt, bảo hành, nhân viên | "Tủ lạnh chạy êm, giao hàng đúng hẹn" |
| H2 | **Review tiêu cực** có lý do cụ thể, kể cả gay gắt | "Máy giặt kêu to, nhân viên tư vấn dở" |
| H3 | **Review ngắn, chung chung** nhưng đúng ngữ cảnh | "Tốt", "ok", "hàng đẹp", "👍", "giao nhanh" |
| H4 | Review **không dấu, teencode, sai chính tả, viết tắt** nhưng nội dung đúng chủ đề | "sp xai dc, ko co van de" |
| H5 | **Câu hỏi về sản phẩm** (thông tin, bảo hành, màu sắc) | "Máy này có bảo hành mấy năm vậy shop?" |
| H6 | **Phản hồi, bổ sung** về trải nghiệm sau thời gian sử dụng | "Dùng 3 tháng vẫn ổn" |
| H7 | **Nhắc đến thương hiệu/cửa hàng khác** để so sánh khách quan, không dẫn dắt mua | "Mình xem bên khác giá cao hơn nên mua ở đây" |
| H8 | Có **link/SĐT hợp lệ** liên quan: SĐT tổng đài Điện máy xanh, link tham khảo chính thức | "Gọi 1800.xxxx thì được hỗ trợ" |
| H9 | **Khen/chê chung chung nhưng có sao khớp** và không có dấu hiệu bất thường | 5 sao, "Rất hài lòng" |

## 5. Các trường hợp biên (edge cases)

| Tình huống | Gán nhãn | Lý do |
|---|---|---|
| Review có từ ngắn ("👍", "ok") | HAM | Ngắn không đồng nghĩa spam |
| Review ngắn phổ biến lặp nhiều lần do nhiều người thật | HAM | Xem H3, ưu tiên ngữ cảnh |
| Khen quá nhiều, hoa mỹ nhưng có chi tiết thật | HAM | Có nội dung kiểm chứng được |
| Chê nhưng có SĐT cá nhân để "ai bị giống mình liên hệ" | xem xét theo ngữ cảnh | Có thể là thật, có thể dẫn dắt |
| So sánh giá với cửa hàng khác kèm tên shop | HAM nếu khách quan; SPAM nếu có SĐT/link dẫn dắt | Phân biệt theo mục đích |
| Nội dung đúng sản phẩm nhưng copy từ trang khác | SPAM (B4) nếu rõ ràng sao chép | |
| Review nói về dịch vụ chung (giao hàng, nhân viên) không đề cập sản phẩm | HAM | Vẫn thuộc trải nghiệm mua hàng |
| Review tiếng nước ngoài | HAM nếu đúng nội dung| |
| Review sai danh mục nhưng nghi do người dùng nhầm | HAM nếu không có dấu hiệu quảng cáo/lặp | Nhầm lẫn khác với spam |
| Seeding nhẹ ("Cảm ơn shop, hàng tốt") nhưng nhiều bản giống nhau trên nhiều sản phẩm | SPAM (C1/C2) | Dựa vào mẫu lặp |
| Review ngắn kèm tên sản phẩm khác | xét ngữ cảnh | |

## 6. Thứ tự ưu tiên khi xung đột

1. **Nhóm D, A (quảng cáo, lừa đảo, độc hại)** → SPAM ngay, bất kể nội dung còn lại.
2. **Nhóm C (lặp, bot, seeding)** → SPAM nếu có bằng chứng định lượng (số lần lặp, tần suất).
3. **Nhóm B (không liên quan)** → SPAM nếu rõ ràng, nếu mơ hồ thì xét theo ngữ cảnh để gắn SPAM/ HAM.
4. **Có nội dung thực tế (H1, H2, H5, H6)** → HAM, kể cả khi chất lượng viết kém.
5. **Không đủ thông tin**

**Nguyên tắc cuối:** *Nghi ngờ nhưng thiếu bằng chứng thì không gán SPAM.* Gán nhầm HAM thành SPAM làm mất review hợp lệ nên nghiêm trọng hơn.

## 7. Quy trình áp dụng cho người gán nhãn

1. Đọc review, xem metadata (số sao, sản phẩm, số lần lặp, user, thời gian).
2. Kiểm tra theo thứ tự: **A → D → C → B → H**.
3. Ghi **nhãn**
4. Với cụm trùng lặp: xem vài bản đại diện rồi gán cho cả cụm.

## 8. Kiểm soát chất lượng

- Mỗi review gán bởi **2 người**, bất đồng thì người thứ 3 quyết định.
- Đo **Cohen's Kappa** sau mỗi lô 200-500 mẫu, mục tiêu **κ ≥ 0.75**.
- Chèn **20-30 mẫu vàng** vào mỗi lô.
- Cập nhật rule khi gặp trường hợp mới, ghi **version** cho guideline (v1.0, v1.1...).
- Họp rà soát các mẫu bất đồng, bổ sung vào mục edge cases.