# **CHƯƠNG 3: XÂY DỰNG VÀ TRIỂN KHAI HỆ THỐNG**

Trên cơ sở các phương pháp đã trình bày trong Chương 2, chương này mô tả quá
trình phân tích, thiết kế và xây dựng hệ thống phân loại đánh giá Spam/Ham. Hệ
thống được tổ chức dưới dạng một pipeline xử lý dữ liệu hoàn chỉnh, bắt đầu từ
khâu thu thập đánh giá trên trang Điện Máy Xanh, tiếp theo là tiền xử lý, biểu
diễn văn bản, huấn luyện mô hình và kết thúc bằng việc đánh giá, lưu trữ kết quả.
Bên cạnh đó, dự án được đóng gói bằng Docker nhằm bảo đảm khả năng triển khai và
tái lập thí nghiệm trên các môi trường khác nhau.

## **3.1. Phân tích yêu cầu hệ thống**

### **3.1.1. Yêu cầu chức năng**

Mục tiêu của hệ thống là tự động phân loại một đánh giá tiếng Việt thành một
trong hai lớp: **Ham** đối với đánh giá hợp lệ và **Spam** đối với đánh giá rác.
Để thực hiện mục tiêu này, hệ thống cần đáp ứng các chức năng chính sau:

- Thu thập nội dung đánh giá sản phẩm từ website Điện Máy Xanh và lưu trữ dưới
  dạng dữ liệu có cấu trúc.
- Làm sạch và chuẩn hóa văn bản tiếng Việt, bao gồm Unicode, chữ hoa – chữ
  thường, teencode, ký tự lặp, đường dẫn, địa chỉ thư điện tử, số điện thoại và
  các biểu thức số.
- Phát hiện và xử lý các mẫu trùng lặp hoặc có nhãn mâu thuẫn trước khi phân chia
  dữ liệu.
- Biểu diễn văn bản bằng bốn phương pháp BoW, TF-IDF, Word2Vec và FastText.
- Huấn luyện, lựa chọn siêu tham số và đánh giá các mô hình Naive Bayes, SVM và
  FastText trên cùng một tập kiểm thử.
- Lưu mô hình, chỉ số đánh giá, ma trận nhầm lẫn và các trường hợp phân loại sai
  để phục vụ việc so sánh và phân tích.
- Cho phép triển khai lại toàn bộ quy trình trên một máy khác thông qua môi
  trường Docker.

### **3.1.2. Yêu cầu phi chức năng**

Ngoài các yêu cầu chức năng, hệ thống cần bảo đảm tính đúng đắn và khả năng tái
lập của thí nghiệm. Dữ liệu kiểm thử không được tham gia vào quá trình xây dựng
từ điển, học biểu diễn hoặc lựa chọn siêu tham số. Các mô hình phải sử dụng cùng
một phép chia Train/Test để kết quả so sánh có ý nghĩa. Những tham số có yếu tố
ngẫu nhiên được thiết lập cùng một giá trị `random_state=42`; Word2Vec và
FastText được huấn luyện bằng một luồng nhằm hạn chế sai khác giữa các lần chạy.

Hệ thống cũng cần có cấu trúc module rõ ràng để mỗi giai đoạn có thể được kiểm
tra và thực thi độc lập. Các kết quả trung gian phải được lưu lại thay vì tính
toán lại trong mọi lần thí nghiệm. Yêu cầu này đặc biệt cần thiết khi thực hiện
tìm kiếm siêu tham số cho nhiều mô hình và nhiều phương pháp biểu diễn văn bản.

## **3.2. Thiết kế hệ thống**

### **3.2.1. Kiến trúc tổng thể**

Hệ thống được thiết kế theo kiến trúc pipeline tuần tự. Mỗi khối đảm nhận một
nhiệm vụ riêng và trao đổi dữ liệu với khối tiếp theo thông qua các tệp CSV hoặc
artifact đã được tuần tự hóa. Kiến trúc tổng thể được thể hiện trong Hình 3.1.

```text
  Website Điện Máy Xanh
            │
            ▼
  Thu thập dữ liệu bằng Selenium
            │
            ▼
  Tiền xử lý và khử trùng lặp
            │
            ▼
  Chia tập Train/Test phân tầng
            │
            ├──────────┬──────────┬────────────┐
            ▼          ▼          ▼            ▼
           BoW       TF-IDF    Word2Vec      FastText
            │          │          │            │
            ├──── NB ──┼──── NB ──┼──── NB      │
            └─── SVM ──┴─── SVM ──┴─── SVM     │
                       │                       │
                       └───────────┬───────────┘
                                   ▼
                       Đánh giá và so sánh mô hình
                                   │
                                   ▼
                         Lưu kết quả thực nghiệm
```

*Hình 3.1. Kiến trúc tổng thể của hệ thống phân loại đánh giá Spam/Ham.*

Pipeline gồm năm phân hệ: thu thập dữ liệu, tiền xử lý, trích chọn đặc trưng,
huấn luyện mô hình và đánh giá kết quả. Việc phân chia thành các phân hệ giúp hệ
thống có tính mô-đun và dễ mở rộng. Chẳng hạn, một phương pháp biểu diễn văn bản
mới có thể được bổ sung mà không cần thay đổi chương trình thu thập và tiền xử
lý dữ liệu.

### **3.2.2. Luồng dữ liệu**

Dữ liệu ban đầu được crawler lưu dưới định dạng CSV. Sau khi được gán nhãn, mỗi
bản ghi gồm các thuộc tính danh mục sản phẩm, tên sản phẩm, nội dung đánh giá,
số sao và nhãn. Phân hệ tiền xử lý bổ sung hai trường `clean_text` và `split`.
Trong đó, `clean_text` là nội dung sau chuẩn hóa, còn `split` xác định bản ghi
thuộc tập Train hay Test.

Từ tệp dữ liệu đã xử lý, các chương trình trích chọn đặc trưng tạo ra ma trận
đặc trưng tương ứng. Mỗi artifact đặc trưng chứa `X_train`, `X_test`, `y_train`
và `y_test`, nhờ đó các chương trình huấn luyện không cần tự đọc và chia lại dữ
liệu. Bộ vector hóa BoW, TF-IDF và mô hình Word2Vec cũng được lưu riêng để bảo
toàn từ điển và các tham số đã học từ tập Train.

| Giai đoạn | Dữ liệu đầu vào | Kết quả đầu ra |
| :--- | :--- | :--- |
| Thu thập | Trang sản phẩm Điện Máy Xanh | Tệp CSV chứa đánh giá thô |
| Tiền xử lý | Dữ liệu đã gán nhãn | `processed.csv` |
| Trích chọn đặc trưng | `processed.csv` | Ma trận đặc trưng và vectorizer |
| Huấn luyện | Ma trận Train/Test | Mô hình đã tối ưu |
| Đánh giá | Nhãn thật và nhãn dự đoán | JSON, CSV, ảnh và bảng tổng hợp |

*Bảng 3.1. Luồng dữ liệu giữa các phân hệ.*

### **3.2.3. Tổ chức mã nguồn**

Mã nguồn được tổ chức theo chức năng thay vì theo từng thí nghiệm riêng lẻ. Thư
mục `data_collection/` chứa chương trình thu thập dữ liệu; `preprocess/` thực
hiện làm sạch và chia tập; `feature_extraction/` xây dựng các biểu diễn BoW,
TF-IDF và Word2Vec; `model/` chứa sáu cấu hình Naive Bayes và SVM;
`FastText_Performance/` chứa chương trình huấn luyện FastText. Các kết quả được
lưu thống nhất trong `results/`.

Cách tổ chức trên làm giảm sự phụ thuộc giữa các thành phần. Đặc biệt, phần đánh
giá chung được tách thành module `model/evaluate.py`. Do đó, mỗi tệp mô hình chỉ
cần khai báo thuật toán, không gian siêu tham số và loại đặc trưng cần sử dụng,
trong khi toàn bộ quy trình tìm kiếm, dự đoán, tính chỉ số và lưu kết quả được
thực hiện theo cùng một cách.

## **3.3. Xây dựng các phân hệ**

### **3.3.1. Phân hệ thu thập dữ liệu**

Dữ liệu đánh giá trên Điện Máy Xanh được hiển thị động bằng JavaScript. Vì vậy,
việc gửi yêu cầu HTTP và đọc mã HTML ban đầu không thu được đầy đủ nội dung.
Nhóm sử dụng Selenium WebDriver để điều khiển trình duyệt Chrome, mô phỏng các
thao tác của người dùng và đọc dữ liệu sau khi trang đã tải hoàn chỉnh.

Quá trình thu thập được thực hiện theo hình thức bán tự động. Người sử dụng mở
trang sản phẩm trong cửa sổ Chrome do chương trình tạo ra, xử lý captcha nếu có,
sau đó yêu cầu crawler đọc các đánh giá. Chương trình hỗ trợ cả hai hình thức
hiển thị thường gặp là chuyển trang và nhấn nút “Xem thêm”. Mỗi bản ghi thu được
gồm danh mục, tên sản phẩm, người đánh giá, số sao, nội dung và đường dẫn nguồn.

Để hạn chế trùng lặp, crawler sử dụng thuộc tính `data-comment-id` làm định danh
cho đánh giá. Các định danh đã gặp được lưu trong một tập hợp; một đánh giá chỉ
được thêm khi định danh của nó chưa xuất hiện trong phiên thu thập. Dữ liệu sau
cùng được lưu dưới dạng CSV để thuận tiện cho việc kiểm tra và gán nhãn.

### **3.3.2. Phân hệ tiền xử lý dữ liệu**

Phân hệ tiền xử lý được xây dựng trong tệp `preprocess/preprocess.py`. Đầu tiên,
chương trình loại bỏ các bản ghi thiếu nội dung hoặc thiếu nhãn. Mỗi đánh giá sau
đó được đưa qua hàm `clean_text()` để chuẩn hóa về cùng một biểu diễn. Các bước
được thực hiện theo thứ tự cố định nhằm bảo đảm dữ liệu huấn luyện và dữ liệu mới
được xử lý giống nhau.

Sau bước làm sạch, hệ thống nhóm dữ liệu theo `clean_text`. Nếu cùng một nội dung
có nhiều nhãn khác nhau, nhãn xuất hiện nhiều hơn được lựa chọn theo nguyên tắc
biểu quyết đa số. Tiếp theo, mỗi nội dung chuẩn hóa chỉ được giữ lại một lần.
Việc khử trùng lặp được thực hiện trước khi chia dữ liệu để ngăn cùng một câu
xuất hiện đồng thời trong Train và Test.

Dữ liệu còn lại được chia theo tỷ lệ 80% cho huấn luyện và 20% cho kiểm thử bằng
phương pháp phân tầng theo nhãn. Kết quả của phép chia được ghi trực tiếp vào cột
`split` của `processed.csv`. Nhờ đó, mọi mô hình đều sử dụng cùng các mẫu Train
và Test, loại bỏ một nguồn sai lệch có thể xuất hiện khi mỗi chương trình tự chia
dữ liệu độc lập.

### **3.3.3. Phân hệ trích chọn đặc trưng**

Đối với BoW và TF-IDF, nhóm sử dụng `CountVectorizer` và `TfidfVectorizer` của
scikit-learn. Hai bộ vector hóa chỉ được `fit` trên tập Train. Sau khi từ điển và
trọng số được xác lập, cùng bộ vector hóa đó được dùng để `transform` tập Test.
Quy trình này bảo đảm thông tin về từ vựng của tập Test không tham gia vào quá
trình xây dựng không gian đặc trưng.

Đối với Word2Vec, mô hình Skip-gram được huấn luyện từ các câu thuộc tập Train.
Mỗi đánh giá được biểu diễn bằng trung bình vector của những token có mặt trong
từ điển. Trường hợp không có token phù hợp được biểu diễn bằng vector toàn số 0.
Mô hình Word2Vec và các ma trận đặc trưng được lưu lại để sử dụng trong các cấu
hình Gaussian Naive Bayes và RBF SVM.

FastText được triển khai trong một module riêng. Thay vì tạo trước ma trận đặc
trưng, FastText nhận văn bản theo định dạng `__label__<nhãn> <nội dung>` và đồng
thời học biểu diễn subword với bộ phân loại. Tệp huấn luyện trung gian được tạo
trong thư mục tạm và tự động xóa sau khi hoàn thành, tránh sinh thêm dữ liệu
không cần thiết trong project.

### **3.3.4. Phân hệ huấn luyện và lựa chọn mô hình**

Sáu cấu hình kết hợp giữa Naive Bayes, SVM và ba loại đặc trưng truyền thống
được triển khai thành các chương trình độc lập. Khi một chương trình được thực
thi, module đánh giá nạp đúng artifact đặc trưng, sau đó sử dụng
`StratifiedKFold` gồm 5 fold để duy trì tỷ lệ Spam/Ham trong từng lần chia.

Quá trình lựa chọn siêu tham số được thực hiện bằng GridSearchCV và chỉ sử dụng
tập Train. Chỉ số tối ưu là F1-score của lớp Spam, thay vì Accuracy, do đây là
lớp thiểu số và cũng là đối tượng chính cần phát hiện. Sau khi tìm được cấu hình
tốt nhất, mô hình được huấn luyện lại trên toàn bộ tập Train rồi mới dự đoán tập
Test. Tập Test vì vậy chỉ được sử dụng một lần để báo cáo khả năng tổng quát hóa.

Đối với SVM kết hợp Word2Vec, `StandardScaler` và bộ phân loại RBF SVM được đặt
trong cùng một `Pipeline`. Thiết kế này có ý nghĩa quan trọng trong quá trình
cross-validation: bộ chuẩn hóa chỉ học trung bình và độ lệch chuẩn từ phần dữ
liệu huấn luyện của từng fold, không sử dụng dữ liệu validation của fold đó.

### **3.3.5. Phân hệ đánh giá và lưu kết quả**

Sau khi dự đoán, hệ thống tính Accuracy, Precision, Recall và F1-score của lớp
Spam, Macro-F1, ROC-AUC và PR-AUC. Với các mô hình có `predict_proba`, xác suất
của lớp Spam được sử dụng để xây dựng đường cong. Đối với SVM, hệ thống sử dụng
khoảng cách có dấu từ mẫu đến siêu phẳng thông qua `decision_function`.

Ngoài các chỉ số tổng hợp, hệ thống xây dựng ma trận nhầm lẫn và tách riêng hai
nhóm lỗi: Ham bị dự đoán thành Spam và Spam bị bỏ sót thành Ham. Những trường hợp
này được lưu vào CSV cùng điểm dự đoán để phục vụ phân tích định tính. Kết quả
của mỗi mô hình gồm bốn loại artifact như Bảng 3.2.

| Artifact | Nội dung và mục đích |
| :--- | :--- |
| `<model>.pkl` | Mô hình tốt nhất sau huấn luyện |
| `<model>.json` | Siêu tham số và các chỉ số đánh giá |
| `<model>_confusion_matrix.png` | Ma trận nhầm lẫn trực quan |
| `<model>_errors.csv` | Các mẫu bị phân loại sai |
| `summary.csv` | Bảng tổng hợp và so sánh các mô hình |

*Bảng 3.2. Các kết quả được sinh ra sau quá trình đánh giá.*

Việc tự động hóa bước lưu kết quả giúp hạn chế sai sót khi sao chép số liệu thủ
công. Tệp `summary.csv` được cập nhật sau mỗi thí nghiệm và sắp xếp theo F1-score
của lớp Spam, tạo nguồn dữ liệu thống nhất cho các bảng so sánh trong Chương 4.

## **3.4. Triển khai hệ thống**

### **3.4.1. Môi trường thực thi**

Hệ thống được phát triển bằng Python 3.11. Các thư viện chính gồm Pandas và NumPy
cho xử lý dữ liệu; scikit-learn cho vector hóa, huấn luyện và đánh giá; Gensim
cho Word2Vec; FastText cho biểu diễn subword; Joblib cho việc lưu mô hình; và
Matplotlib cho trực quan hóa. Danh sách phụ thuộc được khai báo trong các tệp
`requirements.txt`, giúp các thành viên cài đặt môi trường theo cùng một cấu
hình.

| Nhóm chức năng | Công nghệ sử dụng |
| :--- | :--- |
| Thu thập dữ liệu | Selenium, Chrome WebDriver |
| Xử lý và lưu trữ dữ liệu | Python, Pandas, NumPy, CSV |
| Học máy | scikit-learn, Gensim, FastText |
| Lưu mô hình và kết quả | Joblib, JSON, CSV |
| Trực quan hóa | Matplotlib |
| Đóng gói môi trường | Docker |

*Bảng 3.3. Môi trường và công nghệ triển khai hệ thống.*

### **3.4.2. Đóng gói bằng Docker**

Để giảm sự khác biệt về hệ điều hành và phiên bản thư viện, nhóm đóng gói
pipeline trong một Docker image. Image sử dụng `python:3.11-slim` làm nền, thiết
lập `/app` là thư mục làm việc, cài đặt các thư viện cần thiết và sao chép mã
nguồn vào container. So với việc cấu hình thủ công trên từng máy, Docker giúp
tạo ra môi trường thực thi thống nhất và có thể tái tạo.

Ba thư mục `data/`, `feature_extraction/features/` và `results/` được gắn từ máy
chủ vào container dưới dạng volume. Cơ chế này tách môi trường thực thi khỏi dữ
liệu lâu dài. Container có thể được xóa và tạo lại mà không làm mất dữ liệu đã
xử lý, vectorizer, mô hình hoặc kết quả thực nghiệm.

Quá trình triển khai được thực hiện theo hai bước. Trước hết, Docker tạo image từ
Dockerfile của project. Sau đó, container được khởi chạy ở chế độ tương tác với
các volume nêu trên. Trong container, các chương trình được thực thi tuần tự từ
tiền xử lý, trích chọn đặc trưng đến huấn luyện mô hình. Thứ tự này phản ánh quan
hệ phụ thuộc giữa các artifact và giúp hệ thống phát hiện sớm trường hợp thiếu
dữ liệu đầu vào.

### **3.4.3. Quy trình vận hành**

Quy trình vận hành của hệ thống gồm bốn bước. Đầu tiên, dữ liệu thô đã gán nhãn
được đưa vào module tiền xử lý để tạo `processed.csv`. Tiếp theo, ba chương trình
trích chọn đặc trưng lần lượt sinh các artifact BoW, TF-IDF và Word2Vec. Ở bước
thứ ba, các chương trình mô hình thực hiện tìm kiếm siêu tham số, huấn luyện và
đánh giá. Cuối cùng, nhóm kiểm tra `summary.csv`, ma trận nhầm lẫn và các tệp lỗi
để phân tích kết quả.

Trong mỗi giai đoạn, chương trình đều in ra thông tin kiểm tra. Bước tiền xử lý
báo số lượng bản ghi, phân bố nhãn và số mẫu bị loại; bước trích chọn đặc trưng
báo kích thước từ điển, kích thước ma trận và số câu không có đặc trưng; bước
đánh giá báo siêu tham số tốt nhất, các độ đo và thời gian xử lý. Những thông tin
này hỗ trợ phát hiện sớm lỗi dữ liệu hoặc sai lệch cấu hình trước khi kết quả
được sử dụng trong báo cáo.

## **3.5. Kiểm thử hệ thống**

Việc kiểm thử được thực hiện ở từng giai đoạn của pipeline. Đối với dữ liệu, hệ
thống kiểm tra giá trị thiếu, kiểu dữ liệu của nhãn, số lượng mẫu trước và sau
khử trùng lặp, cũng như tỷ lệ Spam/Ham trong hai tập. Đối với đặc trưng, kích
thước của `X_train`, `X_test`, `y_train` và `y_test` được đối chiếu để bảo đảm số
mẫu nhất quán.

Đối với quá trình huấn luyện, việc tách dữ liệu được kiểm tra thông qua cột
`split`; các vectorizer chỉ được học trên Train. GridSearchCV chỉ nhận
`X_train, y_train`, còn tập Test được giữ độc lập đến giai đoạn đánh giá cuối.
Các mô hình sau huấn luyện được lưu và có thể nạp lại bằng Joblib. Kết quả dự
đoán được kiểm tra thông qua ma trận nhầm lẫn, báo cáo phân loại và danh sách lỗi.

Hệ thống Docker được kiểm tra bằng cách xây dựng image và chạy lại pipeline với
các thư mục dữ liệu được gắn từ máy chủ. Các artifact tạo trong container xuất
hiện tại đúng thư mục trên máy chủ, cho thấy cơ chế lưu trữ kết quả hoạt động
đúng. Kết quả chi tiết về độ chính xác và hiệu năng của từng mô hình được trình
bày trong Chương 4.

## **3.6. Tiểu kết chương**

Chương này đã trình bày quá trình xây dựng hệ thống phân loại đánh giá Spam/Ham
từ khâu phân tích yêu cầu, thiết kế kiến trúc đến cài đặt và triển khai. Hệ thống
được tổ chức thành các phân hệ độc lập, sử dụng một phép chia dữ liệu chung và
tuân thủ nguyên tắc không sử dụng thông tin từ tập Test trong quá trình huấn
luyện. Các bước đánh giá và lưu kết quả được tự động hóa, tạo điều kiện so sánh
công bằng giữa các mô hình.

Việc đóng gói bằng Docker giúp môi trường thí nghiệm có khả năng tái lập và giảm
sai khác khi chạy trên nhiều máy. Phiên bản hiện tại tập trung vào xử lý theo lô
phục vụ mục tiêu nghiên cứu và so sánh mô hình. Trong tương lai, hệ thống có thể
được mở rộng thành dịch vụ suy luận thời gian thực, tiếp nhận đánh giá mới qua
API và trả về nhãn Spam/Ham cho các hệ thống thương mại điện tử.
