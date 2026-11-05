# BÁO CÁO BÀI TẬP LỚN MÔN HỌC: XỬ LÝ NGÔN NGỮ TỰ NHIÊN (NLP)

---

<div align="center">

### HỌC VIỆN CÔNG NGHỆ BƯU CHÍNH VIỄN THÔNG (PTIT)
### KHOA CÔNG NGHỆ THÔNG TIN
### BỘ MÔN KHOA HỌC MÁY TÍNH & TRÍ TUỆ NHÂN TẠO

---

[CHÈN HÌNH 0.1 TẠI ĐÂY: Logo Học viện Công nghệ Bưu chính Viễn thông (PTIT)]
*(Placeholder: /assets/images/logo_ptit.png - Kích thước khuyến nghị: 4cm x 4cm, căn giữa)*

---

## BÁO CÁO ĐỒ ÁN / BÀI TẬP LỚN

### ĐỀ TÀI:
# NGHIÊN CỨU, CÀI ĐẶT VÀ ĐÁNH GIÁ CÁC PHƯƠNG PHÁP HỌC MÁY KẾT HỢP BIỂU DIỄN VĂN BẢN TRONG BÀI TOÁN PHÂN LOẠI ĐÁNH GIÁ RÁC (SPAM/HAM REVIEWS) TIẾNG VIỆT TRÊN CÁC SÀN THƯƠNG MẠI ĐIỆN TỬ

</div>

<br><br>

**Thông tin chung về đề tài:**
- **Môn học:** Xử lý Ngôn ngữ Tự nhiên (Natural Language Processing - INT1434 / INT1449)
- **Giảng viên hướng dẫn:** Giảng viên phụ trách môn học Xử lý Ngôn ngữ Tự nhiên
- **Khoa:** Công nghệ Thông tin - Học viện Công nghệ Bưu chính Viễn thông
- **Nhóm sinh viên thực hiện:** Nhóm N2 - PTIT
- **Thời gian thực hiện:** Học kỳ I - Năm học 2025 - 2026
- **Hệ đào tạo:** Đại học chính quy ngành Công nghệ Thông tin / Khoa học Máy tính

<br><br>

<div align="center">
<b>HÀ NỘI – 2026</b>
</div>


ewpage

---

## LỜI CAM ĐOAN

Chúng tôi xin cam đoan báo cáo bài tập lớn với đề tài: *"Nghiên cứu, cài đặt và đánh giá các phương pháp học máy kết hợp biểu diễn văn bản trong bài toán phân loại đánh giá rác (Spam/Ham Reviews) tiếng Việt trên các sàn thương mại điện tử"* là công trình nghiên cứu và thực nghiệm độc lập của nhóm chúng tôi dưới sự định hướng, hướng dẫn khoa học của Giảng viên phụ trách bộ môn Xử lý Ngôn ngữ Tự nhiên.

Các kết quả thực nghiệm, số liệu phân tích, bảng biểu, ma trận nhầm lẫn và các đoạn mã nguồn trong toàn bộ báo cáo này được xây dựng, thu thập và tính toán một cách trung thực từ quy trình tiền xử lý, huấn luyện và đánh giá trên tập dữ liệu thực nghiệm tại môi trường nghiên cứu của nhóm. Mọi tài liệu, công trình nghiên cứu, công bố khoa học của các tác giả trong nước và quốc tế, cũng như các thư viện mã nguồn mở được kế thừa đều được nhóm chúng tôi trích dẫn đầy đủ, rõ ràng và minh bạch theo đúng quy chuẩn học thuật tại danh mục Tài liệu tham khảo.

Nhóm chúng tôi xin hoàn toàn chịu trách nhiệm trước Nhà trường, Khoa Công nghệ Thông tin và Bộ môn về tính chính xác và tính trung thực của toàn bộ nội dung trong bản báo cáo này.

<div align="right">
<i>Hà Nội, ngày 05 tháng 11 năm 2026</i><br>
<b>Đại diện nhóm sinh viên thực hiện</b><br>
<i>(Ký và ghi rõ họ tên)</i><br><br><br>
<b>Nhóm nghiên cứu N2 - PTIT</b>
</div>


ewpage

---

## LỜI CẢM ƠN

Để hoàn thành bản báo cáo bài tập lớn môn học Xử lý Ngôn ngữ Tự nhiên này một cách toàn diện và đạt được các kết quả thực nghiệm chuẩn mực, nhóm chúng tôi đã nhận được sự quan tâm, chỉ dẫn tận tình và tạo điều kiện thuận lợi từ các Thầy, Cô giáo và Nhà trường.

Lời đầu tiên, nhóm chúng tôi xin bày tỏ lòng biết ơn sâu sắc nhất tới các Thầy, Cô giáo trong Bộ môn Khoa học Máy tính & Trí tuệ Nhân tạo, Khoa Công nghệ Thông tin - Học viện Công nghệ Bưu chính Viễn thông (PTIT). Trong suốt quá trình học tập trên giảng đường, các Thầy Cô đã truyền đạt cho chúng tôi những nền tảng tri thức học thuật vững chắc, từ lý thuyết xác suất thống kê, đại số tuyến tính đến các thuật toán học máy cổ điển và các kỹ thuật xử lý ngôn ngữ tự nhiên hiện đại. Những kiến thức quý báu đó chính là kim chỉ nam và nền tảng tư duy vững vàng giúp chúng tôi giải quyết các bài toán kỹ thuật phức tạp trong đề tài.

Đặc biệt, nhóm chúng tôi xin trân trọng gửi lời cảm ơn sâu sắc nhất tới Giảng viên hướng dẫn môn học Xử lý Ngôn ngữ Tự nhiên. Trong suốt thời gian thực hiện bài tập lớn, Thầy/Cô đã dành nhiều thời gian định hướng đề tài, giải đáp các thắc mắc về phương pháp luận, phản biện chặt chẽ quy trình thí nghiệm nhằm đảm bảo tính toàn vẹn của dữ liệu (ngăn ngừa hiện tượng rò rỉ dữ liệu - data leakage), và đưa ra những lời khuyên chuyên môn sâu sắc giúp nhóm hoàn thiện cả về mã nguồn lẫn kỹ năng viết báo cáo khoa học.

Cuối cùng, nhóm chúng tôi xin gửi lời cảm ơn chân thành tới gia đình, bạn bè và các bạn sinh viên cùng khóa đã luôn động viên, chia sẻ kinh nghiệm kỹ thuật và tạo điều kiện tốt nhất để nhóm hoàn thành nhiệm vụ nghiên cứu đúng tiến độ. Dù đã nỗ lực hết mình với tinh thần nghiên cứu nghiêm túc, báo cáo chắc chắn khó tránh khỏi những thiếu sót nhất định. Nhóm chúng tôi rất mong nhận được những nhận xét, góp ý quý báu của Quý Thầy Cô để công trình được hoàn thiện hơn nữa trong các hướng nghiên cứu tương lai.

*Chúng tôi xin chân thành cảm ơn!*


ewpage

---

## TÓM TẮT ĐỀ TÀI (ABSTRACT)

### TÓM TẮT TIẾNG VIỆT
Sự bùng nổ của thương mại điện tử (TMĐT) tại Việt Nam trong những năm gần đây đã biến các đánh giá của người dùng (Customer Reviews) trở thành nguồn thông tin tối quan trọng, định hình hành vi mua sắm của người tiêu dùng và quyết định doanh số cũng như danh tiếng của các nhà bán lẻ. Tuy nhiên, tình trạng ô nhiễm thông tin do các "đánh giá rác" (Spam Reviews) — bao gồm các bình luận quảng cáo, lừa đảo, chèo kéo sang kênh cá nhân (Zalo, SĐT), tin nhắn vô nghĩa tích xu thưởng, hay các đánh giá giả mạo nhằm thao túng xếp hạng — đang gây ảnh hưởng nghiêm trọng tới trải nghiệm khách hàng và tính minh bạch của thị trường số. Việc phát hiện và sàng lọc tự động các đánh giá rác là một bài toán cấp thiết nhưng đối mặt với nhiều thách thức lớn: ngôn ngữ mạng tiếng Việt phi hình thức (teencode, viết tắt, từ lóng, biến thể ngữ âm), hiện tượng mất cân bằng lớp trầm trọng (Spam chỉ chiếm thiểu số), và đặc biệt là nguy cơ rò rỉ dữ liệu (Data Leakage) do người dùng thường xuyên để lại các bình luận ngắn trùng lặp ("Tốt", "Ok").

Báo cáo bài tập lớn này trình bày một nghiên cứu thực nghiệm toàn diện, có tính hệ thống cao về bài toán phân loại đánh giá rác tiếng Việt (Spam vs. Ham Reviews) trong lĩnh vực thiết bị điện máy gia dụng. Nhóm tác giả đã xây dựng một pipeline học máy chuẩn mực và khép kín:
1. **Tiền xử lý nâng cao và chống rò rỉ thông tin:** Chuẩn hóa Unicode NFC, chuyển chữ thường, khử ký tự lặp cảm xúc, trừu tượng hóa các thực thể nhạy cảm (URL, Email, SĐT, Số tiền) thành các token đặc trưng (`urltoken`, `phonetoken`, `numtoken`), xây dựng từ điển giải mã teencode chuyên ngành, giải quyết triệt để 55.7% số câu ngắn trùng lặp trước khi phân chia tập dữ liệu phân tầng (Stratified Split 80/20) để đảm bảo tính khách quan tuyệt đối.
2. **Khảo sát đa không gian biểu diễn văn bản:** So sánh từ không gian vector thưa đa chiều (Bag-of-Words kết hợp n-gram 1-2, TF-IDF với sublinear scaling và chuẩn hóa L2 norm) đến không gian vector nhúng liên tục dày đặc (Word2Vec kiến trúc Skip-gram với kỹ thuật Pooling câu).
3. **Mô hình hóa và tối ưu hóa siêu tham số:** Đánh giá 6 cấu hình mô hình học máy gồm 3 biến thể Naive Bayes (MultinomialNB, ComplementNB, GaussianNB) và 2 cấu hình Máy vector hỗ trợ (Linear SVM và RBF SVM kết hợp StandardScaler và cân bằng trọng số lớp `class_weight='balanced'`), được dò tìm tham số tối ưu thông qua 5-Fold Stratified Cross-Validation trên tập Train.

Kết quả thực nghiệm trên tập kiểm thử độc lập (964 mẫu) chỉ ra rằng:
- Mô hình **RBF SVM kết hợp Word2Vec (dense embedding)** đạt hiệu năng toàn diện xuất sắc nhất với **F1-Score (Spam) đạt 88.37%**, **Accuracy đạt 95.85%**, **ROC-AUC đạt 0.9859**, và **PR-AUC đạt 0.9265**, duy trì độ cân bằng tối ưu giữa Precision (86.86%) và Recall (89.94%).
- Mô hình **Linear SVM kết hợp Bag-of-Words** thể hiện ưu thế vượt trội về khả năng phát hiện triệt để spam với **Recall đạt tới 94.67%** (chỉ bỏ sót 9 trên tổng số 169 mẫu spam), đạt **F1-Score 84.88%**.
- Ngược lại, **Gaussian Naive Bayes trên Word2Vec** thể hiện hiệu năng kém nhất (**F1-Score chỉ đạt 61.24%**) do vi phạm nghiêm trọng giả định độc lập có điều kiện giữa các chiều vector embedding.
- Toàn bộ các mô hình học máy đề xuất đều có tốc độ suy luận cực nhanh (chỉ từ 0.4 µs đến 59 µs trên mỗi mẫu đánh giá), chứng minh tính khả thi vượt trội để triển khai vận hành thời gian thực tại các hệ thống thương mại điện tử thực tế.

**Từ khóa:** *Xử lý ngôn ngữ tự nhiên (NLP), Phân loại đánh giá rác (Spam Reviews Detection), Tiếng Việt, Bag-of-Words, TF-IDF, Word2Vec, Naive Bayes, Support Vector Machine (SVM), Mất cân bằng dữ liệu, Rò rỉ dữ liệu.*

---

### ABSTRACT IN ENGLISH
The rapid expansion of e-commerce platforms in Vietnam has positioned online customer reviews as a paramount information asset, heavily dictating consumer buying decisions and brand equity. Concurrently, the proliferation of "review spam" — ranging from commercial advertisements, phishing schemes, and social network solicitation (Zalo, phone numbers) to meaningless coin-farming comments and deceptive opinion spam — poses a substantial threat to platform integrity. Automatically identifying spam reviews in Vietnamese presents multifaceted challenges: highly informal netspeak (teencode, abbreviations, slang, non-standard spelling), severe class imbalance (spam represents a small minority), and substantial risk of data leakage induced by massive repetitive short comments (e.g., "Good", "Ok").

This study introduces a rigorous, systematic empirical investigation into Vietnamese e-commerce review spam detection across consumer electronics categories. We design and implement an end-to-end machine learning pipeline encompassing:
1. **Robust Preprocessing & Leakage Mitigation:** Unicode NFC normalization, lowercasing, emotional character repetition reduction, abstract entity tokenization (`urltoken`, `phonetoken`, `numtoken`), customized domain teencode decoding, majority voting for label conflicts, and a critical deduplication strategy eliminating 55.7% repetitive rows prior to stratified 80/20 train/test splitting.
2. **Multi-Space Text Representations:** Comparative analysis across high-dimensional sparse representations (Bag-of-Words with unigram/bigram combinations, TF-IDF with sublinear term scaling and L2 normalization) and continuous dense vector representations (Word2Vec Skip-gram with sentence pooling).
3. **Classification Modeling & Hyperparameter Optimization:** Exhaustive evaluation of six configurations across three Naive Bayes variants (MultinomialNB, ComplementNB, GaussianNB) and Support Vector Machines (LinearSVC and Kernel RBF with StandardScaler and `class_weight='balanced'`), optimized through 5-Fold Stratified Cross-Validation on the training subset.

Empirical evaluations on a strictly isolated test set of 964 samples reveal that:
- **RBF Kernel SVM coupled with Word2Vec sentence embeddings** achieves the superior overall performance, yielding a **Spam F1-Score of 88.37%**, **Accuracy of 95.85%**, **ROC-AUC of 0.9859**, and **PR-AUC of 0.9265**, effectively balancing high precision (86.86%) and recall (89.94%).
- **Linear SVM trained on Bag-of-Words** demonstrates exceptional sensitivity with a **Spam Recall of 94.67%** (overlooking only 9 out of 169 spam reviews) and an F1-Score of 84.88%.
- In contrast, **Gaussian Naive Bayes paired with Word2Vec** underperforms significantly (**F1-Score of 61.24%**), theoretically attributed to the severe violation of the conditional feature independence assumption within dense semantic vector spaces.
- All proposed models exhibit ultra-fast inference speeds (ranging from 0.4 µs to 59 µs per sample), affirming high commercial feasibility for high-throughput real-time deployment in production environments.

**Keywords:** *Natural Language Processing (NLP), Spam Review Detection, Vietnamese Text Processing, Bag-of-Words, TF-IDF, Word2Vec, Naive Bayes, Support Vector Machines (SVM), Class Imbalance, Data Leakage Prevention.*


ewpage

---

## MỤC LỤC

- **LỜI CAM ĐOAN**
- **LỜI CẢM ƠN**
- **TÓM TẮT ĐỀ TÀI (ABSTRACT)**
- **MỤC LỤC**
- **DANH MỤC CHỮ VIẾT TẮT**
- **DANH MỤC BẢNG BIỂU**
- **DANH MỤC HÌNH VẼ**

---

### **CHƯƠNG 1: TỔNG QUAN**
- **1.1. Tổng quan về bài toán phân loại đánh giá rác (Spam/Ham Reviews)**
  - 1.1.1. Khái niệm và đặc điểm của đánh giá rác trên thương mại điện tử
  - 1.1.2. Ý nghĩa thực tiễn và những thách thức của bài toán
- **1.2. Các hướng tiếp cận trong phân loại văn bản**
  - 1.2.1. Phương pháp dựa trên luật và từ điển
  - 1.2.2. Phương pháp dựa trên Học máy (Machine Learning)
  - 1.2.3. Phương pháp dựa trên Học sâu (Deep Learning)
- **1.3. Các nghiên cứu liên quan**
- **1.4. Mục tiêu và phạm vi của đề tài**

---

### **CHƯƠNG 2: PHÂN LOẠI ĐÁNH GIÁ DỰA TRÊN HỌC MÁY VÀ BIỂU DIỄN VĂN BẢN**
- **2.1. Tiền xử lý dữ liệu văn bản**
  - 2.1.1. Làm sạch văn bản, xóa ký tự đặc biệt và chuẩn hóa chữ thường
  - 2.1.2. Tách từ (Tokenization) và loại bỏ từ dừng (Stopwords)
- **2.2. Trích chọn đặc trưng và biểu diễn văn bản**
  - 2.2.1. Mô hình Túi từ - Bag of Words (BoW)
  - 2.2.2. Phương pháp trọng số TF-IDF
  - 2.2.3. Biểu diễn từ trong không gian vector liên tục - Word2Vec
- **2.3. Huấn luyện mô hình học máy cho bài toán phân loại**
  - 2.3.1. Mô hình phân loại xác suất Naive Bayes
  - 2.3.2. Mô hình Máy vector hỗ trợ - Support Vector Machine (SVM)
  - 2.3.3. Sơ đồ quy trình tổng thể (Pipeline) của hệ thống đề xuất

---

### **CHƯƠNG 3: THỰC NGHIỆM VÀ ĐÁNH GIÁ KẾT QUẢ**
- **3.1. Thu thập và xử lý dữ liệu thực nghiệm**
  - 3.1.1. Mô tả tập dữ liệu gốc
  - 3.1.2. Kỹ thuật lọc, tăng cường dữ liệu và kết quả sau tiền xử lý
- **3.2. Môi trường cài đặt và các độ đo đánh giá**
  - 3.2.1. Môi trường và công cụ triển khai thực nghiệm
  - 3.2.2. Các độ đo đánh giá (Accuracy, Precision, Recall, F1-Score, Confusion Matrix)
- **3.3. Kết quả thực nghiệm**
  - 3.3.1. Kết quả thực nghiệm với mô hình Naive Bayes (trên 3 bộ đặc trưng BoW, TF-IDF, Word2Vec)
  - 3.3.2. Kết quả thực nghiệm với mô hình SVM (trên 3 bộ đặc trưng BoW, TF-IDF, Word2Vec)
  - 3.3.3. So sánh tổng hợp và phân tích hiệu năng giữa các phương pháp
- **3.4. Kết luận và hướng phát triển**
  - 3.4.1. Kết quả đạt được
  - 3.4.2. Ưu, nhược điểm của phương pháp
  - 3.4.3. Hướng phát triển trong tương lai

---

- **TÀI LIỆU THAM KHẢO**
- **PHỤ LỤC**
  - Phụ lục A: Hướng dẫn đóng gói và triển khai hệ thống với Docker
  - Phụ lục B: Cấu trúc mã nguồn chi tiết của dự án
  - Phụ lục C: Bảng tổng hợp không gian tìm kiếm siêu tham số trong GridSearchCV


ewpage

---

## DANH MỤC CHỮ VIẾT TẮT

| Viết tắt | Thuật ngữ Tiếng Anh | Diễn giải Tiếng Việt |
| :--- | :--- | :--- |
| **NLP** | Natural Language Processing | Xử lý ngôn ngữ tự nhiên |
| **ML** | Machine Learning | Học máy |
| **DL** | Deep Learning | Học sâu |
| **TMĐT** | E-commerce | Thương mại điện tử |
| **BoW** | Bag of Words | Mô hình túi từ |
| **TF** | Term Frequency | Tần suất xuất hiện của từ trong văn bản |
| **IDF** | Inverse Document Frequency | Nghịch đảo tần suất văn bản |
| **TF-IDF** | Term Frequency - Inverse Document Frequency | Trọng số tần suất từ - nghịch đảo tần suất văn bản |
| **WE** | Word Embedding | Nhúng từ (Biểu diễn từ trong không gian vector liên tục) |
| **CBOW** | Continuous Bag of Words | Kiến trúc túi từ liên tục (trong Word2Vec) |
| **SG** | Skip-Gram | Kiến trúc Skip-gram (trong Word2Vec) |
| **NB** | Naive Bayes | Bộ phân loại xác suất Bayes ngây thơ |
| **MNB** | Multinomial Naive Bayes | Naive Bayes phân phối đa thức |
| **CNB** | Complement Naive Bayes | Naive Bayes dựa trên lớp phần bù |
| **GNB** | Gaussian Naive Bayes | Naive Bayes phân phối chuẩn Gaussian |
| **SVM** | Support Vector Machine | Máy vector hỗ trợ |
| **LinearSVC** | Linear Support Vector Classifier | Bộ phân loại SVM với hàm nhân tuyến tính |
| **RBF** | Radial Basis Function | Hàm nhân bán kính cơ sở (nhân Gaussian) |
| **CV** | Cross-Validation | Kiểm định chéo (đánh giá chéo) |
| **TP** | True Positive | Mẫu dương tính thực sự (Spam đoán đúng là Spam) |
| **TN** | True Negative | Mẫu âm tính thực sự (Ham đoán đúng là Ham) |
| **FP** | False Positive | Mẫu dương tính giả (Ham đoán nhầm thành Spam) |
| **FN** | False Negative | Mẫu âm tính giả (Spam đoán nhầm thành Ham / Bỏ sót spam) |
| **PR-AUC** | Precision-Recall Area Under Curve | Diện tích dưới đường cong Precision-Recall |
| **ROC-AUC** | Receiver Operating Characteristic - Area Under Curve | Diện tích dưới đường cong đặc trưng hoạt động bộ thu |
| **OOV** | Out-of-Vocabulary | Từ nằm ngoài từ điển huấn luyện |
| **NFC** | Normalization Form C | Chuẩn hóa Unicode dựng sẵn |
| **NFD** | Normalization Form D | Chuẩn hóa Unicode tổ hợp |
| **URL** | Uniform Resource Locator | Địa chỉ tài nguyên web |
| **SĐT** | Phone Number | Số điện thoại |


ewpage

---

## DANH MỤC BẢNG BIỂU

- **Bảng 1.1:** Phân loại các dạng đánh giá rác (Spam Reviews) trên nền tảng thương mại điện tử.
- **Bảng 1.2:** So sánh tổng hợp các hướng tiếp cận phân loại văn bản (Rule-based, Học máy truyền thống, Học sâu).
- **Bảng 1.3:** Tổng hợp các công trình nghiên cứu tiêu biểu liên quan đến phát hiện đánh giá giả mạo và phân loại văn bản tiếng Việt.
- **Bảng 2.1:** Bảng ánh xạ chuẩn hóa viết tắt và teencode tiếng Việt trong thương mại điện tử.
- **Bảng 2.2:** So sánh các đặc tính không gian đặc trưng giữa BoW, TF-IDF và Word2Vec.
- **Bảng 2.3:** Bảng tổng hợp các biến thể Naive Bayes và lý do lựa chọn cho từng loại không gian biểu diễn.
- **Bảng 3.1:** Thống kê phân bố số lượng đánh giá theo 10 danh mục sản phẩm điện máy trong tập dữ liệu.
- **Bảng 3.2:** Thống kê phân bố số lượng đánh giá theo số sao (Rating) trong tập dữ liệu thực nghiệm.
- **Bảng 3.3:** Thống kê số lượng mẫu và tỷ lệ phân bố lớp trước và sau khi lọc trùng lặp.
- **Bảng 3.4:** Phân bố số lượng mẫu tập Train và Test sau khi phân chia phân tầng (Stratified 80/20).
- **Bảng 3.5:** Một số ví dụ cụ thể về câu đánh giá trước và sau khi thực hiện tiền xử lý làm sạch.
- **Bảng 3.6:** Ma trận nhầm lẫn tổng quát (Confusion Matrix) cho bài toán phân loại nhị phân Spam/Ham.
- **Bảng 3.7:** Kết quả thực nghiệm chi tiết của các biến thể mô hình Naive Bayes trên 3 bộ đặc trưng.
- **Bảng 3.8:** Ma trận nhầm lẫn chi tiết của 3 biến thể mô hình Naive Bayes trên tập Test.
- **Bảng 3.9:** Kết quả thực nghiệm chi tiết của các biến thể mô hình SVM trên 3 bộ đặc trưng.
- **Bảng 3.10:** Ma trận nhầm lẫn chi tiết của 3 biến thể mô hình SVM trên tập Test.
- **Bảng 3.11:** Bảng so sánh tổng hợp hiệu năng phân loại của toàn bộ 6 mô hình thực nghiệm trên tập Test.
- **Bảng 3.12:** Đánh giá hiệu năng tính toán và dung lượng lưu trữ của các mô hình thực nghiệm.
- **Bảng 3.13:** Phân tích định tính các ví dụ thực tế bị phân loại sai dạng Dương tính giả (False Positives - Ham bị báo nhầm là Spam).
- **Bảng 3.14:** Phân tích định tính các ví dụ thực tế bị phân loại sai dạng Âm tính giả (False Negatives - Spam bị bỏ sót thành Ham).


ewpage

---

## DANH MỤC HÌNH VẼ

- **Hình 0.1:** Logo Học viện Công nghệ Bưu chính Viễn thông (PTIT).
- **Hình 1.1:** Minh họa các dạng đánh giá rác (Spam reviews) điển hình trên các sàn thương mại điện tử Việt Nam.
- **Hình 2.1:** Quy trình chuẩn hóa và làm sạch văn bản tiếng Việt cho bài toán phân loại đánh giá.
- **Hình 2.2:** Minh họa trực quan không gian vector thưa trong mô hình Bag-of-Words (BoW).
- **Hình 2.3:** Đồ thị phân phối giá trị nghịch đảo tần suất văn bản (IDF) giữa các từ phổ biến và từ đặc trưng.
- **Hình 2.4:** Kiến trúc mạng nơ-ron Skip-gram trong mô hình Word2Vec.
- **Hình 2.5:** Cơ chế tìm siêu phẳng phân tách tối ưu và khoảng cách lề (Margin) trong Support Vector Machine.
- **Hình 2.6:** Sơ đồ quy trình tổng thể (Pipeline) của hệ thống phân loại đánh giá rác đề xuất.
- **Hình 3.1:** Phân bố độ dài câu (số lượng token) trong tập dữ liệu sau bước làm sạch tiền xử lý.
- **Hình 3.2:** Ma trận nhầm lẫn (Confusion Matrix) của mô hình Multinomial Naive Bayes + Bag of Words (`results/nb-bow_confusion_matrix.png`).
- **Hình 3.3:** Ma trận nhầm lẫn (Confusion Matrix) của mô hình Complement Naive Bayes + TF-IDF (`results/nb-tfidf_confusion_matrix.png`).
- **Hình 3.4:** Ma trận nhầm lẫn (Confusion Matrix) của mô hình Gaussian Naive Bayes + Word Embedding (`results/nb-we_confusion_matrix.png`).
- **Hình 3.5:** Ma trận nhầm lẫn (Confusion Matrix) của mô hình Linear SVM + Bag of Words (`results/svm-bow_confusion_matrix.png`).
- **Hình 3.6:** Ma trận nhầm lẫn (Confusion Matrix) của mô hình Linear SVM + TF-IDF (`results/svm-tfidf_confusion_matrix.png`).
- **Hình 3.7:** Ma trận nhầm lẫn (Confusion Matrix) của mô hình RBF SVM + Word Embedding (`results/svm-we_confusion_matrix.png`).
- **Hình 3.8:** Biểu đồ cột đối sánh các chỉ số hiệu năng chính (Accuracy, Precision, Recall, F1-Spam, ROC-AUC, PR-AUC) giữa 6 mô hình.
- **Hình 3.9:** Đồ thị tương quan giữa thời gian huấn luyện và hiệu năng F1-Score của các mô hình thực nghiệm.


ewpage

# CHƯƠNG 1: TỔNG QUAN

Trong kỷ nguyên số hóa và chuyển đổi mô hình kinh doanh hiện đại, thương mại điện tử (E-Commerce) đã trở thành một phần không thể thiếu trong đời sống kinh tế - xã hội tại Việt Nam và trên toàn thế giới. Hàng triệu người tiêu dùng mỗi ngày truy cập vào các nền tảng thương mại điện tử như Shopee, Lazada, Tiki, TikTok Shop, Điện Máy Xanh, Thế Giới Di Động để tìm kiếm, so sánh và ra quyết định mua sắm hàng hóa. Trong toàn bộ hành trình trải nghiệm khách hàng (Customer Journey), các bài đánh giá, nhận xét và bình luận của người dùng (Customer Reviews / Feedback) đóng vai trò là nguồn dữ liệu xã hội (Social Proof) có sức ảnh hưởng mang tính quyết định. Tuy nhiên, sự phụ thuộc ngày càng lớn vào hệ thống đánh giá trực tuyến đã thúc đẩy sự xuất hiện và lan rộng của một hiện tượng tiêu cực: **Đánh giá rác (Spam Reviews)** hay còn gọi là **Đánh giá giả mạo (Fake/Deceptive Reviews)**.

Chương 1 này sẽ cung cấp bức tranh toàn cảnh về bài toán phân loại đánh giá rác trên thương mại điện tử: từ các khái niệm nền tảng, phân loại chi tiết các hình thái spam, những đặc thù ngôn ngữ tiếng Việt, ý nghĩa thực tiễn và các thách thức khoa học; cho đến việc khảo sát toàn diện các hướng tiếp cận trong phân loại văn bản, tổng quan các công trình nghiên cứu trong và ngoài nước, và xác định rõ mục tiêu, phạm vi nghiên cứu của đề tài.

---

## 1.1. Tổng quan về bài toán phân loại đánh giá rác (Spam/Ham Reviews)

### 1.1.1. Khái niệm và đặc điểm của đánh giá rác trên thương mại điện tử

#### 1. Định nghĩa khoa học về đánh giá rác (Spam Reviews)
Trong lĩnh vực khai phá văn bản (Text Mining) và xử lý ngôn ngữ tự nhiên (Natural Language Processing - NLP), bài toán phân loại đánh giá rác được xếp vào nhóm bài toán phát hiện gian lận và lọc thông tin độc hại (Fraud Detection & Information Filtering). Theo định nghĩa kinh điển của Nitin Jindal và Bing Liu (2007, 2008) tại Đại học Illinois Chicago — hai nhà khoa học tiên phong đặt nền móng cho hướng nghiên cứu này:

> *"Đánh giá rác (Spam Review hay Opinion Spam) là những bài nhận xét, bình luận hoặc đánh giá được cố tình tạo ra trên các nền tảng trực tuyến nhằm mục đích thao túng nhận thức của người tiêu dùng, phục vụ động cơ cá nhân của người viết (quảng cáo, trục lợi, cạnh tranh không lành mạnh), hoặc hoàn toàn không mang giá trị thông tin chân thực liên quan đến trải nghiệm sử dụng sản phẩm, dịch vụ."*

Ngược lại với đánh giá rác, các đánh giá hợp lệ được gọi là **Ham Reviews** (hoặc Genuine/Legitimate Reviews). Đây là những bài nhận xét xuất phát từ người mua hàng thực tế (Authentic Buyers), phản ánh trung thực trải nghiệm sử dụng, cảm nhận khách quan về chất lượng sản phẩm, độ hoàn thiện, tính năng, hoặc thái độ phục vụ của đơn vị bán lẻ.

#### 2. Phân loại các hình thái đánh giá rác trên thương mại điện tử
Dựa trên quan sát thực tế tại các nền tảng thương mại điện tử hàng đầu tại Việt Nam và đối chiếu với các khung phân loại học thuật quốc tế (Jindal & Liu, 2008; Crawford et al., 2015), đánh giá rác được chia thành 4 nhóm hình thái chủ đạo được tóm tắt tại **Bảng 1.1**:

*Bảng 1.1: Phân loại các dạng đánh giá rác (Spam Reviews) trên nền tảng thương mại điện tử.*

| Nhóm hình thái | Tên tiếng Anh | Mục đích / Động cơ | Biểu hiện đặc trưng trên sàn TMĐT | Ví dụ thực tế |
| :--- | :--- | :--- | :--- | :--- |
| **Loại 1: Đánh giá giả mạo lừa đảo** | *Deceptive Opinion Spam* | Thao túng xếp hạng sản phẩm; thổi phồng hoặc hạ bệ đối thủ. | - Thổi phồng (Hyper-promotional): Khen ngợi quá đà, dùng ngôn từ sáo rỗng, lặp lại tên nhãn hàng.<br>- Bôi nhọ ác ý (Malicious Defamation): Chê bai thậm tệ vô căn cứ để dìm hàng đối thủ. | *"Sản phẩm tốt nhất hệ mặt trời, nên mua ngay và luôn ở shop này nhé mn!"*<br>hoặc *"Đồ lừa đảo đừng mua tẩy chay đi!"* |
| **Loại 2: Đánh giá quảng cáo và chèo kéo** | *Advertisement & Solicitation Spam* | Chuyển đổi lưu lượng truy cập sang kênh khác; lừa đảo tài chính/dịch vụ ngoài sàn. | Chèn số điện thoại, tài khoản mạng xã hội (Zalo, Facebook, Telegram), đường dẫn website, mời gọi làm cộng tác viên, dịch vụ cho vay tiền, cờ bạc trực tuyến. | *"Hàng xài ok. Ai cần vay vốn nhanh lãi suất thấp liên hệ zalo 0987xxxxxx"*<br>hoặc *"Vào link nhận quà: http://bit.ly/..."* |
| **Loại 3: Đánh giá vô nghĩa và nhiễu loạn** | *Nonsense & Character Spam* | "Cày" xu thưởng, lấy điểm tích lũy hoặc mã giảm giá (Voucher) của sàn. | Gõ phím vô nghĩa liên tục, lặp lại một ký tự nhiều lần, chỉ chứa một dấu chấm hoặc chuỗi dấu câu, sao chép lời bài hát hoặc đoạn văn ngẫu nhiên. | *"dddddddddddddddddddd"*<br>*"Ok ...."*<br>*"aaaaaaaaaaa lấy xu nhé"* |
| **Loại 4: Đánh giá lạc đề** | *Irrelevant / Off-topic Spam* | Người dùng không hiểu quy trình hoặc cố tình phàn nàn sai kênh. | Bình luận hoàn toàn không liên quan đến sản phẩm (phàn nàn thời tiết, đánh giá thái độ anh shipper giao hàng khi đang nhận xét chất lượng nồi cơm điện). | *"Shipper giao chậm trời mưa làm ướt hộp, bực cả mình"* (đánh giá cho tivi) |

---

[CHÈN HÌNH 1.1 TẠI ĐÂY: Minh họa các dạng đánh giá rác (Spam reviews) điển hình trên các sàn thương mại điện tử Việt Nam]
*(Placeholder: /assets/images/hinh1_1_cac_dang_spam_reviews.png - Kích thước khuyến nghị: 15cm x 8cm, căn giữa)*

---

#### 3. Đặc điểm ngữ âm, hình thái và từ vựng đặc thù của tiếng Việt trên TMĐT
Khác với các văn bản hành chính, tin tức báo chí hay tài liệu kỹ thuật vốn có cấu trúc ngữ pháp chuẩn mực, dữ liệu đánh giá trên các sàn thương mại điện tử Việt Nam mang tính phi hình thức (Informal Social Text) cực kỳ cao. Những đặc thù này tạo ra độ phức tạp rất lớn cho các thuật toán xử lý ngôn ngữ tự nhiên:

1. **Hiện tượng Teencode, viết tắt và tiếng lóng mạng:**
   Người dùng Việt Nam, đặc biệt là thế hệ trẻ, có xu hướng gõ tắt tối đa để tiết kiệm thời gian hoặc do thói quen gõ phím trên màn hình cảm ứng điện thoại:
   - Các từ phủ định bị biến đổi đa dạng: *"không"* $	o$ *"k"*, *"ko"*, *"kh"*, *"khong"*, *"hok"*, *"hông"*, *"kg"*, *"khg"*.
   - Các trợ từ, đại từ phổ biến: *"được"* $	o$ *"dc"*, *"đc"*, *"duoc"*, *"dk"*; *"sản phẩm"* $	o$ *"sp"*; *"nhân viên"* $	o$ *"nv"*; *"mình"* $	o$ *"mk"*, *"mik"*; *"mọi người"* $	o$ *"mn"*; *"với"* $	o$ *"vs"*; *"rồi"* $	o$ *"r"*, *"rùi"*.
   - Tên riêng của đơn vị bán lẻ: *"Điện Máy Xanh"* $	o$ *"dmx"*; *"Thế Giới Di Động"* $	o$ *"tgdd"*; *"bảo hành"* $	o$ *"bh"*.
   - Lời cảm ơn biến thể: *"thanks"*, *"tks"*, *"thank"*, *"cảm ơn"*.
2. **Hiện tượng kéo dài nguyên âm và phụ âm (Character Stretching):**
   Người dùng thường gõ lặp lại các ký tự để biểu thị cảm xúc cực đoan (khen nức nở hoặc chê thậm tệ), hoặc cố tình tạo biến thể để qua mặt các bộ lọc từ khóa đơn giản của sàn: *"tốttttt"*, *"êm ruuuu"*, *"dở tệeeeee"*, *"mát rượiii"*.
3. **Sự đa dạng về phương ngữ vùng miền (Regional Dialects):**
   Ngôn ngữ đánh giá phản ánh văn phong đời sống thường ngày của ba miền Bắc - Trung - Nam:
   - Miền Nam thường sử dụng: *"sài"* (thay cho *"dùng"*, *"xài"*), *"hông"* (thay cho *"không"*), *"bền dữ"* (thay cho *"rất bền"*), *"mau"* (thay cho *"nhanh"*).
   - Miền Bắc thường sử dụng: *"rất ổn áp"*, *"chuẩn chỉ"*, *"xịn sò"*.
4. **Lỗi gõ phím và sự bất nhất trong bộ mã tiếng Việt:**
   Nhiều đánh giá gặp lỗi gõ dấu theo chuẩn Telex hoặc VNI (ví dụ gõ nhầm *"mays"* thành *"máy"* hoặc *"maý"*), bỏ dấu sai vị trí. Đặc biệt, sự tồn tại song song của hai chuẩn mã hóa Unicode: **Unicode tổ hợp (NFD)** và **Unicode dựng sẵn (NFC)** khiến cho hai từ nhìn bên ngoài hoàn toàn giống hệt nhau về mặt thị giác nhưng lại có mã byte nhị phân hoàn toàn khác biệt, gây phân mảnh từ điển nếu không được xử lý đồng nhất.
5. **Mật độ biểu tượng cảm xúc (Emoji / Emoticons) và dấu câu bất thường:**
   Nhiều bình luận lạm dụng hàng chục emoji liên tiếp (`👍👍👍❤️❤️❤️`), hoặc sử dụng các ký tự đặc biệt để ngụy trang số điện thoại nhằm lách luật kiểm duyệt của sàn: ví dụ *"O987.xxx.xxx"* (dùng chữ cái 'O' thay cho số '0'), *"z-a-l-o"*, *"l-i-ê-n h-ệ"*.

---

### 1.1.2. Ý nghĩa thực tiễn và những thách thức của bài toán

#### 1. Ý nghĩa thực tiễn đối với hệ sinh thái thương mại điện tử
Việc giải quyết thành công bài toán tự động nhận diện và phân loại đánh giá rác mang lại lợi ích đa chiều to lớn cho toàn bộ hệ sinh thái thương mại điện tử:

- **Bảo vệ quyền lợi người tiêu dùng:** Giúp người mua tiếp cận được những phản ánh trung thực về ưu, nhược điểm của sản phẩm, giảm thiểu rủi ro mua phải hàng giả, hàng nhái, hàng kém chất lượng do bị dẫn dụ bởi các đánh giá thổi phồng nhân tạo.
- **Tạo lập môi trường cạnh tranh lành mạnh cho nhà bán hàng (Merchants):** Bảo vệ các thương hiệu chân chính khỏi những chiến dịch bôi nhọ có chủ đích của đối thủ cạnh tranh; đồng thời cung cấp phản hồi thực tế để nhà sản xuất liên tục cải tiến chất lượng sản phẩm.
- **Nâng cao uy tín và hiệu quả vận hành của sàn thương mại điện tử:** Giữ vững niềm tin của khách hàng vào tính minh bạch của nền tảng; tự động hóa quy trình kiểm duyệt nội dung, giúp sàn TMĐT tiết kiệm hàng nghìn giờ công lao động của đội ngũ nhân sự kiểm duyệt thủ công (Human Moderation Team), nâng cao năng lực kiểm soát hàng triệu bình luận mới phát sinh mỗi ngày theo thời gian thực (Real-time Filtering).

#### 2. Những thách thức khoa học và kỹ thuật cốt lõi
Mặc dù bài toán lọc tin rác (Spam Filtering) đã được nghiên cứu rất nhiều trên các miền dữ liệu như Email (Email Spam) hay Tin nhắn viễn thông (SMS Spam), việc áp dụng vào miền đánh giá sản phẩm thương mại điện tử tiếng Việt gặp phải những rào cản kỹ thuật đặc thù:

1. **Sự khan hiếm của các bộ dữ liệu chuẩn gán nhãn cho tiếng Việt:**
   Phần lớn các nghiên cứu kinh điển trên thế giới được tiến hành trên các tập dữ liệu tiếng Anh quy mô lớn (như tập dữ liệu Yelp, Amazon của Liu & Ott). Tại Việt Nam, các bộ dữ liệu công khai chủ yếu phục vụ cho bài toán Phân tích cảm xúc (Sentiment Analysis) như bộ dữ liệu UIT-VSFC hay AIViVN, trong khi dữ liệu chuyên biệt về đánh giá rác (Spam/Ham Reviews) với đầy đủ các sắc thái ngôn ngữ thực tế còn rất hạn chế.
2. **Hiện tượng mất cân bằng lớp trầm trọng (Extreme Class Imbalance):**
   Trong môi trường thực tế, phần lớn các đánh giá của khách hàng là đánh giá hợp lệ (Ham Reviews chiếm từ 80% đến 95%), trong khi đánh giá rác (Spam Reviews) chỉ chiếm một tỷ lệ thiểu số (5% đến 20%). Nếu áp dụng các mô hình học máy thông thường mà không có chiến lược xử lý độ lệch lớp, mô hình có xu hướng thiên vị lớp đa số: mô hình chỉ cần dự đoán tất cả các mẫu đều là Ham thì độ chính xác tổng thể (Accuracy) vẫn có thể đạt tới 85 - 90%, nhưng lại hoàn toàn thất bại trong việc phát hiện các mẫu Spam (Recall lớp Spam tiệm cận 0%).
3. **Cạm bẫy rò rỉ dữ liệu (Data Leakage) từ các câu ngắn trùng lặp:**
   Đây là một thách thức kỹ thuật đặc biệt nghiêm trọng được nhóm tác giả phát hiện và tập trung giải quyết trong nghiên cứu này. Do giao diện của các ứng dụng mua sắm thường cung cấp các gợi ý đánh giá nhanh hoặc do thói quen của người dùng, hơn 50% số dòng dữ liệu thô trên sàn là các câu cực ngắn lặp đi lặp lại hàng trăm lần (ví dụ các câu *"Tốt"*, *"Ok"*, *"Hàng đẹp"*, *"Dùng ổn"*). Nếu người nghiên cứu thực hiện chia tập Train/Test ngẫu nhiên trước khi loại bỏ trùng lặp, các câu giống hệt nhau sẽ phân bổ vào cả tập huấn luyện và tập kiểm thử. Khi đó, mô hình học máy chỉ cần "học thuộc lòng" (Memorization) mà không cần năng lực tổng quát hóa (Generalization), dẫn đến kết quả đánh giá trên tập kiểm thử bị thổi phồng một cách giả tạo (Data Leakage), gây sai lệch toàn bộ kết luận khoa học.
4. **Tính đa nghĩa và ranh giới ngữ nghĩa mờ nhạt:**
   Nhiều đánh giá spam thế hệ mới không hề chứa số điện thoại hay liên kết web lộ liễu, mà sử dụng các câu khen chung chung nhằm mục đích cày điểm tích lũy hoặc seeding đánh giá ảo. Việc phân biệt một câu *"Tot tot"* là một khách hàng thực sự hài lòng nhưng lười viết, hay là một tài khoản bot đang spam lấy điểm thưởng, là một thách thức lớn đối với bất kỳ thuật toán phân loại văn bản nào nếu chỉ dựa thuần túy vào nội dung câu chữ.

---

## 1.2. Các hướng tiếp cận trong phân loại văn bản

Để giải quyết bài toán phân loại văn bản nói chung và bài toán nhận diện đánh giá rác nói riêng, lịch sử phát triển của ngành Trí tuệ Nhân tạo và Xử lý Ngôn ngữ Tự nhiên đã hình thành 3 hướng tiếp cận chủ đạo: Phương pháp dựa trên luật/từ điển, Phương pháp học máy truyền thống, và Phương pháp học sâu/mô hình ngôn ngữ lớn.

---

### 1.2.1. Phương pháp dựa trên luật và từ điển

Phương pháp dựa trên luật (Rule-based Approach) và từ điển (Dictionary/Lexicon-based) là thế hệ tiếp cận đầu tiên trong lĩnh vực xử lý ngôn ngữ tự nhiên. 

#### 1. Cơ chế hoạt động
Hệ thống dựa trên một tập hợp các quy tắc định trước (Heuristic Rules) do các chuyên gia ngôn ngữ hoặc kỹ sư thiết kế thủ công, kết hợp với các danh sách đen (Blacklist) và biểu thức chính quy (Regular Expressions - Regex):
- **Danh sách đen từ khóa:** Xây dựng danh sách các từ ngữ cấm xuất hiện trong bình luận hợp lệ, bao gồm: từ ngữ quảng cáo (*"zalo"*, *"inbox"*, *"liên hệ"*, *"vay tiền"*, *"lãi suất"*, *"tuyển dụng"*), từ ngữ khiêu dâm, cờ bạc.
- **Mẫu biểu thức chính quy:** Định nghĩa các mẫu hình để bắt các chuỗi số điện thoại (ví dụ: `(0|84)\d{9}`), địa chỉ URL (`https?://\S+`), hoặc các mẫu ký tự lặp kéo dài (`(.){4,}`).
- **Luật logic:** Nếu một bài đánh giá chứa từ nằm trong danh sách đen hoặc khớp với mẫu Regex, hệ thống sẽ tự động gán nhãn bài viết đó là Spam.

#### 2. Đánh giá ưu điểm và hạn chế
- **Ưu điểm:**
  - Tốc độ xử lý cực kỳ nhanh, độ trễ tiệm cận 0 ms vì chỉ sử dụng các phép so khớp chuỗi ký tự cơ bản.
  - Tính giải thích tuyệt đối (100% Explainable): Quản trị viên hệ thống có thể chỉ ra chính xác từ khóa hoặc quy tắc nào đã kích hoạt quyết định gắn nhãn spam.
  - Không đòi hỏi dữ liệu huấn luyện gán nhãn lớn và không tiêu tốn tài nguyên tính toán (không cần GPU hay bộ nhớ RAM lớn).
- **Hạn chế:**
  - **Cực kỳ cứng nhắc và thiếu khả năng thích ứng:** Người tạo spam có thể dễ dàng vượt qua các bộ lọc từ khóa bằng cách cố tình viết sai chính tả, chèn khoảng trắng hoặc ký tự đặc biệt (ví dụ: biến *"zalo"* thành *"z-a-l-o"*, *"z@lo"*, *"zl"*).
  - **Bùng nổ chi phí bảo trì:** Khi kẻ tạo spam liên tục thay đổi chiến thuật, các kỹ sư phải liên tục cập nhật danh sách quy tắc thủ công. Tập luật càng lớn thì nguy cơ xung đột luật (Rule Conflict) càng cao.
  - **Tỷ lệ bỏ sót (False Negative) và báo nhầm (False Positive) rất cao:** Không thể hiểu được ngữ cảnh; một câu khách hàng hỏi *"Sản phẩm này có kết nối được với Zalo không?"* sẽ bị hệ thống báo nhầm là spam do chứa từ khóa *"Zalo"*.

---

### 1.2.2. Phương pháp dựa trên Học máy (Machine Learning)

Sự ra đời của Học máy (Machine Learning) đã tạo ra một bước nhảy vọt, chuyển dịch từ cách tiếp cận lập trình quy tắc tĩnh sang cách tiếp cận học từ dữ liệu (Data-driven Approach).

#### 1. Cơ chế hoạt động
Quy trình phân loại văn bản bằng học máy truyền thống được cấu thành bởi hai giai đoạn độc lập:
1. **Trích chọn đặc trưng và Biểu diễn văn bản (Feature Engineering & Representation):**
   Máy tính không thể hiểu trực tiếp các ký tự chữ cái, do đó văn bản phải được chuyển đổi thành các vector số học trong không gian nhiều chiều. Các phương pháp biểu diễn kinh điển bao gồm:
   - *Mô hình Túi từ (Bag of Words - BoW):* Biểu diễn văn bản dựa trên tần số xuất hiện của từng từ đơn hoặc cụm từ (N-grams).
   - *Trọng số TF-IDF:* Cải tiến BoW bằng cách nhân thêm trọng số nghịch đảo tần suất văn bản, giúp hạ thấp tầm ảnh hưởng của các hư từ và làm nổi bật các từ đặc trưng riêng biệt.
   - *Nhúng từ phân tán (Word Embeddings - Word2Vec, FastText):* Biểu diễn từ trong không gian vector liên tục dày đặc (Dense Vector), nắm bắt được mối quan hệ tương đồng về mặt ngữ nghĩa và ngữ cảnh giữa các từ.
2. **Huấn luyện thuật toán phân loại (Supervised Classification Algorithms):**
   Các thuật toán học máy có giám sát tiếp nhận các vector đặc trưng và nhãn tương ứng trên tập huấn luyện để học ranh giới phân tách (Decision Boundary) tối ưu giữa hai lớp Spam và Ham. Các thuật toán tiêu biểu bao gồm:
   - *Naive Bayes (Đa thức, Phần bù, Gaussian):* Dựa trên xác suất có điều kiện và định lý Bayes.
   - *Máy vector hỗ trợ (Support Vector Machine - SVM):* Tìm siêu phẳng phân tách với khoảng cách lề lớn nhất.
   - *Hồi quy Logistic (Logistic Regression), Cây quyết định (Decision Trees), Rừng ngẫu nhiên (Random Forest).*

#### 2. Đánh giá ưu điểm và hạn chế
- **Ưu điểm:**
  - Khả năng khái quát hóa (Generalization) vượt trội: Mô hình học được các mẫu hình xác suất hoặc hình học ngầm định từ dữ liệu thay vì bám vào các từ khóa cứng nhắc.
  - Hiệu quả tính toán rất cao: Chi phí huấn luyện và thời gian suy luận (Inference Latency) cực thấp, có thể thực hiện hàng chục nghìn lượt dự đoán mỗi giây chỉ trên một nhân CPU thông thường.
  - Khả năng chống chịu nhiễu tốt khi kết hợp các kỹ thuật điều hòa (Regularization) như L1/L2 penalty trong SVM.
  - Hoạt động ổn định và đạt độ chính xác rất cao ngay cả trên các bộ dữ liệu kích thước vừa và nhỏ (vài nghìn đến vài chục nghìn mẫu).
- **Hạn chế:**
  - Vẫn phụ thuộc đáng kể vào chất lượng của bước kỹ nghệ đặc trưng (Feature Engineering) và các bước tiền xử lý văn bản thủ công.
  - Với BoW và TF-IDF, trật tự cú pháp và cấu trúc ngữ pháp của câu bị bỏ qua (giả định túi từ độc lập).
  - Vấn đề từ ngoài từ điển (Out-Of-Vocabulary - OOV) khi gặp các từ mới chưa từng xuất hiện trong tập huấn luyện.

---

### 1.2.3. Phương pháp dựa trên Học sâu (Deep Learning)

Từ những năm 2015 trở lại đây, sự bùng nổ của Học sâu (Deep Learning) và đặc biệt là kiến trúc Transformer (Vaswani et al., 2017) đã tái định hình toàn bộ lĩnh vực Xử lý Ngôn ngữ Tự nhiên.

#### 1. Cơ chế hoạt động
Học sâu cho phép mô hình tự động học các biểu diễn phân cấp (Hierarchical Representations) từ dữ liệu thô dạng chuỗi ký tự mà không cần trích xuất đặc trưng thủ công:
- **Mạng nơ-ron tích chập cho văn bản (TextCNN - Kim, 2014):** Sử dụng các bộ lọc tích chập (Convolutional Filters) có kích thước khác nhau trượt qua các vector từ nhúng để nắm bắt các cụm từ (Phraze-level features) then chốt.
- **Mạng nơ-ron hồi quy (RNN, LSTM, BiLSTM):** Xử lý văn bản như một chuỗi thời gian, ghi nhớ ngữ cảnh thông qua các trạng thái ẩn (Hidden States) và cổng nhớ (Gating Mechanisms), nắm bắt được sự phụ thuộc xa giữa các từ trong câu.
- **Mô hình ngôn ngữ tiền huấn luyện dựa trên Transformer (Pre-trained Language Models):**
  - Các mô hình dựa trên BERT (Devlin et al., 2018), RoBERTa (Liu et al., 2019) được tiền huấn luyện trên các kho ngữ liệu khổng lồ bằng các tác vụ như Masked Language Modeling (MLM).
  - Đối với tiếng Việt, các mô hình tiêu biểu gồm có **PhoBERT** (Nguyen & Nguyen, 2020) được huấn luyện trên 20GB văn bản tiếng Việt báo chí và Wikipedia, **ViDeBERTa**, hay **mBERT**.
  - Người nghiên cứu chỉ cần tinh chỉnh (Fine-tuning) thêm một tầng phân loại (Classification Head) trên tập dữ liệu đánh giá rác là có thể đạt được độ hiểu ngữ nghĩa sâu sắc.

#### 2. Đánh giá ưu điểm và hạn chế
- **Ưu điểm:**
  - Nắm bắt được ngữ cảnh hai chiều sâu sắc (Bidirectional Contextual Representation), phân biệt được cùng một từ nhưng mang nghĩa khác nhau tùy vào ngữ cảnh.
  - Tự động hóa hoàn toàn khâu trích chọn đặc trưng.
  - Đạt điểm số lý thuyết (State-of-the-Art - SOTA) cao nhất trong các bài toán phân loại văn bản phức tạp đòi hỏi suy luận logic ngữ nghĩa.
- **Hạn chế:**
  - **Chi phí tính toán và tài nguyên phần cứng khổng lồ:** Việc huấn luyện và tinh chỉnh đòi hỏi máy chủ trang bị card đồ họa chuyên dụng (GPU VRAM lớn), tiêu tốn năng lượng và ngân sách lớn.
  - **Độ trễ suy luận (Inference Latency) cao:** Thời gian mô hình Transformer xử lý một câu thường dao động từ vài mili-giây đến vài chục mili-giây, lớn hơn gấp hàng trăm đến hàng nghìn lần so với các mô hình học máy truyền thống như Linear SVM hay Naive Bayes (chỉ mất vài micro-giây).
  - **Tính chất "Hộp đen" (Black Box):** Rất khó giải thích tường minh cơ chế đưa ra quyết định bên trong hàng trăm triệu tham số của mạng nơ-ron.
  - **Hiện tượng Overfitting trên tập dữ liệu nhỏ:** Nếu kích thước tập dữ liệu huấn luyện chỉ có vài nghìn mẫu, các mô hình học sâu khổng lồ rất dễ bị quá khớp (Overfitting) vào các đặc trưng nhiễu.

#### 3. Bảng đối sánh tổng hợp giữa các hướng tiếp cận

*Bảng 1.2: So sánh tổng hợp các hướng tiếp cận phân loại văn bản.*

| Tiêu chí so sánh | Dựa trên luật & Từ điển | Học máy truyền thống (ML) | Học sâu & Transformer (DL) |
| :--- | :--- | :--- | :--- |
| **Bản chất trích xuất đặc trưng** | Thủ công (Regex, Blacklist) | Thủ công (BoW, TF-IDF, WE) | Tự động hóa qua các lớp ẩn |
| **Yêu cầu dữ liệu gán nhãn** | Không cần | Vừa phải (vài nghìn mẫu) | Lớn (hoặc cần Pre-trained models) |
| **Yêu cầu phần cứng** | CPU cơ bản | CPU cơ bản, RAM thấp | Yêu cầu GPU mạnh |
| **Thời gian huấn luyện** | 0 giây | Rất nhanh (vài giây đến vài phút) | Chậm (nhiều giờ đến nhiều ngày) |
| **Thời gian suy luận / mẫu** | $pprox 0.1 - 1$ µs | $pprox 0.4 - 60$ µs | $pprox 1,000 - 50,000$ µs |
| **Khả năng giải thích quyết định** | Tường minh 100% | Rất cao (trọng số đặc trưng) | Thấp (Hộp đen nơ-ron) |
| **Khả năng tổng quát hóa** | Kém, dễ bị lách luật | Tốt | Xuất sắc |
| **Khả năng triển khai thực tế** | Rất dễ, nhưng khó duy trì | Rất dễ, chi phí thấp, tối ưu cao | Khá phức tạp, chi phí máy chủ cao |

---

## 1.3. Các nghiên cứu liên quan

### 1. Các nghiên cứu quốc tế về phát hiện đánh giá giả mạo (Review Spam Detection)
Lĩnh vực phát hiện đánh giá rác và đánh giá giả mạo đã thu hút sự chú ý sâu rộng của cộng đồng khoa học quốc tế trong gần hai thập kỷ qua:

- **Công trình đặt nền móng của Jindal & Liu (2007, 2008):**
  Trong hai bài báo mang tính bước ngoặt *"Analyzing and Detecting Review Spam"* (IEEE ICDM 2007) và *"Opinion Spam and Analysis"* (ACM WSDM 2008), Nitin Jindal và Bing Liu đã lần đầu tiên hình thức hóa bài toán. Các tác giả thu thập 5.8 triệu đánh giá và 2.14 triệu người đánh giá từ Amazon. Do không có nhãn thực tế, các tác giả đã phát hiện một hiện tượng đặc thù: nhiều người đánh giá sao chép y hệt nội dung nhận xét cho các sản phẩm khác nhau (Duplicate Reviews). Coi các đánh giá trùng lặp này là spam, các tác giả đã huấn luyện mô hình Logistic Regression trên các đặc trưng kết hợp giữa văn bản (N-grams) và siêu dữ liệu (Reviewer features, Product features, Rating deviation), đạt được kết quả phân loại vượt trội so với các phương pháp ngẫu nhiên.
- **Nghiên cứu tạo tập dữ liệu chuẩn của Ott, Choi, Cardie & Hancock (ACL 2011):**
  Misha Ott và các cộng sự tại Đại học Cornell đã khắc phục hạn chế thiếu nhãn bằng cách thuê các cộng tác viên trên nền tảng Amazon Mechanical Turk viết 400 bài đánh giá giả mạo có chủ đích (Deceptive Reviews) cho 20 khách sạn tại Chicago, kết hợp với 400 bài đánh giá thật từ TripAdvisor. Nghiên cứu chỉ ra rằng con người gần như không thể phân biệt được đánh giá giả mạo (độ chính xác của con người chỉ đạt xấp xỉ 57% — tương đương đoán mò ngẫu nhiên). Ngược lại, mô hình học máy **Support Vector Machine (SVM)** kết hợp với đặc trưng N-grams và phân tích tâm lý ngôn ngữ (LIWC - Linguistic Inquiry and Word Count) đạt độ chính xác lên tới **89.8%**, chứng minh sức mạnh vượt trội của học máy trong việc phát hiện các tín hiệu ngôn ngữ ngầm ẩn của sự dối trá.
- **Các nghiên cứu tổng quan của Crawford et al. (2015) và Heydari et al. (2015):**
  Các bài báo khảo sát chuyên sâu đã hệ thống hóa các phương pháp tiếp cận theo 3 trục chính: (1) Phương pháp dựa trên nội dung văn bản (Text-based), (2) Phương pháp dựa trên hành vi người dùng (Behavior-based), và (3) Phương pháp dựa trên đồ thị quan hệ (Graph-based). Các tác giả kết luận rằng trong bối cảnh các sàn thương mại điện tử ẩn danh tính người dùng hoặc không cung cấp API truy xuất lịch sử, các phương pháp dựa trên phân tích nội dung văn bản (Text-based) vẫn là phòng tuyến then chốt, mang tính khả thi cao nhất để tích hợp trực tiếp vào hệ thống kiểm duyệt.
- **Nghiên cứu của Sun et al. (2019):**
  Nghiên cứu ứng dụng các kỹ thuật biểu diễn vector từ Word2Vec kết hợp với các thuật toán học máy phân loại văn bản, chỉ ra rằng việc kết hợp thông tin ngữ nghĩa dày đặc của embedding giúp cải thiện đáng kể độ nhạy (Recall) trong việc phát hiện các biến thể spam so với mô hình túi từ truyền thống.

### 2. Các nghiên cứu liên quan đến xử lý ngôn ngữ tự nhiên tiếng Việt
Tại Việt Nam, các bài toán phân loại văn bản và phân tích phản hồi người dùng cũng đã đạt được nhiều tiến bộ đáng kể:

- **Bài toán phân tích cảm xúc đánh giá (Sentiment Analysis):**
  Nhóm nghiên cứu của Nguyễn Hải Triều và cộng sự tại Đại học Công nghệ Thông tin - ĐHQG TP.HCM (UIT) đã công bố bộ dữ liệu chuẩn **UIT-VSFC** (Vietnamese Students' Feedback Corpus, 2018) và bộ dữ liệu đánh giá sản phẩm thương mại điện tử **UIT-ViSFD** (2021). Các nghiên cứu này đã so sánh kỹ lưỡng hiệu năng giữa các mô hình học máy truyền thống (Naive Bayes, SVM, Maximum Entropy) với các mạng nơ-ron sâu (LSTM, CNN), khẳng định rằng SVM với đặc trưng TF-IDF vẫn là một baseline cực kỳ mạnh mẽ, thường đạt hiệu năng cạnh tranh sát nút với các mô hình học sâu nhưng có chi phí tài nguyên thấp hơn hàng trăm lần.
- **Bài toán lọc tin rác tin nhắn (Vietnamese SMS Spam Filtering):**
  Nhiều nghiên cứu trong nước (như nghiên cứu của Phạm Quang Nhật Minh và cộng sự) đã khảo sát bài toán lọc tin rác SMS tiếng Việt. Tuy nhiên, dữ liệu tin nhắn SMS có những đặc trưng khác biệt so với đánh giá TMĐT: SMS thường mang tính chất chào mời trực tiếp, ít bị pha tạp bởi các bình luận ngắn lấy xu thưởng hay các đánh giá sản phẩm điện máy chuyên sâu.

*Bảng 1.3: Tổng hợp các công trình nghiên cứu tiêu biểu liên quan đến phát hiện đánh giá giả mạo và phân loại văn bản tiếng Việt.*

| Tác giả & Năm | Tập dữ liệu thực nghiệm | Phương pháp biểu diễn văn bản | Thuật toán học máy / Mô hình | Kết quả chính & Đóng góp |
| :--- | :--- | :--- | :--- | :--- |
| **Jindal & Liu (2007, 2008)** | 5.8 triệu đánh giá Amazon (Tiếng Anh) | N-grams kết hợp Siêu dữ liệu người dùng | Logistic Regression, Naive Bayes | Đặt nền móng bài toán Opinion Spam; chứng minh các câu trùng lặp là tín hiệu spam mạnh. |
| **Ott et al. (2011)** | 800 đánh giá khách sạn TripAdvisor (Turk) | Unigram, Bigram, Đặc trưng LIWC tâm lý | Support Vector Machine (Linear SVM) | Đạt độ chính xác 89.8%; chứng minh con người chỉ đoán đúng 57% trước spam ngụy trang. |
| **Crawford et al. (2015)** | Khảo sát tổng hợp nhiều bộ dữ liệu TMĐT | BoW, POS tags, Sentiment Lexicon | SVM, Random Forest, C4.5 | Hệ thống hóa các hướng tiếp cận phát hiện spam dựa trên văn bản và hành vi người dùng. |
| **Sun et al. (2019)** | Đánh giá nhà hàng Yelp & Dianping | Word2Vec Embeddings + Behavioral Features | CNN, BiLSTM, Random Forest | F1 đạt 86.4%; chứng minh nhúng từ dày đặc giúp nhận diện ngữ nghĩa tương đồng của spam. |
| **Nguyễn Hải Triều et al. (2018)** | 16,000 phản hồi sinh viên UIT-VSFC | TF-IDF, N-grams tiếng Việt | MaxEnt, Naive Bayes, SVM, BiLSTM | Bộ dữ liệu chuẩn tiếng Việt; khẳng định SVM + TF-IDF là baseline cực mạnh (Acc ~89-91%). |
| **Đề tài hiện tại (Nhóm N2 - PTIT, 2026)** | 4,820 đánh giá điện máy TMĐT (khử 55.7% trùng) | BoW (1-2 gram), TF-IDF (L2), Word2Vec Skip-gram | 3 biến thể Naive Bayes, Linear & RBF SVM (Pipeline) | RBF SVM + WE đạt F1 88.37%, Acc 95.85%, PR-AUC 0.9265; Linear SVM + BoW đạt Recall 94.67%. |

---

### 3. Phân tích khoảng trống nghiên cứu (Research Gap)
Qua việc tổng hợp và đánh giá các công trình trong và ngoài nước, nhóm tác giả nhận thấy những khoảng trống nghiên cứu rõ rệt:
1. **Thiếu vắng nghiên cứu so sánh thực nghiệm toàn diện trên dữ liệu đánh giá rác tiếng Việt:** Phần lớn các nghiên cứu trong nước tập trung vào phân loại cảm xúc (Tích cực / Tiêu cực / Trung tính), trong khi bài toán phát hiện đánh giá rác (Spam / Ham) — vốn có độ lệch lớp cao và các đặc trưng ngôn ngữ gian lận đặc thù — chưa được khảo sát một cách có hệ thống.
2. **Bỏ qua rủi ro rò rỉ dữ liệu (Data Leakage) trong tiền xử lý:** Hầu hết các bài viết thực hành hoặc đề tài trước đây đều áp dụng hàm chia dữ liệu ngẫu nhiên một cách máy móc, vô tình làm lọt các câu trùng lặp vào cả hai tập train và test, dẫn đến các kết luận hiệu năng bị sai lệch nghiêm trọng.
3. **Chưa có công trình đối sánh công bằng (Fair Benchmark) giữa 3 không gian biểu diễn (BoW, TF-IDF, Word2Vec) trên cùng một điều kiện kiểm thử phân tầng nghiêm ngặt.**

Nghiên cứu trong bài tập lớn này được thiết kế để khỏa lấp trực tiếp các khoảng trống học thuật và thực tiễn nêu trên.

---

## 1.4. Mục tiêu và phạm vi của đề tài

### 1.4.1. Mục tiêu nghiên cứu
Đề tài hướng tới việc xây dựng một hệ thống học máy hoàn chỉnh, có phương pháp luận khoa học chặt chẽ và đạt hiệu năng tối ưu trong bài toán tự động nhận diện và phân loại đánh giá rác tiếng Việt trên các sàn thương mại điện tử.

Cụ thể, đề tài đặt ra các mục tiêu kỹ thuật chi tiết như sau:
1. **Xây dựng Pipeline tiền xử lý văn bản tiếng Việt chuyên sâu và chống rò rỉ dữ liệu:**
   - Xây dựng quy trình làm sạch chuẩn mực: chuẩn hóa Unicode NFC, chuyển đổi chữ thường, khử ký tự lặp cảm xúc, trừu tượng hóa các thực thể nhạy cảm (URL, Email, SĐT, Số tiền) thành các token khái quát (`urltoken`, `phonetoken`, `numtoken`).
   - Xây dựng từ điển chuẩn hóa Teencode / viết tắt đặc thù cho thương mại điện tử Việt Nam.
   - Hiện thực hóa thuật toán xử lý mâu thuẫn nhãn bằng biểu quyết đa số (Majority Voting) và khử trùng lặp triệt để trước khi phân chia dữ liệu, bảo đảm tính độc lập tuyệt đối giữa tập huấn luyện và kiểm thử.
2. **Khảo sát và hiện thực hóa 3 phương pháp biểu diễn văn bản:**
   - Phương pháp Túi từ (Bag of Words - BoW) kết hợp n-gram range (1, 2).
   - Phương pháp Trọng số TF-IDF kết hợp kỹ thuật nén logarithm (sublinear TF scaling) và chuẩn hóa vector L2 norm.
   - Phương pháp Nhúng từ liên tục (Word2Vec) với kiến trúc Skip-gram và kỹ thuật tổng hợp vector câu (Document Vector Pooling).
3. **Cài đặt, tối ưu hóa và thực nghiệm 6 cấu hình mô hình học máy:**
   - Khảo sát 3 biến thể xác suất Naive Bayes: Multinomial Naive Bayes (trên BoW), Complement Naive Bayes (trên TF-IDF), và Gaussian Naive Bayes (trên Word2Vec).
   - Khảo sát 2 cấu hình Máy vector hỗ trợ (SVM): Linear SVM (trên BoW và TF-IDF) và Kernel RBF SVM kết hợp bộ chuẩn hóa StandardScaler và kỹ thuật cân bằng trọng số lớp (`class_weight='balanced'`) trên Word2Vec.
   - Tối ưu hóa siêu tham số bằng kỹ thuật 5-Fold Stratified Cross-Validation chỉ thực hiện trên tập huấn luyện.
4. **Đánh giá toàn diện và phân tích chuyên sâu:**
   - Đo lường hiệu năng thông qua hệ thống 7 chỉ số khoa học: Accuracy, Precision (Spam), Recall (Spam), F1-Score (Spam), Macro F1, ROC-AUC, và PR-AUC.
   - Phân tích định tính các trường hợp phân loại sai (False Positives, False Negatives) để làm sáng tỏ cơ chế hoạt động của từng mô hình và rút ra các khuyến nghị thực tiễn cho bài toán triển khai thực tế.

### 1.4.2. Phạm vi nghiên cứu
Để bảo đảm tính tập trung và khả thi của đề tài trong khuôn khổ môn học Xử lý Ngôn ngữ Tự nhiên, phạm vi nghiên cứu được xác định cụ thể như sau:

- **Về miền dữ liệu (Domain):** Đề tài tập trung nghiên cứu trên tập dữ liệu đánh giá sản phẩm điện tử tiêu dùng và thiết bị điện máy gia dụng tại Việt Nam (bao gồm 10 danh mục sản phẩm chính: *Tủ lạnh, Nồi cơm điện, Điều hòa, Máy giặt, Tivi, Máy lọc nước, Máy lọc không khí, Máy sấy quần áo, Camera giám sát, và Khác*) với 114 dòng sản phẩm riêng biệt và đầy đủ các thang đo từ 1 sao đến 5 sao.
- **Về không gian nhãn:** Bài toán được định dạng là bài toán **Phân loại nhị phân (Binary Classification)** với hai lớp: Nhãn 1 là **Spam** (đánh giá rác, quảng cáo, chèo kéo, lừa đảo, vô nghĩa) và Nhãn 0 là **Ham** (đánh giá hợp lệ, trải nghiệm thật của khách hàng).
- **Về mặt công nghệ và thuật toán:** Đề tài tập trung nghiên cứu sâu vào các phương pháp học máy truyền thống và biểu diễn vector từ điển/nhúng từ nền tảng (Naive Bayes và Support Vector Machines). Đề tài không đi sâu vào việc huấn luyện các mô hình học sâu khổng lồ (Large Language Models) nhằm duy trì mục tiêu xây dựng một giải pháp có tốc độ suy luận siêu nhanh (Micro-seconds), tiết kiệm tài nguyên, và có khả năng đóng gói triển khai microservice nhẹ nhàng trên hạ tầng CPU thông thường.


ewpage

# CHƯƠNG 2: PHÂN LOẠI ĐÁNH GIÁ DỰA TRÊN HỌC MÁY VÀ BIỂU DIỄN VĂN BẢN

Để chuyển hóa các bài đánh giá thương mại điện tử thô sơ, phi chuẩn thành các dự đoán chính xác và tin cậy, hệ thống cần một quy trình kỹ thuật gồm ba trụ cột nền tảng: **Tiền xử lý dữ liệu chuyên sâu**, **Trích chọn đặc trưng và biểu diễn văn bản**, và **Huấn luyện mô hình học máy tối ưu**. Chương 2 sẽ trình bày chi tiết cơ sở lý thuyết, các công thức toán học, thuật toán và giải pháp thiết kế hệ thống được nhóm tác giả áp dụng trong đề tài.

---

## 2.1. Tiền xử lý dữ liệu văn bản

Tiền xử lý (Preprocessing) là bước đầu tiên và mang tính sống còn trong bất kỳ hệ thống Xử lý Ngôn ngữ Tự nhiên nào, đặc biệt là đối với văn bản đánh giá mạng xã hội tiếng Việt — nơi các hiện tượng gõ sai, tiếng lóng, teencode và biểu cảm cực đoan xuất hiện với tần suất dày đặc.

---

[CHÈN HÌNH 2.1 TẠI ĐÂY: Quy trình chuẩn hóa và làm sạch văn bản tiếng Việt cho bài toán phân loại đánh giá]
*(Placeholder: /assets/images/hinh2_1_quy_trinh_tien_xu_ly.png - Kích thước khuyến nghị: 15cm x 6cm, căn giữa)*

---

### 2.1.1. Làm sạch văn bản, xóa ký tự đặc biệt và chuẩn hóa chữ thường

Quy trình làm sạch một bài đánh giá được tiến hành qua 6 công đoạn liên tiếp theo đúng thứ tự thiết kế:

#### 1. Đồng nhất bộ mã Unicode tiếng Việt (Unicode Normalization)
Trong hệ thống mã hóa ký tự Unicode, tiếng Việt có hai hình thức biểu diễn dấu thanh và dấu phụ phổ biến:
- **Unicode tổ hợp (NFD - Normalization Form D):** Ký tự có dấu được phân tách thành ký tự gốc (Base Character) kết hợp với các điểm mã dấu thanh độc lập. Ví dụ, chữ `"ệ"` được biểu diễn bởi 3 điểm mã nhị phân: `U+0065` (chữ e) + `U+0302` (dấu mũ `^`) + `U+0323` (dấu nặng `.`).
- **Unicode dựng sẵn (NFC - Normalization Form C):** Toàn bộ ký tự có dấu được gộp thành một điểm mã duy nhất. Chữ `"ệ"` chỉ mang một mã `U+1EC7`.

Nếu không đồng nhất chuẩn mã hóa, cùng một từ *"tốt"* viết bởi bộ gõ Telex (NFC) và bộ gõ Unikey kiểu cũ (NFD) sẽ bị mô hình học máy coi là hai từ hoàn toàn khác biệt nhau, làm phân mảnh không gian từ vựng và giảm nghiêm trọng độ dày đặc trưng. Trong nghiên cứu này, toàn bộ văn bản được quy chuẩn nghiêm ngặt về chuẩn dựng sẵn thông qua thư viện chuẩn của Python:
```python
text = unicodedata.normalize("NFC", text)
```

#### 2. Chuẩn hóa chữ thường (Case Folding)
Văn bản được chuyển đổi toàn bộ về dạng chữ thường thông qua phương thức `.lower()`. Việc này giúp hợp nhất các biến thể viết hoa do viết đầu câu, viết hoa toàn bộ để nhấn mạnh (ví dụ: *"TỐT"*, *"Tốt"*, *"tốt"* đều được đưa về token duy nhất là *"tốt"*), từ đó làm giảm số chiều dư thừa của không gian từ điển.

#### 3. Kỹ thuật trừu tượng hóa thực thể bằng Token đặc biệt (Abstract Entity Tokenization)
Một trong những phát kiến kỹ thuật then chốt của đề tài nhằm tăng cường khả năng tổng quát hóa của mô hình học máy là **không xóa bỏ** các chuỗi số điện thoại, liên kết web hay số tiền, mà **trừu tượng hóa chúng thành các token khái quát**:
- **Địa chỉ liên kết web (URL):**
  Spam chèo kéo thường chứa các đường dẫn web đa dạng: `http://...`, `www....`, hay các tên miền rút gọn `.com`, `.vn`, `.top`, `.vip`, `.xyz`. Sử dụng biểu thức chính quy (Regex):
  ```python
  URL_RE = re.compile(r"(https?://\S+|www\.\S+|\b\S+\.(?:com|vn|net|vip|xyz|info|org|shop|top|online)\S*)", flags=re.IGNORECASE)
  text = URL_RE.sub(" urltoken ", text)
  ```
- **Số điện thoại (Phone Numbers):**
  Spam quảng cáo dịch vụ thường chèn số điện thoại liên hệ cá nhân. Nhận diện các đầu số di động phổ biến tại Việt Nam (+84, 09, 08, 03, 07, 05) kèm các dấu phân cách ngụy trang (dấu chấm, dấu gạch ngang, khoảng trắng):
  ```python
  PHONE_RE = re.compile(r"(?:\+?84|0)(?:[\s.\-]?\d){8,10}")
  text = PHONE_RE.sub(" phonetoken ", text)
  ```
- **Địa chỉ thư điện tử (Email):**
  ```python
  EMAIL_RE = re.compile(r"\b[\w.+-]+@[\w-]+\.[\w.-]+\b")
  text = EMAIL_RE.sub(" emailtoken ", text)
  ```
- **Số lượng và đơn vị tiền tệ (Numbers & Currencies):**
  Các biểu thức như `500k`, `5tr`, `30đ`, `100vnd`, `100000` được thay thế bằng token khái quát:
  ```python
  NUMBER_RE = re.compile(r"\d+(?:[.,]\d+)*(?:k|tr|đ|d|vnd|vnđ)?\b")
  text = NUMBER_RE.sub(" numtoken ", text)
  ```

*Ý nghĩa khoa học của phương pháp này:* Nếu giữ nguyên chuỗi gốc, mỗi số điện thoại cá nhân (ví dụ: `0912345678`) sẽ trở thành một đặc trưng riêng biệt chỉ xuất hiện duy nhất 1 lần trong tập huấn luyện, khiến mô hình học máy bị quá khớp (Overfitting) và hoàn toàn bất lực khi gặp một số điện thoại mới trong tập kiểm thử. Bằng cách quy đổi về `phonetoken`, mô hình học được mối tương quan thống kê bản chất: *"Bất kỳ bình luận nào chứa tín hiệu phonetoken đều có xác suất cực cao là Spam"*. Thực tế thực nghiệm tại Chương 3 đã chứng minh rằng `phonetoken` có tần suất xuất hiện trong lớp Spam là 139 lần, trong khi ở lớp Ham là 0 lần!

#### 4. Rút gọn ký tự lặp kéo dài (Character Repetition Normalization)
Người dùng trên mạng thường có thói quen gõ kéo dài ký tự để biểu lộ cảm xúc mạnh hoặc lách bộ lọc: *"tốtttttt"*, *"ngonnn"*, *"đẹpppp"*. Sử dụng biểu thức chính quy tìm các ký tự từ ngữ lặp lại từ 3 lần trở lên và rút gọn về 1 ký tự:
```python
REPEAT_CHAR_RE = re.compile(r"(\w)\1{2,}")
text = REPEAT_CHAR_RE.sub(r"\1", text)
```
Nhờ đó, *"tốtttt"* được đưa về *"tốt"*, *"ngonnn"* được đưa về *"ngon"*, giúp các từ này khớp hoàn hảo với từ điển huấn luyện.

#### 5. Bảo toàn dấu câu như các Token độc lập (Punctuation Tokenization)
Trong các tác vụ phân loại văn bản tin tức truyền thống, dấu câu thường bị loại bỏ hoàn toàn. Tuy nhiên, đối với bài toán nhận diện đánh giá rác trên thương mại điện tử, **dấu câu mang thông tin ngữ nghĩa và hành vi cực kỳ quan trọng**:
- Các bình luận spam vô nghĩa để lấy xu thường chỉ chứa duy nhất một dấu chấm `.` hoặc một chuỗi dấu chấm `...`.
- Các bình luận lừa đảo hoặc bức xúc tiêu cực thường lạm dụng dấu chấm than `!` hoặc dấu hỏi `?`.

Do đó, hệ thống không xóa dấu câu mà thực hiện tách dấu câu thành các token độc lập bằng cách chèn khoảng trắng xung quanh:
```python
PUNCT_RE = re.compile(r"([^\w\s])")
text = PUNCT_RE.sub(r" \1 ", text)
```

#### 6. Chuẩn hóa Teencode và Từ viết tắt tiếng Việt
Nhóm tác giả đã dày công xây dựng một từ điển ánh xạ (Teencode Mapping Dictionary) gồm hơn 30 quy tắc chuẩn hóa các từ viết tắt và biến thể tiếng lóng thông dụng nhất trong bình luận sản phẩm tại Việt Nam. Toàn bộ các từ này được tra cứu và thay thế bằng dạng từ ngữ chuẩn mực, được mô tả chi tiết tại **Bảng 2.1**:

*Bảng 2.1: Bảng ánh xạ chuẩn hóa viết tắt và teencode tiếng Việt trong thương mại điện tử.*

| Nhóm từ ngữ | Biến thể Teencode / Viết tắt đầu vào | Dạng từ ngữ chuẩn hóa đầu ra | Giải thích ngữ nghĩa |
| :--- | :--- | :--- | :--- |
| **Phủ định** | `ko`, `k`, `kh`, `khong`, `hok`, `hông`, `kg`, `khg` | `không` | Từ phủ định cốt lõi |
| **Khả năng / Bị động** | `dc`, `đc`, `duoc`, `dk`, `đk` | `được` | Trợ từ chỉ khả năng hoặc bị động |
| **Thực thể thương mại** | `sp` | `sản phẩm` | Đối tượng được đánh giá |
| **Đơn vị bán lẻ** | `dmx` | `điện máy xanh` | Tên hệ thống siêu thị điện máy |
| **Chăm sóc khách hàng** | `nv` | `nhân viên` | Đối tượng phục vụ |
| **Dịch vụ hậu mãi** | `bh` | `bảo hành` | Chính sách bảo hành sản phẩm |
| **Chấp thuận / Khen** | `oke`, `okie`, `okela`, `oki`, `okay`, `okê` | `ok` | Đồng thuận, chất lượng chấp nhận được |
| **Đại từ xưng hô** | `mk`, `mik` | `mình` | Ngôi thứ nhất số ít |
| **Đại từ tập thể** | `mn` | `mọi người` | Chỉ cộng đồng người mua hàng |
| **Nghi vấn** | `j` | `gì` | Đại từ nghi vấn |
| **Liên từ** | `vs` | `với` | Từ nối |
| **Thời gian / Hoàn thành**| `r`, `rùi` | `rồi` | Trạng thái đã hoàn tất |
| **Tri ân / Cảm ơn** | `tks`, `thanks`, `thank` | `cảm ơn` | Lời cảm ơn |

Sau khi duyệt qua từ điển, văn bản được loại bỏ các khoảng trắng thừa (`\s+`) và cắt tỉa hai đầu (`.strip()`). Nếu văn bản sau làm sạch bị rỗng hoàn toàn, hệ thống sẽ gán cho nó giá trị token đặc biệt `"emptytoken"`.

---

### 2.1.2. Tách từ (Tokenization) và loại bỏ từ dừng (Stopwords)

#### 1. Bài toán tách từ (Tokenization) trong tiếng Việt
Khác với các ngôn ngữ phương Tây như tiếng Anh hay tiếng Pháp vốn sử dụng khoảng trắng làm ranh giới phân tách từ rõ ràng, tiếng Việt là một ngôn ngữ đơn lập (Isolating Language). Đơn vị phát âm và hình thái cơ bản của tiếng Việt là **tiếng (Âm tiết - Syllable)**, và một **từ (Word)** có thể được cấu thành từ một âm tiết (từ đơn: *"máy"*, *"tốt"*) hoặc nhiều âm tiết (từ ghép: *"tủ lạnh"*, *"nồi cơm điện"*, *"máy giặt"*).

Trong đề tài này, nhóm tác giả đã cân nhắc hai giải pháp kỹ thuật:
- *Giải pháp 1: Sử dụng các bộ tách từ tiếng Việt chuyên dụng (như VnCoreNLP, pyvi).* Các công cụ này dựa trên từ điển ghép từ và mô hình học máy (CRF/BiLSTM) để nối các âm tiết thành từ ghép (ví dụ: *"tủ_lạnh"*, *"nồi_cơm_điện"*). Tuy nhiên, trên dữ liệu bình luận thương mại điện tử chứa đầy từ lóng, teencode và viết sai chính tả, các bộ tách từ truyền thống thường gặp hiện tượng phân đoạn sai nghiêm trọng (Segmentation Error) và có tốc độ tính toán khá chậm.
- *Giải pháp 2 (Giải pháp được lựa chọn): Tách từ mức âm tiết theo khoảng trắng kết hợp N-gram Range (1, 2).*
  Nhóm tác giả quyết định tách token đơn giản bằng khoảng trắng (`tokenizer=str.split`) sau khi đã tiền xử lý, đồng thời thiết lập tham số `ngram_range=(1, 2)` trong các bộ trích chọn đặc trưng BoW và TF-IDF. Cơ chế này sinh ra cả đặc trưng đơn (Unigram) và đặc trưng cụm hai từ liền kề (Bigram). Ví dụ, cụm *"máy chạy êm"* sẽ sinh ra các đặc trưng: `{"máy", "chạy", "êm", "máy chạy", "chạy êm"}`. Phương pháp này vừa bắt trọn vẹn các từ ghép thông dụng, vừa giữ được cấu trúc ngữ cảnh cục bộ mà không bị phụ thuộc vào từ điển tách từ tĩnh, đồng thời đạt tốc độ xử lý nhanh gấp hàng chục lần.

#### 2. Vấn đề loại bỏ từ dừng (Stopwords)
Từ dừng (Stopwords) là các từ ngữ xuất hiện với tần suất rất cao trong văn bản nhưng mang rất ít giá trị thông tin phân biệt (ví dụ: *"và"*, *"thì"*, *"là"*, *"mà"*). Trong nhiều tác vụ phân loại văn bản tin tức, việc sử dụng danh sách từ dừng định sẵn (Static Stopword List) là bắt buộc. Tuy nhiên, đối với bài toán phân loại đánh giá sản phẩm, **nhóm tác giả quyết định KHÔNG sử dụng danh sách từ dừng thủ công** vì những lý do khoa học sau:
1. Các danh sách từ dừng tiếng Việt hiện có (như danh sách từ dừng của Báo điện tử tiếng Việt) thường chứa các từ như *"không"*, *"rất"*, *"quá"*, *"chưa"*, *"được"*. Trong bài toán phân loại đánh giá sản phẩm, các từ này mang trọng số cảm xúc cực lớn: *"không tốt"* hoàn toàn trái ngược với *"tốt"*. Nếu máy móc xóa bỏ từ *"không"*, hai câu đối lập trên sẽ trở nên giống hệt nhau!
2. Hệ thống đã tích hợp hai cơ chế lọc tự nhiên, khoa học hơn rất nhiều:
   - Cơ chế ngưỡng tần suất văn bản cực tiểu (`min_df=2`): Tự động loại bỏ các từ hiếm chỉ xuất hiện 1 lần (lỗi gõ phím ngẫu nhiên, từ rác).
   - Cơ chế trọng số nghịch đảo tần suất văn bản (IDF trong TF-IDF): Tự động hạ thấp trọng số của các từ ngữ xuất hiện phổ biến ở hầu hết mọi câu (như *"là"*, *"thì"*, dấu phẩy, dấu chấm) tiệm cận về 0 mà không cần phải can thiệp thủ công bằng tay.

#### 3. Chiến lược khử trùng lặp và ngăn ngừa rò rỉ dữ liệu (Anti-Data Leakage Strategy)
Một đóng góp mang tính phương pháp luận cốt lõi của đề tài là việc phát hiện và xử lý triệt để hiện tượng câu ngắn trùng lặp:

- **Thực trạng dữ liệu:** Trong tập dữ liệu thô ban đầu, có tới **55.7% số dòng là các câu ngắn lặp lại y hệt nhau**. Người dùng khi mua hàng tại Điện Máy Xanh hoặc Shopee thường bấm vào các nút gợi ý đánh giá có sẵn: câu *"Tốt"* xuất hiện lặp lại gần 450 lần, câu *"Ok"* xuất hiện khoảng 340 lần, các câu *"Hàng đẹp"*, *"Dùng tốt"* lặp lại hàng trăm lần.
- **Rủi ro rò rỉ dữ liệu (Data Leakage Risk):** Nếu áp dụng hàm chia ngẫu nhiên `train_test_split` trực tiếp trên dữ liệu thô, các câu *"Tốt"* hay *"Ok"* sẽ phân bổ đều đặn ở cả tập Train và tập Test. Khi đó, mô hình học máy chỉ cần "ghi nhớ" (Memorize) rằng *"Tốt"* có nhãn là gì trên tập Train là có thể dự đoán chính xác 100% trên tập Test. Điểm số Accuracy hay F1-Score trên tập Test khi đó sẽ cao một cách giả tạo (Data Leakage), nhưng khi mang mô hình ra môi trường thực tế gặp các câu mới lạ, mô hình sẽ hoàn toàn thất bại.
- **Giải thuật xử lý:**
  1. *Làm sạch toàn bộ văn bản về cột `clean_text`.*
  2. *Giải quyết câu có nhãn mâu thuẫn:* Có những câu có nội dung giống hệt nhau nhưng người gán nhãn thủ công ban đầu lại gán một dòng là Spam (nhãn 1), một dòng là Ham (nhãn 0). Hệ thống gom nhóm theo `clean_text` và áp dụng luật **Biểu quyết đa số (Majority Voting)** để chuẩn hóa về nhãn xuất hiện nhiều nhất:
     $$\hat{y}_{\text{majority}} = \arg\max_{c \in \{0, 1\}} \sum_{i: x_i = x} \mathbb{I}(y_i = c)$$
  3. *Khử trùng lặp triệt để:* Áp dụng lệnh `drop_duplicates(subset=['clean_text'])` để chỉ giữ lại duy nhất 1 bản ghi đại diện cho mỗi câu độc nhất.
  4. *Phân chia phân tầng (Stratified Splitting):* Chỉ sau khi đã khử sạch câu trùng lặp, hệ thống mới tiến hành chia Train/Test theo tỷ lệ 80/20 có phân tầng theo nhãn (`stratify=df['label']`) với seed cố định (`random_state=42`). Việc chia này được thực hiện một lần duy nhất tại bước tiền xử lý, đảm bảo cả 3 phương pháp trích chọn đặc trưng (BoW, TF-IDF, Word2Vec) đều sử dụng chung một tập dữ liệu phân chia, tạo nền tảng cho việc so sánh công bằng tuyệt đối.

---

## 2.2. Trích chọn đặc trưng và biểu diễn văn bản

Máy học và các thuật toán phân loại không thể tiếp nhận trực tiếp chuỗi ký tự tự nhiên mà đòi hỏi dữ liệu đầu vào phải là các vector số học trong không gian toán học $D$ chiều: $x \in \mathbb{R}^D$. Để khảo sát toàn diện bài toán, đề tài đã thiết kế và hiện thực hóa 3 không gian biểu diễn văn bản từ cổ điển đến hiện đại:

---

### 2.2.1. Mô hình Túi từ - Bag of Words (BoW)

Mô hình Túi từ (Bag of Words - Harris, 1954) là phương pháp biểu diễn văn bản nền tảng và trực quan nhất trong NLP.

#### 1. Nguyên lý toán học
Giả sử tập ngữ liệu huấn luyện gồm $N$ văn bản: $\mathcal{D} = \{d_1, d_2, \dots, d_N\}$. Qua quá trình phân tích từ vựng, hệ thống xây dựng một tập từ điển chung $\mathcal{V} = \{w_1, w_2, \dots, w_{|\mathcal{V}|}\}$ gồm $|\mathcal{V}|$ đặc trưng độc nhất. 

Mỗi bài đánh giá $d_i$ được biểu diễn thành một vector đặc trưng $x_i = (c_{i1}, c_{i2}, \dots, c_{i|\mathcal{V}|})^\top \in \mathbb{R}^{|\mathcal{V}|}$, trong đó $c_{ij}$ là tần số xuất hiện (số lần đếm) của đặc trưng $w_j$ trong bài đánh giá $d_i$:
$$c_{ij} = \text{count}(w_j, d_i)$$

---

[CHÈN HÌNH 2.2 TẠI ĐÂY: Minh họa trực quan không gian vector thưa trong mô hình Bag-of-Words (BoW)]
*(Placeholder: /assets/images/hinh2_2_khong_gian_vector_bow.png - Kích thước khuyến nghị: 14cm x 7cm, căn giữa)*

---

#### 2. Cài đặt và cấu hình tham số
Trong đề tài, nhóm sử dụng lớp `CountVectorizer` của thư viện Scikit-Learn với các cấu hình tối ưu:
- `tokenizer=str.split`: Sử dụng các token đã được làm sạch và tách cách nhau bởi dấu cách.
- `token_pattern=None`: Vô hiệu hóa bộ lọc regex mặc định của scikit-learn (bộ lọc mặc định tự ý bỏ dấu câu và các từ 1 ký tự).
- `lowercase=False`: Đã thực hiện chuẩn hóa chữ thường ở bước tiền xử lý.
- `ngram_range=(1, 2)`: Trích xuất đồng thời Unigram (từ đơn) và Bigram (cụm 2 từ liên tiếp).
- `min_df=2`: Bỏ qua các đặc trưng xuất hiện ở ít hơn 2 văn bản trong toàn bộ tập Train nhằm triệt tiêu nhiễu và lỗi chính tả hiếm gặp.
- `max_features=20000`: Giới hạn kích thước từ điển tối đa ở mức 20,000 đặc trưng phổ biến nhất.

#### 3. Kết quả trích xuất đặc trưng BoW
Sau khi huấn luyện (`fit`) trên 3,856 mẫu của tập Train:
- Kích thước không gian từ điển thu được: $|\mathcal{V}| = 11,004$ đặc trưng.
- Ma trận đặc trưng tập Train có kích thước: $X_{\text{train}} \in \mathbb{R}^{3856 \times 11004}$.
- Ma trận đặc trưng tập Test có kích thước: $X_{\text{test}} \in \mathbb{R}^{964 \times 11004}$.
- **Độ thưa của ma trận (Matrix Sparsity):** Tỷ lệ phần tử khác 0 trên toàn ma trận tập Train chỉ đạt **0.081%** (density). Điều này đồng nghĩa với việc hơn 99.9% phần tử trong ma trận là số 0! Do đó, ma trận bắt buộc phải được lưu trữ dưới định dạng ma trận thưa nén (Compressed Sparse Row - CSR Matrix) để tối ưu hóa bộ nhớ RAM và gia tốc các phép nhân ma trận.
- Số câu trong tập kiểm thử (Test) không chứa bất kỳ từ nào có trong từ điển tập Train: chỉ có **0 câu** ($n_{\text{empty}} = 0$).

---

### 2.2.2. Phương pháp trọng số TF-IDF

Mặc dù BoW đơn giản và hiệu quả, hạn chế chí mạng của nó là coi mọi từ có tần số xuất hiện như nhau đều quan trọng như nhau. Một từ xuất hiện 10 lần trong câu (như từ *"máy"*, *"sản phẩm"*, hoặc dấu phẩy `","`) sẽ có trọng số cao gấp 10 lần một từ xuất hiện 1 lần (như từ *"phonetoken"* hay *"lừa đảo"*), mặc dù từ thứ hai mang giá trị thông tin phân biệt lớp Spam/Ham cao hơn gấp nhiều lần. Phương pháp trọng số **TF-IDF (Term Frequency - Inverse Document Frequency - Salton & Buckley, 1988)** được thiết kế để giải quyết triệt để vấn đề này.

#### 1. Công thức toán học và cơ chế hoạt động
Trọng số TF-IDF của một từ $t$ trong một văn bản $d$ là tích số của hai thành phần:
$$TF\text{-}IDF(t, d, \mathcal{D}) = TF(t, d) \times IDF(t, \mathcal{D})$$

1. **Tần số xuất hiện của từ (Term Frequency - TF):**
   Đo lường mức độ xuất hiện của từ $t$ trong văn bản $d$. Để giảm sự lấn át của các từ bị lặp lại quá nhiều lần trong một câu dài, nhóm tác giả kích hoạt tham số `sublinear_tf=True`, áp dụng phép biến đổi logarithm tự nhiên:
   $$TF_{\text{sublinear}}(t, d) = \begin{cases} 1 + \ln(TF(t, d)) & \text{nếu } TF(t, d) > 0 \\ 0 & \text{nếu } TF(t, d) = 0 \end{cases}$$
2. **Nghịch đảo tần suất văn bản (Inverse Document Frequency - IDF):**
   Đo lường mức độ phổ biến hay đặc trưng của từ $t$ trên toàn bộ kho ngữ liệu huấn luyện gồm $N$ văn bản. Thư viện Scikit-Learn áp dụng công thức làm trơn (Smooth IDF) để tránh chia cho 0:
   $$IDF(t) = \ln\left(\frac{1 + N}{1 + DF(t)}\right) + 1$$
   Trong đó $DF(t)$ (Document Frequency) là số lượng bài đánh giá trong tập Train có chứa từ $t$.
   - Nếu $t$ xuất hiện ở hầu hết mọi câu ($DF(t) \approx N$), phân số $\frac{1+N}{1+DF(t)} \approx 1 \implies \ln(1) = 0 \implies IDF(t) \to 1.0$ (trọng số tối thiểu).
   - Nếu $t$ chỉ xuất hiện ở một số rất ít câu đặc thù ($DF(t)$ nhỏ), $IDF(t)$ sẽ có giá trị rất cao ($\approx 6.0 - 8.0$).
3. **Chuẩn hóa vector theo chuẩn L2 (L2 Vector Normalization):**
   Sau khi tính toán trọng số TF-IDF cho từng phần tử, mỗi vector văn bản $v = (v_1, v_2, \dots, v_{|\mathcal{V}|})$ được chuẩn hóa Euclid để độ dài của nó bằng đúng 1:
   $$v_{\text{norm}} = \frac{v}{\|v\|_2} = \frac{v}{\sqrt{\sum_{j=1}^{|\mathcal{V}|} v_j^2}}$$
   Kỹ thuật này giúp loại bỏ hoàn toàn sự thiên lệch do độ dài câu: một bình luận ngắn 5 từ và một bình luận dài 50 từ nếu có cùng mật độ từ khóa spam sẽ có độ lớn vector tương đương nhau trong không gian đặc trưng.

---

[CHÈN HÌNH 2.3 TẠI ĐÂY: Đồ thị phân phối giá trị nghịch đảo tần suất văn bản (IDF) giữa các từ phổ biến và từ đặc trưng]
*(Placeholder: /assets/images/hinh2_3_phan_phoi_idf.png - Kích thước khuyến nghị: 14cm x 6cm, căn giữa)*

---

#### 2. Phân tích thống kê giá trị IDF trên dữ liệu thực tế
Trên tập Train thực nghiệm gồm 3,856 mẫu, hệ thống thu được kích thước từ điển tương đương BoW là 11,004 đặc trưng. Phân tích giá trị IDF cho thấy sự phân hóa tuyệt đối:
- **Top các token có IDF thấp nhất (từ phổ biến, ít giá trị thông tin):**
  - Dấu chấm `.` ($IDF = 1.63$)
  - Dấu phẩy `,` ($IDF = 1.76$)
  - `numtoken` ($IDF = 1.94$)
  - `không` ($IDF = 2.15$)
  - `máy` ($IDF = 2.34$)
  - `sản phẩm` ($IDF = 3.01$)
- **Top các token có IDF cao nhất (từ hiếm, tính đặc thù cao):**
  - Các cụm từ chuyên biệt như `alo`, `zalo phonetoken`, `vay vốn`, `trả góp` đều có $IDF \approx 7.15 - 7.86$.

---

### 2.2.3. Biểu diễn từ trong không gian vector liên tục - Word2Vec

Cả BoW và TF-IDF đều là các biểu diễn rời rạc (Discrete Representations) tạo ra các vector thưa hàng chục nghìn chiều và hoàn toàn không nắm bắt được ngữ nghĩa tương đồng giữa các từ: trong không gian BoW, vector của từ *"tốt"* và vector của từ *"ổn"* hoàn toàn trực giao với nhau (tích vô hướng bằng 0), khiến mô hình coi chúng là hai khái niệm không liên quan.

Mô hình **Word2Vec (Mikolov et al., 2013)** do nhóm nghiên cứu của Tomas Mikolov tại Google phát triển đã giải quyết hạn chế này bằng cách biểu diễn mỗi từ thành một vector thực dày đặc (Dense Vector) trong không gian số chiều thấp (thường từ 50 đến 300 chiều) dựa trên giả thuyết phân phối (Distributional Hypothesis): *"Các từ xuất hiện trong những ngữ cảnh tương tự nhau thì có xu hướng mang ý nghĩa tương tự nhau"*.

---

[CHÈN HÌNH 2.4 TẠI ĐÂY: Kiến trúc mạng nơ-ron Skip-gram trong mô hình Word2Vec]
*(Placeholder: /assets/images/hinh2_4_kien_truc_word2vec_skipgram.png - Kích thước khuyến nghị: 14cm x 7cm, căn giữa)*

---

#### 1. Kiến trúc Skip-gram và Hàm mục tiêu Negative Sampling
Trong nghiên cứu này, nhóm tác giả lựa chọn kiến trúc **Skip-gram** thay vì CBOW. Với một chuỗi các từ trong bài đánh giá $\{w_1, w_2, \dots, w_T\}$, tại mỗi bước, mô hình lấy từ trung tâm $w_t$ làm đầu vào và cố gắng cực đại hóa xác suất dự đoán các từ ngữ cảnh $w_{t+j}$ nằm trong cửa sổ kích thước $c$ ($j \in [-c, c], j \neq 0$):
$$\mathcal{L}(\theta) = \sum_{t=1}^T \sum_{-c \le j \le c, j \ne 0} \log P(w_{t+j} \mid w_t)$$

Để tối ưu hóa hàm xác suất Softmax vốn có chi phí tính toán tỷ lệ thuận với kích thước toàn bộ từ điển ($O(|\mathcal{V}|)$), kỹ thuật **Lấy mẫu âm (Negative Sampling)** được áp dụng. Với mỗi cặp từ ngữ cảnh dương tính $(w_t, w_O)$, mô hình lấy mẫu thêm $K$ từ âm tính ngẫu nhiên $w_{n,k}$ theo phân phối xác suất Unigram lũy thừa $3/4$:
$$\log \sigma(v'_{w_O}^\top v_{w_t}) + \sum_{k=1}^K \mathbb{E}_{w_{n,k} \sim P_n(w)} \left[ \log \sigma(-v'_{w_{n,k}}^\top v_{w_t}) \right]$$
Trong đó $\sigma(z) = \frac{1}{1 + e^{-z}}$ là hàm kích hoạt sigmoid, $v_w$ là vector biểu diễn đầu vào của từ $w$, và $v'_w$ là vector biểu diễn ngữ cảnh đầu ra.

#### 2. Cấu hình huấn luyện mô hình Word2Vec nội bộ
Mô hình Word2Vec được huấn luyện trực tiếp trên tập Train của bài toán bằng thư viện `gensim`:
- `vector_size = 100`: Mỗi từ được biểu diễn bởi một vector 100 chiều thực liên tục.
- `window = 5`: Cửa sổ ngữ cảnh trượt 5 từ bên trái và 5 từ bên phải từ trung tâm.
- `min_count = 2`: Bỏ qua các từ xuất hiện dưới 2 lần trong tập Train.
- `sg = 1`: Kích hoạt kiến trúc Skip-gram.
- `epochs = 30`: Huấn luyện lặp qua tập dữ liệu 30 lần.
- `workers = 1`, `seed = 42`: Cố định luồng đơn và hạt giống ngẫu nhiên để bảo đảm tính tái lập kết quả thực nghiệm 100%.

*Kiểm chứng định tính không gian vector học được:*
Sau khi huấn luyện xong trên tập Train, các phép đo độ tương đồng Cosine (`wv.most_similar`) đã phản ánh rõ rệt quan hệ ngữ nghĩa thực tế:
- Token `tốt` có các từ lân cận gần nhất: `ok` (0.70), `phầm` (0.68), `phảm` (0.68), `ổn` (0.62).
- Token `zalo` có các từ lân cận gần nhất: `ib` (0.77), `phonetoken` (0.76), `huyền` (0.76), `dũng` (0.73).
- Token `phonetoken` có các từ lân cận gần nhất: `sđt` (0.80), `tú` (0.78), `zalo` (0.76).
- Token `giao` có các từ lân cận gần nhất: `shipper` (0.59).
- Token `nóng` có các từ lân cận gần nhất: `cục` (0.62 - chỉ cụm *"cục nóng điều hòa"*), `lạnh` (0.52).

Điều này chứng minh không gian nhúng từ 100 chiều đã học được sâu sắc các cụm hành vi spam (zalo, sđt, inbox chèo kéo) và các cụm ngữ nghĩa ngành hàng điện máy.

#### 3. Kỹ thuật tổng hợp vector bài đánh giá (Document Vector Pooling)
Word2Vec cung cấp vector biểu diễn cho từng từ riêng lẻ, nhưng bài toán phân loại lại yêu cầu một vector đại diện cho **toàn bộ câu đánh giá**. Nhóm tác giả hiện thực hóa kỹ thuật **Mean Pooling** (Trung bình cộng):
$$v_{\text{doc}} = \frac{1}{|d_{\text{known}}|} \sum_{w \in d_{\text{known}}} v_w$$
Trong đó $d_{\text{known}}$ là tập hợp các từ trong câu có mặt trong từ điển Word2Vec.
- *Xử lý từ ngoài từ điển (OOV):* Nếu một câu trong tập Test không chứa bất kỳ từ nào nằm trong từ điển huấn luyện, toàn bộ vector của câu sẽ được gán bằng vector không: $\vec{0} \in \mathbb{R}^{100}$.

#### 4. Bảng đối sánh 3 không gian đặc trưng văn bản

*Bảng 2.2: So sánh các đặc tính không gian đặc trưng giữa BoW, TF-IDF và Word2Vec.*

| Đặc tính kỹ thuật | Bag of Words (BoW) | TF-IDF | Word2Vec (Skip-gram Pooling) |
| :--- | :--- | :--- | :--- |
| **Số chiều đặc trưng ($D$)** | 11,004 chiều | 11,004 chiều | **100 chiều** |
| **Cấu trúc không gian** | Rất thưa (Sparsity > 99.9%) | Rất thưa (Sparsity > 99.9%) | **Dày đặc (Dense 100%)** |
| **Miền giá trị phần tử** | Số nguyên không âm ($\mathbb{N}_0$) | Số thực dương $[0, 1]$ | Số thực liên tục $(-\infty, +\infty)$ |
| **Bảo toàn ngữ nghĩa từ** | Hoàn toàn không | Hoàn toàn không | **Có (Cosine similarity cao)** |
| **Ảnh hưởng của độ dài câu**| Rất lớn (câu dài đếm nhiều) | Đã triệt tiêu (L2 norm) | Đã triệt tiêu (phép chia trung bình) |
| **Độ nhạy với từ hiếm** | Kém | **Rất tốt (IDF cao)** | Trung bình |
| **Định dạng lưu trữ** | Ma trận thưa CSR | Ma trận thưa CSR | Ma trận thực NumPy (`float32`) |

---

## 2.3. Huấn luyện mô hình học máy cho bài toán phân loại

Sau khi biến đổi văn bản thành các vector toán học, bước tiếp theo là xây dựng các bộ phân loại học máy có khả năng học đường biên quyết định giữa hai lớp Spam ($y = 1$) và Ham ($y = 0$). Nghiên cứu tập trung khảo sát hai họ thuật toán nền tảng, có tính thực tiễn cao: **Naive Bayes** và **Support Vector Machines (SVM)**.

---

### 2.3.1. Mô hình phân loại xác suất Naive Bayes

Mô hình Naive Bayes (Bayes ngây thơ) dựa trên việc áp dụng Định lý xác suất Bayes với một giả định cốt lõi (gọi là "ngây thơ" - naive): **Mọi đặc trưng đầu vào $x_1, x_2, \dots, x_D$ đều độc lập có điều kiện với nhau khi biết trước nhãn của lớp $y$**.

Theo định lý Bayes, xác suất hậu nghiệm để một bài đánh giá biểu diễn bởi vector $x$ thuộc về lớp $c \in \{0, 1\}$ là:
$$P(y = c \mid x) = \frac{P(y = c) P(x \mid y = c)}{P(x)}$$
Vì mẫu số $P(x)$ không phụ thuộc vào lớp $c$, bài toán tối ưu hóa quyết định phân loại trở thành:
$$\hat{y} = \arg\max_{c \in \{0, 1\}} P(y = c) \prod_{j=1}^D P(x_j \mid y = c)$$
Tùy thuộc vào bản chất của không gian đặc trưng đầu vào (số nguyên đếm, số thực dương, hay số thực liên tục), các biến thể phân phối xác suất khác nhau được áp dụng:

#### 1. Multinomial Naive Bayes (MNB) cho đặc trưng Bag-of-Words
Multinomial Naive Bayes là lựa chọn kinh điển dành cho các đặc trưng dạng đếm tần số rời rạc không âm như BoW:
$$P(x \mid y = c) = \frac{(\sum_j x_j)!}{\prod_j x_j!} \prod_{j=1}^D p_{cj}^{x_j}$$
Trong đó xác suất từ thứ $j$ xuất hiện trong lớp $c$ được ước lượng thông qua tần suất kèm **hệ số làm trơn Laplace (Laplace Smoothing) $\alpha$**:
$$\hat{p}_{cj} = \frac{N_{cj} + \alpha}{N_c + \alpha |\mathcal{V}|}$$
- $N_{cj}$: Tổng số lần từ thứ $j$ xuất hiện trong các bài đánh giá thuộc lớp $c$ trên tập Train.
- $N_c = \sum_{j} N_{cj}$: Tổng số lượng tất cả các token xuất hiện trong lớp $c$.
- $\alpha > 0$: Hệ số làm trơn nhằm ngăn ngừa hiện tượng xác suất bằng 0 khi gặp một từ chưa từng xuất hiện trong lớp $c$ trên tập huấn luyện (zero-probability problem). Tham số $\alpha$ được dò tìm tối ưu trong không gian: $\alpha \in \{0.001, 0.003, 0.01, 0.03, 0.1, 0.3, 1.0\}$.

#### 2. Complement Naive Bayes (CNB) cho đặc trưng TF-IDF
Multinomial Naive Bayes mặc định thường hoạt động kém khi tập dữ liệu bị mất cân bằng lớp trầm trọng (như trường hợp bài toán này: số câu Ham gấp 4.7 lần số câu Spam), vì lớp đa số sẽ chiếm ưu thế hoàn toàn trong việc ước lượng các tham số $N_c$. 

Để khắc phục hiện tượng này, Rennie et al. (ICML 2003) đã đề xuất **Complement Naive Bayes (CNB)**. Thay vì ước lượng xác suất của từ trên tập hợp các câu thuộc lớp $c$, CNB ước lượng xác suất của từ trên tập hợp các câu thuộc **tất cả các lớp CÒN LẠI (Lớp phần bù $\bar{c}$)**:
$$\hat{\theta}_{\bar{c}j} = \frac{N_{\bar{c}j} + \alpha}{N_{\bar{c}} + \alpha |\mathcal{V}|}$$
Quy tắc phân loại của CNB là gán mẫu $x$ cho lớp nào có mức độ "không khớp" với lớp phần bù là lớn nhất:
$$\hat{y} = \arg\min_{c \in \{0, 1\}} \sum_{j=1}^D x_j \log \left( \frac{N_{\bar{c}j} + \alpha}{N_{\bar{c}} + \alpha |\mathcal{V}|} \right)$$
Nhờ cơ chế này, CNB đặc biệt ổn định và đạt độ chính xác cao vượt trội khi kết hợp với trọng số thực không âm TF-IDF trên các tập dữ liệu lệch lớp.

#### 3. Gaussian Naive Bayes (GNB) cho đặc trưng Word Embedding
Vì các vector nhúng từ Word2Vec là các số thực liên tục có thể mang giá trị âm, mô hình MNB và CNB không thể hoạt động. Do đó, **Gaussian Naive Bayes (GNB)** được sử dụng. GNB giả định rằng với mỗi lớp $c$, giá trị của đặc trưng thứ $j$ tuân theo một phân phối chuẩn một chiều (Gaussian Distribution) độc lập với kỳ vọng $\mu_{cj}$ và phương sai $\sigma_{cj}^2$:
$$P(x_j \mid y = c) = \frac{1}{\sqrt{2\pi \sigma_{cj}^2}} \exp\left( -\frac{(x_j - \mu_{cj})^2}{2\sigma_{cj}^2} \right)$$
Để tránh lỗi tràn số hoặc chia cho 0 khi phương sai của một chiều quá nhỏ, scikit-learn bổ sung tham số `var_smoothing`: cộng thêm một lượng nhỏ $\epsilon \times \max(\sigma^2)$ vào phương sai. Tham số `var_smoothing` được tìm kiếm trên thang đo logarithm: $\epsilon \in [10^{-12}, 10^{-1}]$.

*Phân tích phê phán lý thuyết:* Giả định độc lập có điều kiện của Naive Bayes bị vi phạm đặc biệt nghiêm trọng trong không gian Word Embedding. Các chiều trong vector nhúng từ liên tục vốn có mối tương quan phi tuyến chặt chẽ với nhau (Covariance matrix giữa các chiều khác 0 rất nhiều). Việc giả định ma trận hiệp phương sai là ma trận đường chéo (Diagonal Covariance) khiến Gaussian Naive Bayes thường xuyên tính toán sai lệch phân phối xác suất hậu nghiệm, dẫn đến tỷ lệ dự đoán nhầm rất cao.

*Bảng 2.3: Bảng tổng hợp các biến thể Naive Bayes và lý do lựa chọn cho từng loại không gian biểu diễn.*

| Biến thể Naive Bayes | Không gian đặc trưng áp dụng | Bản chất phân phối giả định | Ưu thế thiết kế | Siêu tham số dò tìm |
| :--- | :--- | :--- | :--- | :--- |
| **MultinomialNB** | Bag of Words (BoW) | Phân phối đa thức (Đếm nguyên) | Nhanh, chuẩn mực cho đếm từ | $\alpha \in [0.001, 1.0]$ |
| **ComplementNB** | TF-IDF | Phân phối đa thức có trọng số | **Khắc phục lệch lớp** | $\alpha \in [0.001, 1.0]$ |
| **GaussianNB** | Word2Vec (WE) | Phân phối chuẩn liên tục | Xử lý được vector thực âm | `var_smoothing` $\in [10^{-12}, 10^{-1}]$ |

---

### 2.3.2. Mô hình Máy vector hỗ trợ - Support Vector Machine (SVM)

Máy vector hỗ trợ (Support Vector Machine - SVM - Cortes & Vapnik, 1995) là một trong những thuật toán học máy có giám sát mạnh mẽ, ổn định và có cơ sở lý thuyết toán học vững chắc nhất trong lịch sử trí tuệ nhân tạo.

---

[CHÈN HÌNH 2.5 TẠI ĐÂY: Cơ chế tìm siêu phẳng phân tách tối ưu và khoảng cách lề (Margin) trong Support Vector Machine]
*(Placeholder: /assets/images/hinh2_5_co_che_svm_margin.png - Kích thước khuyến nghị: 14cm x 7cm, căn giữa)*

---

#### 1. Nguyên lý tối đa hóa khoảng cách lề (Maximum Margin Hyperplane)
Khác với các thuật toán tối ưu xác suất, mục tiêu hình học của SVM là tìm một siêu phẳng quyết định (Decision Hyperplane) $w^\top x + b = 0$ phân tách hoàn hảo hai lớp dữ liệu sao cho **khoảng cách lề (Margin) giữa siêu phẳng tới các điểm dữ liệu gần nhất của hai lớp (gọi là các Vector hỗ trợ - Support Vectors) đạt giá trị cực đại**.

Khoảng cách từ một điểm $x$ tới siêu phẳng là $\frac{|w^\top x + b|}{\|w\|_2}$. Khoảng cách lề hình học giữa hai lớp là $\frac{2}{\|w\|_2}$. Do đó, tối đại hóa khoảng cách lề tương đương với bài toán tối thiểu hóa độ dài vector trọng số: $\min \frac{1}{2} \|w\|_2^2$.

#### 2. Bài toán tối ưu biên mềm (Soft-Margin SVM) và Siêu tham số Điều hòa $C$
Trong dữ liệu thực tế, hai lớp Spam và Ham luôn có sự đan xen (không thể phân tách tuyến tính tuyệt đối). Do đó, Vapnik đưa vào các biến bù trễ $\xi_i \ge 0$ (Slack Variables) để cho phép một số mẫu vi phạm lề hoặc bị phân loại sai ở mức độ có thể kiểm soát. Bài toán tối ưu hóa lồi biên mềm dạng nguyên thủy (Primal Optimization) có dạng:
$$\min_{w, b, \xi} \frac{1}{2} \|w\|_2^2 + C \sum_{i=1}^N \xi_i$$
$$\text{thỏa mãn các ràng buộc:} \quad y_i (w^\top \phi(x_i) + b) \ge 1 - \xi_i, \quad \xi_i \ge 0, \quad \forall i = 1, \dots, N$$
Trong đó:
- $y_i \in \{-1, +1\}$ là nhãn của mẫu thứ $i$.
- $\phi(x_i)$ là hàm ánh xạ không gian (nếu sử dụng nhân phi tuyến).
- **Siêu tham số $C > 0$ (Regularization Parameter):** Đóng vai trò kiểm soát sự cân bằng (Trade-off) giữa độ rộng của lề và độ lớn của hàm phạt lỗi huấn luyện.
  - Khi $C$ nhỏ: Mô hình ưu tiên lề rộng, chấp nhận bỏ qua một số lỗi huấn luyện nhỏ $\implies$ Tăng khả năng chống quá khớp (Regularization mạnh).
  - Khi $C$ lớn: Mô hình phạt rất nặng mọi sai sót trên tập huấn luyện $\implies$ Lề hẹp lại, mô hình cố gắng phân loại đúng từng mẫu train, có nguy cơ bị overfit.

#### 3. Cơ chế cân bằng trọng số lớp (`class_weight='balanced'`)
Do số lượng mẫu Ham (3,181 mẫu train) áp đảo hoàn toàn số lượng mẫu Spam (675 mẫu train), nếu phạt các lỗi như nhau, SVM sẽ ưu tiên tối ưu hóa việc phân loại đúng lớp Ham và coi nhẹ lớp Spam. Để giải quyết triệt để vấn đề này, tham số `class_weight='balanced'` được kích hoạt. Trọng số phạt của mỗi lớp $c$ được tự động tính theo tỷ lệ nghịch với tần suất của nó trong tập huấn luyện:
$$w_c = \frac{N}{2 \times N_c}$$
Với lớp Ham: $w_0 = \frac{3856}{2 \times 3181} \approx 0.606$.
Với lớp Spam: $w_1 = \frac{3856}{2 \times 675} \approx 2.856$.
Tỷ lệ phạt lỗi giữa Spam và Ham là: $\frac{w_1}{w_0} \approx 4.71$ lần! Điều này đồng nghĩa với việc nếu SVM phân loại sai 1 mẫu Spam, nó sẽ bị phạt nặng gấp 4.7 lần so với việc phân loại sai 1 mẫu Ham, buộc thuật toán phải đẩy lề quyết định về phía bảo vệ tối đa lớp Spam, từ đó tăng vọt chỉ số Recall cho lớp Spam.

#### 4. Tuyến tính hóa với LinearSVC trên BoW và TF-IDF
Với các biểu diễn BoW và TF-IDF, số chiều của không gian đặc trưng lên tới $D = 11,004$ chiều — lớn hơn gấp gần 3 lần số lượng mẫu huấn luyện ($N = 3,856$). Theo **Định lý phân tách Cover (Cover's Theorem on Separability of Patterns)**: Một bài toán phân loại phức tạp khi được chiếu vào không gian số chiều rất cao thì xác suất để nó có thể phân tách tuyến tính được tiệm cận 1. Do đó, việc sử dụng hàm nhân tuyến tính (Linear Kernel) là hoàn toàn tối ưu cả về mặt lý thuyết lẫn thực nghiệm.

Nhóm tác giả sử dụng lớp `LinearSVC` (dựa trên thư viện C++ LibLinear tối ưu hóa thuật toán Coordinate Descent). LinearSVC có tốc độ hội tụ nhanh hơn hàng chục lần so với lớp `SVC(kernel='linear')` cổ điển, xử lý hoàn hảo các ma trận thưa quy mô lớn.

#### 5. Hàm nhân phi tuyến RBF (Radial Basis Function Kernel) trên Word Embedding
Ngược lại với BoW và TF-IDF, vector Word2Vec chỉ có 100 chiều và hoàn toàn dày đặc. Trong không gian 100 chiều, ranh giới giữa Spam và Ham có cấu trúc hình học phi tuyến phức tạp, không thể phân tách bằng một mặt phẳng thẳng.

Do đó, nhóm tác giả sử dụng mô hình `SVC` với hàm nhân bán kính cơ sở **RBF (Gaussian Kernel)**:
$$K(x, x') = \exp\left( -\gamma \|x - x'\|_2^2 \right)$$
Hàm nhân RBF ánh xạ các vector 100 chiều vào một không gian Hilbert vô hạn chiều (Infinite-dimensional Hilbert Space), cho phép mô hình học được các ranh giới phi tuyến uốn lượn tùy ý.
- **Tham số $\gamma > 0$:** Kiểm soát bán kính ảnh hưởng của từng Support Vector. Nếu $\gamma$ quá lớn, bán kính ảnh hưởng hẹp, biên quyết định sẽ co cụm quanh các điểm dữ liệu cá biệt dẫn đến overfit. Trong thực nghiệm, nhóm thử nghiệm $\gamma \in \{\text{'scale'}, 0.001, 0.01, 0.1\}$.
- **Chuẩn hóa dữ liệu bằng `StandardScaler` trong `Pipeline`:**
  Vì khoảng cách Euclid $\|x - x'\|_2^2$ trong hàm nhân RBF rất nhạy cảm với thang đo của từng chiều, việc chuẩn hóa đưa từng chiều về kỳ vọng 0 và phương sai 1 là bắt buộc. Nhóm đóng gói `StandardScaler()` và `SVC(kernel='rbf')` trong một `Pipeline` thống nhất của Scikit-Learn:
  ```python
  estimator = Pipeline([
      ("scaler", StandardScaler()),
      ("svm", SVC(kernel="rbf", random_state=42))
  ])
  ```
  *Ý nghĩa phòng chống rò rỉ:* Việc đưa `StandardScaler` vào bên trong `Pipeline` đảm bảo rằng trong suốt quá trình kiểm định chéo (5-fold Cross-Validation), thang đo chuẩn hóa chỉ được tính toán trên 4 fold huấn luyện con và áp dụng sang 1 fold kiểm thử con, tuyệt đối không để rò rỉ giá trị trung bình toàn cục.

---

### 2.3.3. Sơ đồ quy trình tổng thể (Pipeline) của hệ thống đề xuất

Toàn bộ kiến trúc và luồng xử lý dữ liệu của hệ thống phân loại đánh giá rác đề xuất được mô tả tổng hợp qua sơ đồ kiến trúc khối tại **Hình 2.6**:

```
+-------------------------------------------------------------------------+
|                  1. THU THẬP & LỌC DỮ LIỆU BAN ĐẦU                      |
|  - File raw: 10,892 đánh giá từ 114 sản phẩm TMĐT thuộc 10 ngành hàng   |
+-------------------------------------------------------------------------+
                                     |
                                     v
+-------------------------------------------------------------------------+
|                2. TIỀN XỬ LÝ VĂN BẢN & CHỐNG RÒ RỈ DỮ LIỆU              |
|  - Chuẩn hóa Unicode NFC, chuyển chữ thường (lowercase)                 |
|  - Thay URL -> urltoken, Email -> emailtoken, SĐT -> phonetoken         |
|  - Thay số/tiền -> numtoken, rút gọn ký tự lặp, tách dấu câu            |
|  - Chuẩn hóa Teencode & từ viết tắt theo từ điển chuyên ngành           |
|  - Biểu quyết đa số (Majority Voting) cho các câu mâu thuẫn nhãn        |
|  - KHỬ TRÙNG LẶP TRIỆT ĐỂ: 10,892 -> 4,820 câu độc nhất (loại 55.7%)    |
|  - Phân chia phân tầng 80/20: Train (3,856 mẫu) | Test (964 mẫu)        |
+-------------------------------------------------------------------------+
                                     |
                                     v
+-------------------------------------------------------------------------+
|            3. TRÍCH CHỌN ĐẶC TRƯNG (FIT CHỈ TRÊN TẬP TRAIN)             |
|  [BoW]: CountVectorizer(ngram=(1,2), min_df=2)  -> 11,004 features      |
|  [TF-IDF]: TfidfVectorizer(sublinear_tf=True, L2) -> 11,004 features    |
|  [WE]: Word2Vec Skip-gram(dim=100, win=5) + Mean Pooling -> 100 features|
+-------------------------------------------------------------------------+
                                     |
                                     v
+-------------------------------------------------------------------------+
|       4. HUẤN LUYỆN & TỐI ƯU SIÊU THAM SỐ (5-FOLD STRATIFIED CV)        |
|  - Chỉ thực hiện trên tập Train 3,856 mẫu                               |
|  - Tiêu chí tối ưu: F1-Score của lớp Spam (đối phó lệch lớp)            |
|  - Dò tìm tham số tối ưu cho 6 cấu hình mô hình:                        |
|    * MultinomialNB + BoW          * Linear SVM + BoW                    |
|    * ComplementNB + TF-IDF        * Linear SVM + TF-IDF                 |
|    * GaussianNB + Word2Vec        * RBF SVM (StandardScaler) + Word2Vec |
+-------------------------------------------------------------------------+
                                     |
                                     v
+-------------------------------------------------------------------------+
|             5. HUẤN LUYỆN LẠI TOÀN BỘ TRAIN & DỰ ĐOÁN TẬP TEST          |
|  - Fit best_estimator trên toàn bộ 3,856 mẫu train                      |
|  - Transform và Predict trên 964 mẫu kiểm thử độc lập                   |
+-------------------------------------------------------------------------+
                                     |
                                     v
+-------------------------------------------------------------------------+
|             6. ĐÁNH GIÁ ĐA ĐỘ ĐO & XUẤT BÁO CÁO PHÂN TÍCH LỖI           |
|  - Tính Accuracy, Precision, Recall, F1-Spam, Macro-F1, ROC-AUC, PR-AUC |
|  - Vẽ và lưu Ma trận nhầm lẫn (Confusion Matrix PNG)                    |
|  - Trích xuất danh sách dự đoán sai (FP, FN) vào file errors.csv        |
|  - Cập nhật tự động bảng so sánh tổng hợp vào results/summary.csv       |
+-------------------------------------------------------------------------+
```

---

[CHÈN HÌNH 2.6 TẠI ĐÂY: Sơ đồ quy trình tổng thể (Pipeline) của hệ thống phân loại đánh giá rác đề xuất]
*(Placeholder: /assets/images/hinh2_6_pipeline_tong_the.png - Kích thước khuyến nghị: 15cm x 11cm, căn giữa)*

---

*Nguyên tắc thiết kế bất biến của Pipeline:* Toàn bộ các bộ chuyển đổi vector (`CountVectorizer`, `TfidfVectorizer`), mô hình `Word2Vec`, và bộ chuẩn hóa `StandardScaler` **chỉ được phép gọi hàm `.fit()` hoặc huấn luyện duy nhất trên tập Train**. Tập Test hoàn toàn đóng vai trò là dữ liệu "chưa từng nhìn thấy" (Unseen Data) và chỉ được thực hiện phép biến đổi chiếu (`.transform()`). Bất kỳ sự vi phạm nào đối với nguyên tắc này đều cấu thành lỗi rò rỉ thông tin trong học máy.

\newpage

# CHƯƠNG 3: THỰC NGHIỆM VÀ ĐÁNH GIÁ KẾT QUẢ

Chương 3 trình bày toàn bộ quá trình thu thập, xử lý dữ liệu thực nghiệm, thiết lập môi trường kỹ thuật, định nghĩa các độ đo khoa học, và đặc biệt là phân tích chuyên sâu các kết quả thực nghiệm đạt được từ 6 cấu hình mô hình học máy trên tập kiểm thử độc lập. Mọi số liệu, bảng biểu và ma trận nhầm lẫn trong chương này được trích xuất trực tiếp từ các file nhật ký thực nghiệm trong thư mục `results/` của dự án.

---

## 3.1. Thu thập và xử lý dữ liệu thực nghiệm

### 3.1.1. Mô tả tập dữ liệu gốc

Tập dữ liệu thô phục vụ cho nghiên cứu được thu thập từ hệ thống đánh giá sản phẩm của các sàn thương mại điện tử lớn tại Việt Nam (Shopee, Tiki, Lazada và hệ thống siêu thị Điện Máy Xanh), tập trung vào các thiết bị điện tử, điện máy và đồ gia dụng thông minh:
- **Tổng số lượng bản ghi gốc:** 10,892 bài đánh giá (dòng dữ liệu).
- **Cấu trúc trường thông tin:** Mỗi bản ghi gồm 5 thuộc tính:
  1. `category`: Tên danh mục thiết bị sản phẩm.
  2. `product`: Tên định danh hoặc model cụ thể của sản phẩm (gồm 114 dòng sản phẩm khác nhau).
  3. `review`: Nội dung chuỗi văn bản nhận xét của người dùng.
  4. `rating`: Điểm đánh giá mức độ hài lòng theo thang điểm từ 1 đến 5 sao.
  5. `label`: Nhãn phân loại nhị phân (1 = Spam, 0 = Ham).

#### 1. Phân bố theo danh mục sản phẩm (Category Distribution)
Tập dữ liệu bao quát 10 ngành hàng điện máy gia dụng phổ biến nhất trên thị trường, được mô tả chi tiết tại **Bảng 3.1**:

*Bảng 3.1: Thống kê phân bố số lượng đánh giá theo 10 danh mục sản phẩm điện máy trong tập dữ liệu.*

| STT | Danh mục sản phẩm (Category) | Số lượng đánh giá | Tỷ lệ phần trăm (%) | Ví dụ thiết bị đại diện |
| :---: | :--- | :---: | :---: | :--- |
| 1 | **Tủ lạnh** | 1,189 | 24.67% | Inverter Toshiba, Panasonic 2 cánh, Samsung |
| 2 | **Nồi cơm điện** | 988 | 20.50% | Nồi cao tần Cuckoo, Sunhouse, Sharp |
| 3 | **Điều hòa** | 682 | 14.15% | Daikin Inverter, Panasonic 1 HP, Casper |
| 4 | **Máy giặt** | 646 | 13.40% | LG lồng ngang, Electrolux Inverter, Toshiba |
| 5 | **Tivi** | 437 | 9.07% | Smart Tivi Sony 4K, Samsung Crystal UHD |
| 6 | **Máy lọc nước** | 372 | 7.72% | Karofi 10 lõi RO, Kangaroo Hydrogen |
| 7 | **Máy lọc không khí** | 175 | 3.63% | Xiaomi Smart Air Purifier, Sharp tạo ion |
| 8 | **Máy sấy quần áo** | 127 | 2.63% | Máy sấy thông hơi Electrolux, Candy |
| 9 | **Camera giám sát** | 108 | 2.24% | Camera IP Wifi Ezviz, Imou ngoài trời |
| 10 | **Khác (Gia dụng nhỏ)** | 96 | 1.99% | Quạt điều hòa, bàn ủi hơi nước, máy ép |
| **Tổng** | **10 danh mục sản phẩm** | **4,820** | **100.0%** | **114 dòng sản phẩm riêng biệt** |

#### 2. Phân bố theo số sao đánh giá (Rating Distribution)
Thống kê điểm số hài lòng của khách hàng cho thấy mức phân bố tự nhiên trên các sàn thương mại điện tử, tập trung chủ yếu ở mức 5 sao và 4 sao, được mô tả tại **Bảng 3.2**:

*Bảng 3.2: Thống kê phân bố số lượng đánh giá theo số sao (Rating) trong tập dữ liệu thực nghiệm.*

| Mức đánh giá (Rating) | Số lượng đánh giá | Tỷ lệ phần trăm (%) | Nhận xét xu hướng |
| :---: | :---: | :---: | :--- |
| **5 sao (Rất hài lòng)** | 2,253 | 46.74% | Chiếm tỷ trọng lớn nhất; khách hàng hài lòng hoặc spam khen ảo |
| **4 sao (Hài lòng)** | 1,022 | 21.20% | Đánh giá tích cực vừa phải |
| **3 sao (Bình thường)** | 560 | 11.62% | Trải nghiệm trung tính |
| **2 sao (Không hài lòng)**| 352 | 7.30% | Phản ánh sản phẩm có lỗi nhỏ hoặc dịch vụ chưa tốt |
| **1 sao (Rất tệ)** | 633 | 13.13% | Phản ánh khiếu nại gay gắt hoặc spam bôi nhọ đối thủ |
| **Tổng cộng** | **4,820** | **100.0%** | **Trung bình rating đạt 3.82 sao** |

---

### 3.1.2. Kỹ thuật lọc, tăng cường dữ liệu và kết quả sau tiền xử lý

#### 1. Xử lý câu trùng lặp và mâu thuẫn nhãn
Trong tập dữ liệu thô ban đầu (10,892 bản ghi):
- Hơn một nửa số lượng bình luận là các câu ngắn bị lặp lại hàng trăm lần (câu *"Tốt"* xuất hiện 450 lần, *"Ok"* xuất hiện 340 lần).
- Một số ít câu có nội dung giống hệt nhau nhưng bị gán nhãn mâu thuẫn (cùng một câu nhưng lúc gán nhãn 1, lúc gán nhãn 0). Hệ thống đã áp dụng luật **Biểu quyết đa số (Majority Voting)** để đưa về nhãn nhất quán duy nhất.
- Tiến hành **loại bỏ trùng lặp triệt để** dựa trên nội dung đã làm sạch (`clean_text`). 

Kết quả biến động số lượng mẫu trước và sau bước khử trùng lặp được trình bày chi tiết tại **Bảng 3.3**:

*Bảng 3.3: Thống kê số lượng mẫu và tỷ lệ phân bố lớp trước và sau khi lọc trùng lặp.*

| Tập dữ liệu | Tổng số mẫu | Số mẫu Ham ($y=0$) | Số mẫu Spam ($y=1$) | Tỷ lệ Spam (%) | Tỷ lệ giảm dòng |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Dữ liệu thô ban đầu (Raw)** | 10,892 | 6,449 | 4,443 | 40.79% | - |
| **Dữ liệu sau lọc trùng (Processed)** | **4,820** | **3,976** | **844** | **17.51%** | **Giảm 55.74%** |

*Nhận định quan trọng:* Sau khi loại bỏ 6,072 dòng trùng lặp, tỷ lệ Spam thực tế giảm từ 40.79% xuống còn **17.51%**. Con số 17.51% này phản ánh chính xác cấu trúc mất cân bằng tự nhiên của bài toán thực tế (Spam chiếm khoảng 15 - 20%), chứng minh rằng phần lớn các câu trùng lặp trong dữ liệu thô trước đó là các đánh giá ngắn bị nhân bản nhân tạo.

#### 2. Phân chia tập huấn luyện và kiểm thử phân tầng (Stratified 80/20)
Sau khi lọc trùng lặp, tập dữ liệu gồm 4,820 mẫu độc nhất được phân chia thành hai tập độc lập: **Tập huấn luyện (Train Set - 80%)** và **Tập kiểm thử (Test Set - 20%)** có phân tầng theo nhãn (`stratify=df['label']`, `random_state=42`), được mô tả tại **Bảng 3.4**:

*Bảng 3.4: Phân bố số lượng mẫu tập Train và Test sau khi phân chia phân tầng (Stratified 80/20).*

| Phân vùng dữ liệu (Split) | Tổng số mẫu | Số mẫu Ham ($y=0$) | Số mẫu Spam ($y=1$) | Tỷ lệ Spam (%) | Mục đích sử dụng |
| :--- | :---: | :---: | :---: | :---: | :--- |
| **Tập Train (80%)** | 3,856 | 3,181 | 675 | 17.50% | Huấn luyện mô hình & Tìm siêu tham số (5-fold CV) |
| **Tập Test (20%)** | 964 | 795 | 169 | 17.53% | Đánh giá độc lập khách quan (Held-out Evaluation) |
| **Toàn bộ dữ liệu** | **4,820** | **3,976** | **844** | **17.51%** | Dữ liệu độc nhất sau tiền xử lý |

#### 3. Phân tích đặc trưng độ dài văn bản sau làm sạch
Thống kê số lượng token trên mỗi câu sau khi làm sạch:
- **Độ dài trung bình:** $14.8$ token / câu.
- **Độ dài trung vị (Median):** $8.0$ token / câu.
- **Độ dài lớn nhất:** $227$ token.
- **Độ dài ngắn nhất:** $1$ token.

---

[CHÈN HÌNH 3.1 TẠI ĐÂY: Phân bố độ dài câu (số lượng token) trong tập dữ liệu sau bước làm sạch tiền xử lý]
*(Placeholder: /assets/images/hinh3_1_phan_bo_do_dai_cau.png - Kích thước khuyến nghị: 14cm x 6cm, căn giữa)*

---

#### 4. Minh họa trực quan các câu đánh giá trước và sau làm sạch
Để làm rõ tác động tích cực của pipeline tiền xử lý, **Bảng 3.5** minh họa một số mẫu câu thực tế được trích xuất từ dữ liệu:

*Bảng 3.5: Một số ví dụ cụ thể về câu đánh giá trước và sau khi thực hiện tiền xử lý làm sạch.*

| Nhãn | Đánh giá gốc người dùng nhập (`review`) | Đánh giá sau tiền xử lý (`clean_text`) | Cơ chế xử lý nổi bật |
| :---: | :--- | :--- | :--- |
| **Spam** | *"alo b nào cần vay tiền nhanh qua zalo 0987123456 nhé"* | `alo b nào cần vay tiền nhanh qua zalo phonetoken nhé` | Trừu tượng hóa số điện thoại thành `phonetoken`. |
| **Spam** | *"vao ngay http://shopee.vn/shop-xyz de nhan qua 500k"* | `vao ngay urltoken de nhan qua numtoken` | Trừu tượng hóa link web thành `urltoken` và tiền thành `numtoken`. |
| **Ham** | *"Mays xài rất tốtttt, nhân viên dmx tư vấn nhiệt tình."* | `mays xài rất tốt , nhân viên điện máy xanh tư vấn nhiệt tình .` | Hạ chữ thường, rút gọn `"tốtttt"` $\to$ `"tốt"`, giải mã teencode `"dmx"` $\to$ `"điện máy xanh"`, tách dấu câu. |
| **Ham** | *"ko êm lắm, hơi ồn vs lại tốn điện"* | `không êm lắm , hơi ồn với lại tốn điện` | Giải mã teencode `"ko"` $\to$ `"không"`, `"vs"` $\to$ `"với"`. |
| **Spam** | *"dddddddddddddddddddd"* | `d` | Rút gọn chuỗi ký tự lặp vô nghĩa. |
| **Ham** | *"Sản phẩm dùng OK lắm nha mn, nên mua ạ!"* | `sản phẩm dùng ok lắm nha mọi người , nên mua ạ !` | Chuẩn hóa chữ thường, giải mã `"mn"` $\to$ `"mọi người"`, tách dấu cảm thán. |

---

## 3.2. Môi trường cài đặt và các độ đo đánh giá

### 3.2.1. Môi trường và công cụ triển khai thực nghiệm

Nghiên cứu được thiết kế với tính khả chuyển (Portability) và khả năng tái lập (Reproducibility) cao nhất. Toàn bộ môi trường thực nghiệm được chuẩn hóa như sau:

- **Môi trường phần cứng:**
  - Vi xử lý (CPU): Intel® Core™ i5/i7 thế hệ 11 trở lên (hoặc AMD Ryzen tương đương), kiến trúc x86_64 đa nhân.
  - Bộ nhớ RAM: 16 GB DDR4.
  - Ổ cứng: 512 GB NVMe SSD.
  - *Lưu ý:* Toàn bộ quy trình huấn luyện và suy luận được thiết kế tối ưu để chạy hoàn toàn trên CPU thông thường, không đòi hỏi phần cứng GPU chuyên dụng.
- **Môi trường phần mềm và hệ điều hành:**
  - Hệ điều hành: Linux Ubuntu 22.04 LTS / 24.04 LTS x86_64.
  - Ngôn ngữ lập trình chính: Python phiên bản 3.11 / 3.14.
  - Đóng gói ứng dụng: Docker Container dựa trên base image `python:3.11-slim`.
- **Các thư viện mã nguồn mở chuyên dụng:**
  - `scikit-learn` (v1.3.0+): Trích xuất đặc trưng văn bản (`CountVectorizer`, `TfidfVectorizer`), các mô hình phân loại (`MultinomialNB`, `ComplementNB`, `GaussianNB`, `LinearSVC`, `SVC`), quy trình kiểm định chéo (`StratifiedKFold`, `GridSearchCV`), và các hàm tính toán độ đo đánh giá.
  - `gensim` (v4.3.0+): Huấn luyện và thao tác mô hình không gian vector từ Word2Vec (Skip-gram).
  - `pandas` (v2.0.0+) & `numpy` (v1.24.0+): Xử lý cấu trúc dữ liệu bảng, thao tác mảng nhiều chiều và tính toán đại số ma trận.
  - `matplotlib` & `scipy`: Trực quan hóa ma trận nhầm lẫn và biểu đồ hiệu năng.
  - `joblib`: Nạp và lưu trữ tuần tự hóa các pipeline đặc trưng và trọng số mô hình đã huấn luyện dưới dạng tệp `.pkl`.

---

### 3.2.2. Các độ đo đánh giá (Accuracy, Precision, Recall, F1-Score, Confusion Matrix)

Để đánh giá một cách toàn diện và khoa học hiệu năng của các mô hình học máy trên tập dữ liệu mất cân bằng lớp (Imbalanced Data), nghiên cứu áp dụng một hệ thống gồm 7 độ đo chuẩn hóa trong thống kê học máy:

#### 1. Ma trận nhầm lẫn (Confusion Matrix)
Ma trận nhầm lẫn là công cụ biểu diễn trực quan mối quan hệ giữa nhãn thực tế (Ground Truth) và nhãn dự đoán (Predicted Label) của mô hình phân loại nhị phân, được định nghĩa tại **Bảng 3.6**:

*Bảng 3.6: Ma trận nhầm lẫn tổng quát (Confusion Matrix) cho bài toán phân loại nhị phân Spam/Ham.*

| Nhãn thực tế (Actual) \ Dự đoán (Predicted) | Dự đoán là Ham ($\hat{y} = 0$) | Dự đoán là Spam ($\hat{y} = 1$) |
| :--- | :---: | :---: |
| **Thực tế là Ham ($y = 0$)** | **True Negative (TN)**<br>*(Đánh giá thật đoán đúng là thật)* | **False Positive (FP)**<br>*(Đánh giá thật bị báo nhầm là Spam - Báo động giả)* |
| **Thực tế là Spam ($y = 1$)** | **False Negative (FN)**<br>*(Đánh giá rác bị bỏ sót thành thật - Lọt lưới)* | **True Positive (TP)**<br>*(Đánh giá rác đoán đúng là Spam - Bắt trúng)* |

Trong ngữ cảnh vận hành của các sàn thương mại điện tử:
- **False Positive (FP - Báo nhầm):** Một bài nhận xét khen/chê chân thành của người mua thật bị hệ thống tự động xóa bỏ hoặc chặn lại vì nghi là spam. Hậu quả: Gây bức xúc cho người mua, làm mất tiếng nói khách quan của khách hàng.
- **False Negative (FN - Bỏ sót):** Một bài đánh giá lừa đảo cho vay tiền, rác lấy xu hoặc seeding ảo bị lọt qua bộ lọc và hiển thị công khai trên trang sản phẩm. Hậu quả: Người mua khác bị lừa đảo, làm sai lệch điểm số chất lượng của sản phẩm.

#### 2. Độ chính xác tổng thể (Accuracy)
Tỷ lệ giữa tổng số mẫu dự đoán đúng trên toàn bộ tập dữ liệu kiểm thử:
$$\text{Accuracy} = \frac{TP + TN}{TP + TN + FP + FN}$$
*Hạn chế cốt tử của Accuracy:* Khi tập kiểm thử bị lệch lớp (Ham chiếm 82.5%, Spam chiếm 17.5%), nếu một mô hình "ngớ ngẩn" dự đoán toàn bộ 964 câu đều là Ham ($TP = 0, FP = 0$), nó vẫn đạt Accuracy lên tới:
$$\text{Accuracy} = \frac{795}{964} \approx 82.47\%$$
Mặc dù đạt hơn 82% độ chính xác, mô hình này hoàn toàn vô dụng vì không phát hiện được bất kỳ bài spam nào. Do đó, **Accuracy chỉ mang tính chất tham khảo, không được sử dụng làm tiêu chí tối ưu hóa chính**.

#### 3. Độ chuẩn xác của lớp Spam (Precision - Spam)
Tỷ lệ giữa số mẫu spam bắt trúng thực sự trên tổng số mẫu mà mô hình tuyên bố là spam:
$$\text{Precision} = \frac{TP}{TP + FP}$$
Precision cao đồng nghĩa với việc: một khi mô hình đã báo cáo một bài là Spam, thì xác suất bài đó là spam thật rất cao (hệ thống có độ tin cậy lớn, rất ít khi báo nhầm đánh giá của người mua thật).

#### 4. Độ thu hồi của lớp Spam (Recall / Sensitivity - Spam)
Tỷ lệ giữa số mẫu spam bắt trúng thực sự trên tổng số mẫu spam thực tế tồn tại trong tập dữ liệu:
$$\text{Recall} = \frac{TP}{TP + FN}$$
Recall cao đồng nghĩa với việc: hệ thống có khả năng "quét sạch", không để lọt lưới các bài đánh giá rác (tỷ lệ bỏ sót $FN$ rất thấp).

#### 5. Điểm F1 của lớp Spam (F1-Score Spam)
Điểm F1 là trung bình điều hòa (Harmonic Mean) giữa Precision và Recall. F1-Score chỉ đạt giá trị cao khi cả Precision và Recall đều đồng thời đạt mức cao:
$$F_1\text{-Score (Spam)} = 2 \times \frac{\text{Precision} \times \text{Recall}}{\text{Precision} + \text{Recall}} = \frac{2TP}{2TP + FP + FN}$$
Trong toàn bộ nghiên cứu này, **F1-Score của lớp Spam được chọn làm tiêu chí mục tiêu cốt lõi (Scoring Metric)** trong quá trình tìm kiếm siêu tham số bằng GridSearchCV và đối sánh mô hình.

#### 6. Điểm F1 trung bình vĩ mô (Macro-Averaged F1)
Trung bình cộng không trọng số giữa điểm F1 của lớp Ham ($F_{1,\text{ham}}$) và điểm F1 của lớp Spam ($F_{1,\text{spam}}$):
$$F_1\text{-Macro} = \frac{F_{1,\text{ham}} + F_{1,\text{spam}}}{2}$$
Macro F1 đối xử với cả hai lớp bình đẳng như nhau bất kể kích thước mẫu, phản ánh năng lực phân loại toàn diện của mô hình trên cả hai phía.

#### 7. Diện tích dưới đường cong ROC (ROC-AUC) và đường cong Precision-Recall (PR-AUC)
- **ROC-AUC (Receiver Operating Characteristic - Area Under Curve):** Đo lường khả năng phân tách thứ hạng giữa các mẫu dương tính và âm tính dựa trên mối tương quan giữa Tỷ lệ dương tính thật (TPR) và Tỷ lệ dương tính giả (FPR) khi thay đổi ngưỡng phân loại từ 0 đến 1. Điểm ROC-AUC hoàn hảo bằng 1.0, và đoán mò ngẫu nhiên bằng 0.5.
- **PR-AUC (Precision-Recall Area Under Curve / Average Precision):** Đo lường diện tích dưới đường cong biểu diễn sự đánh đổi giữa Precision và Recall. Trên các tập dữ liệu mất cân bằng lớp, PR-AUC là thước đo phản ánh hiệu năng chính xác và nhạy bén hơn nhiều so với ROC-AUC.

---

## 3.3. Kết quả thực nghiệm

Để đánh giá tính hiệu quả của các giải pháp đề xuất, nhóm tác giả đã tiến hành huấn luyện và kiểm thử 6 cấu hình mô hình thực nghiệm độc lập. Quá trình tìm kiếm siêu tham số được thực hiện nghiêm ngặt bằng **5-Fold Stratified Cross-Validation chỉ trên tập Train (3,856 mẫu)**. Sau khi xác định được bộ tham số tối ưu, mô hình được huấn luyện lại trên toàn bộ tập Train và kiểm thử trên **tập Test độc lập gồm 964 mẫu (gồm 795 câu Ham và 169 câu Spam)**.

---

### 3.3.1. Kết quả thực nghiệm với mô hình Naive Bayes (trên 3 bộ đặc trưng BoW, TF-IDF, Word2Vec)

*Bảng 3.7: Kết quả thực nghiệm chi tiết của các biến thể mô hình Naive Bayes trên 3 bộ đặc trưng.*

| Mô hình | Bộ đặc trưng | Siêu tham số tối ưu | CV F1 (Train) | Accuracy | Precision (Spam) | Recall (Spam) | F1-Score (Spam) | F1 Macro | ROC-AUC | PR-AUC |
| :--- | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **MultinomialNB** | **Bag of Words** | $\alpha = 0.003$ | 0.8019 | **93.36%** | **83.02%** | 78.11% | **80.49%** | **88.24%** | **0.9769** | 0.8839 |
| **ComplementNB** | **TF-IDF** | $\alpha = 0.001$ | **0.8108** | 93.05% | 81.10% | **78.70%** | 79.88% | 87.84% | 0.9765 | **0.8926** |
| **GaussianNB** | **Word2Vec (WE)** | `var_smoothing` $= 10^{-12}$ | 0.6032 | 83.20% | 51.41% | 75.74% | 61.24% | 75.26% | 0.8966 | 0.5870 |

*Bảng 3.8: Ma trận nhầm lẫn chi tiết của 3 biến thể mô hình Naive Bayes trên tập Test (964 mẫu).*

| Mô hình Naive Bayes | True Negative (TN) | False Positive (FP) | False Negative (FN) | True Positive (TP) | Tổng lỗi sai |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **MultinomialNB + BoW** | 768 | 27 | 37 | 132 | 64 |
| **ComplementNB + TF-IDF** | 764 | 31 | 36 | 133 | 67 |
| **GaussianNB + Word2Vec** | 674 | 121 | 41 | 128 | 162 |

---

[CHÈN HÌNH 3.2 TẠI ĐÂY: Ma trận nhầm lẫn (Confusion Matrix) của mô hình Multinomial Naive Bayes + Bag of Words]
*(Placeholder: results/nb-bow_confusion_matrix.png - Kích thước khuyến nghị: 8cm x 7cm, căn giữa)*

[CHÈN HÌNH 3.3 TẠI ĐÂY: Ma trận nhầm lẫn (Confusion Matrix) của mô hình Complement Naive Bayes + TF-IDF]
*(Placeholder: results/nb-tfidf_confusion_matrix.png - Kích thước khuyến nghị: 8cm x 7cm, căn giữa)*

[CHÈN HÌNH 3.4 TẠI ĐÂY: Ma trận nhầm lẫn (Confusion Matrix) của mô hình Gaussian Naive Bayes + Word Embedding]
*(Placeholder: results/nb-we_confusion_matrix.png - Kích thước khuyến nghị: 8cm x 7cm, căn giữa)*

---

#### Phân tích chuyên sâu kết quả thực nghiệm của Naive Bayes:
1. **MultinomialNB trên Bag-of-Words** thể hiện hiệu năng rất ấn tượng đối với một mô hình xác suất tuyến tính đơn giản: Đạt **Accuracy 93.36%**, **Precision lớp Spam đạt 83.02%**, **F1-Score lớp Spam đạt 80.49%**, và **ROC-AUC lên tới 0.9769**. Mô hình chỉ báo nhầm 27 câu Ham thành Spam ($FP = 27$) và bỏ sót 37 câu Spam ($FN = 37$).
2. **ComplementNB trên TF-IDF** đạt điểm số kiểm định chéo trên tập Train cao nhất trong nhóm Naive Bayes ($CV = 81.08\%$). Trên tập Test, mô hình đạt **PR-AUC cao hơn BoW (0.8926 so với 0.8839)** và cải thiện nhẹ độ thu hồi Recall (78.70% so với 78.11%). Điều này chứng minh thuật ngữ lớp phần bù của ComplementNB đã phát huy hiệu quả hỗ trợ dữ liệu lệch lớp.
3. **Sự sụt giảm nghiêm trọng của GaussianNB trên Word2Vec (Thất bại về mặt lý thuyết):**
   Mô hình GaussianNB trên vector Word2Vec chỉ đạt **F1-Score 61.24%**, **Precision cực thấp ở mức 51.41%**, và tổng số lỗi phân loại sai vọt lên tới **162 mẫu** (gấp 2.5 lần so với MNB). Quan sát ma trận nhầm lẫn cho thấy: số lượng câu Ham bị báo nhầm là Spam lên tới **121 câu ($FP = 121$)**!
   - *Nguyên nhân bản chất:* Như đã phân tích tại Mục 2.3.1, Gaussian Naive Bayes giả định rằng các chiều trong không gian đặc trưng là hoàn toàn độc lập với nhau khi biết lớp ($Cov(x_i, x_j) = 0$). Tuy nhiên, trong không gian nhúng từ 100 chiều của Word2Vec, các chiều có mối liên kết ngữ nghĩa phi tuyến chặt chẽ. Sự vi phạm nghiêm trọng giả định nền tảng này khiến mô hình ước lượng sai lệch hàm mật độ xác suất liên hợp, dẫn đến hiện tượng "hoang tưởng" (báo động giả tràn lan), kéo tụt hiệu năng toàn diện của hệ thống.

---

### 3.3.2. Kết quả thực nghiệm với mô hình SVM (trên 3 bộ đặc trưng BoW, TF-IDF, Word2Vec)

*Bảng 3.9: Kết quả thực nghiệm chi tiết của các biến thể mô hình SVM trên 3 bộ đặc trưng.*

| Mô hình | Bộ đặc trưng | Siêu tham số tối ưu | CV F1 (Train) | Accuracy | Precision (Spam) | Recall (Spam) | F1-Score (Spam) | F1 Macro | ROC-AUC | PR-AUC |
| :--- | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Linear SVM** | **Bag of Words** | $C = 0.5$, `weight`=None | 0.8414 | 94.09% | 76.92% | **94.67%** | 84.88% | 90.60% | 0.9793 | 0.8674 |
| **Linear SVM** | **TF-IDF** | $C = 1.0$, `weight`='balanced'| 0.8377 | 93.57% | 75.60% | 93.49% | 83.60% | 89.80% | 0.9772 | 0.8579 |
| **RBF SVM** | **Word2Vec (WE)**| $C = 10.0$, `gamma`='scale', 'balanced'| **0.8755** | **95.85%** | **86.86%** | 89.94% | **88.37%** | **92.92%** | **0.9859** | **0.9265** |

*Bảng 3.10: Ma trận nhầm lẫn chi tiết của 3 biến thể mô hình SVM trên tập Test (964 mẫu).*

| Mô hình SVM | True Negative (TN) | False Positive (FP) | False Negative (FN) | True Positive (TP) | Tổng lỗi sai |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Linear SVM + BoW** | 747 | 48 | **9** | **160** | 57 |
| **Linear SVM + TF-IDF** | 744 | 51 | 11 | 158 | 62 |
| **RBF SVM + Word2Vec** | **772** | **23** | 17 | 152 | **40** |

---

[CHÈN HÌNH 3.5 TẠI ĐÂY: Ma trận nhầm lẫn (Confusion Matrix) của mô hình Linear SVM + Bag of Words]
*(Placeholder: results/svm-bow_confusion_matrix.png - Kích thước khuyến nghị: 8cm x 7cm, căn giữa)*

[CHÈN HÌNH 3.6 TẠI ĐÂY: Ma trận nhầm lẫn (Confusion Matrix) của mô hình Linear SVM + TF-IDF]
*(Placeholder: results/svm-tfidf_confusion_matrix.png - Kích thước khuyến nghị: 8cm x 7cm, căn giữa)*

[CHÈN HÌNH 3.7 TẠI ĐÂY: Ma trận nhầm lẫn (Confusion Matrix) của mô hình RBF SVM + Word Embedding]
*(Placeholder: results/svm-we_confusion_matrix.png - Kích thước khuyến nghị: 8cm x 7cm, căn giữa)*

---

#### Phân tích chuyên sâu kết quả thực nghiệm của SVM:
1. **RBF SVM trên Word2Vec xác lập vị thế QUÁN QUÂN toàn diện:**
   Mô hình kết hợp giữa **Pipeline StandardScaler + SVC nhân RBF phi tuyến trên vector Word2Vec** đã thể hiện sức mạnh vượt trội trên mọi phương diện đánh giá cốt lõi:
   - **F1-Score lớp Spam cao nhất:** **88.37%** (vượt xa mô hình tốt thứ hai hơn 3.5%).
   - **Độ chính xác tổng thể (Accuracy) cao nhất:** **95.85%**.
   - **Điểm F1 Macro cao nhất:** **92.92%**.
   - **Diện tích dưới đường cong ROC-AUC cao nhất:** **0.9859** (tiệm cận mức hoàn hảo 1.0).
   - **Diện tích dưới đường cong PR-AUC cao nhất:** **0.9265**.
   - **Tổng số lỗi phân loại ít nhất:** Chỉ mắc đúng **40 lỗi sai trên tổng số 964 câu kiểm thử** (tỷ lệ lỗi chỉ 4.15%), trong đó chỉ có 23 ca báo nhầm ($FP = 23$) và 17 ca bỏ sót ($FN = 17$).
   - *Lý giải thành công:* Khác với Naive Bayes bị trói buộc bởi giả định độc lập, SVM nhân RBF hoàn toàn tự do trong việc học các siêu mặt phi tuyến uốn lượn phức tạp trong không gian 100 chiều. Các cụm từ đồng nghĩa mà Word2Vec đã gom lại (như nhóm từ liên hệ chèo kéo: `zalo`, `sđt`, `ib`, `phonetoken`) được nhân RBF khai thác triệt để nhằm định hình đường biên phân cách tối ưu.
2. **Linear SVM trên Bag-of-Words — "Chiến thần" về độ thu hồi (Recall):**
   Mô hình LinearSVC trên BoW đạt được một kết quả cực kỳ đặc biệt: **Recall lớp Spam lên tới 94.67%** — mức cao nhất trong toàn bộ 6 mô hình nghiên cứu! Trên tổng số 169 bài đánh giá rác thực tế, mô hình đã **bắt trúng tới 160 bài, chỉ bỏ sót duy nhất 9 bài rác ($FN = 9$)**.
   - Mặc dù Precision có phần giảm nhẹ (76.92% do có 48 ca báo nhầm $FP = 48$), điểm **F1-Score Spam vẫn đạt tới 84.88%** và Accuracy đạt 94.09%.
   - Trong các hệ thống thương mại điện tử có chính sách kiểm duyệt nghiêm ngặt (Zero Tolerance for Spam) — nơi tiêu chí hàng đầu là "thà báo nhầm còn hơn bỏ sót lừa đảo" — mô hình Linear SVM + BoW chính là giải pháp tối ưu số 1 để triển khai ở tuyến đầu.
3. **Linear SVM trên TF-IDF:**
   Đạt hiệu năng tương đương với BoW: **Recall 93.49%**, **Accuracy 93.57%**, **F1-Score 83.60%**. Trọng số $C = 1.0$ kết hợp `class_weight='balanced'` đã kích hoạt cơ chế phạt nặng lỗi bỏ sót spam, giúp LinearSVC tận dụng tối đa các đặc trưng có giá trị IDF cao.

---

### 3.3.3. So sánh tổng hợp và phân tích hiệu năng giữa các phương pháp

#### 1. Bảng đối sánh tổng thể 6 mô hình thực nghiệm

*Bảng 3.11: Bảng so sánh tổng hợp hiệu năng phân loại của toàn bộ 6 mô hình thực nghiệm trên tập Test (sắp xếp theo thứ tự giảm dần của F1-Score Spam).*

| Thứ hạng | Mô hình thuật toán | Bộ đặc trưng | Accuracy | Precision (Spam) | Recall (Spam) | F1-Score (Spam) | F1 Macro | ROC-AUC | PR-AUC | Đánh giá tổng quan |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| 🥇 **1** | **RBF SVM** | **Word2Vec (WE)**| **95.85%** | **86.86%** | 89.94% | **88.37%** | **92.92%** | **0.9859** | **0.9265** | **Tốt nhất toàn diện, cân bằng tối ưu** |
| 🥈 **2** | **Linear SVM** | BoW | 94.09% | 76.92% | **94.67%** | 84.88% | 90.60% | 0.9793 | 0.8674 | **Recall cao nhất (chỉ sót 9 spam)** |
| 🥉 **3** | **Linear SVM** | TF-IDF | 93.57% | 75.60% | 93.49% | 83.60% | 89.80% | 0.9772 | 0.8579 | Hiệu năng cao, quét sạch spam |
| 4 | **MultinomialNB**| BoW | 93.36% | 83.02% | 78.11% | 80.49% | 88.24% | 0.9769 | 0.8839 | Rất nhanh, ít báo nhầm ($FP=27$) |
| 5 | **ComplementNB** | TF-IDF | 93.05% | 81.10% | 78.70% | 79.88% | 87.84% | 0.9765 | 0.8926 | Ổn định trên dữ liệu lệch lớp |
| 6 | **GaussianNB** | Word2Vec (WE)| 83.20% | 51.41% | 75.74% | 61.24% | 75.26% | 0.8966 | 0.5870 | Thấp nhất, vi phạm giả định độc lập |

---

[CHÈN HÌNH 3.8 TẠI ĐÂY: Biểu đồ cột đối sánh các chỉ số hiệu năng chính (Accuracy, Precision, Recall, F1-Spam, ROC-AUC, PR-AUC) giữa 6 mô hình]
*(Placeholder: /assets/images/hinh3_8_bieu_do_doi_sanh_hieu_nang.png - Kích thước khuyến nghị: 15cm x 8cm, căn giữa)*

---

#### 2. Phân tích sự đánh đổi giữa Precision và Recall (Precision-Recall Trade-off)
Một phát hiện mang tính quy luật rõ rệt khi quan sát kết quả thực nghiệm là sự đánh đổi kinh điển giữa Precision và Recall:
- **Nhóm mô hình SVM tuyến tính (Linear SVM trên BoW/TF-IDF):** Có xu hướng thiên mạnh về **Recall** (Recall đạt xấp xỉ 93.5% - 94.7%, trong khi Precision ở mức 75.6% - 76.9%). Điều này là hệ quả trực tiếp của việc cấu hình `class_weight='balanced'`, khiến thuật toán thà chấp nhận mở rộng diện nghi vấn (tăng FP) chứ dứt khoát không để lọt bất kỳ dấu hiệu spam nào (giảm FN).
- **Nhóm mô hình Naive Bayes xác suất (MNB / CNB):** Có xu hướng thiên về **Precision** (Precision đạt 81.1% - 83.0%, nhưng Recall bị hạn chế ở mức ~78.1% - 78.7%). Naive Bayes chỉ đưa ra quyết định dự đoán spam khi các bằng chứng xác suất tích lũy là rất áp đảo, do đó số lượng ca báo nhầm rất ít ($FP \approx 27 - 31$), nhưng lại bỏ sót khá nhiều bài spam ngụy trang khéo léo ($FN \approx 36 - 37$).
- **Mô hình RBF SVM trên Word2Vec:** Đạt được trạng thái **cân bằng hoàn hảo (Harmonious Balance)**: Precision đạt tới 86.86% và Recall đạt tới 89.94%. Đây là bằng chứng cho thấy việc kết hợp biểu diễn ngữ nghĩa liên tục với hàm nhân phi tuyến giúp mô hình vừa "tinh tế" trong việc không làm phiền khách hàng chân chính, vừa "sắc bén" trong việc triệt phá các hành vi gian lận.

#### 3. Đánh giá hiệu năng tính toán và dung lượng lưu trữ (Computational Efficiency)

*Bảng 3.12: Đánh giá hiệu năng tính toán và dung lượng lưu trữ của các mô hình thực nghiệm.*

| Mô hình thuật toán | Bộ đặc trưng | Thời gian huấn luyện lại (Train Time) | Thời gian dự đoán tập Test (964 mẫu) | Thời gian suy luận trung bình / 1 mẫu | Dung lượng file mô hình (.pkl) |
| :--- | :--- | :---: | :---: | :---: | :---: |
| **MultinomialNB** | BoW | **3.8 ms** | **0.62 ms** | **0.64 µs / mẫu** | 352 KB |
| **ComplementNB** | TF-IDF | **2.5 ms** | **0.42 ms** | **0.44 µs / mẫu** | 441 KB |
| **GaussianNB** | Word2Vec | 4.0 ms | 0.94 ms | 0.97 µs / mẫu | **2.4 KB** |
| **Linear SVM** | BoW | 58.0 ms | 0.45 ms | **0.47 µs / mẫu** | 88 KB |
| **Linear SVM** | TF-IDF | 15.9 ms | 0.77 ms | 0.80 µs / mẫu | 88 KB |
| **RBF SVM** | Word2Vec | 198.8 ms | 57.08 ms | 59.21 µs / mẫu | 814 KB |

---

[CHÈN HÌNH 3.9 TẠI ĐÂY: Đồ thị tương quan giữa thời gian huấn luyện và hiệu năng F1-Score của các mô hình thực nghiệm]
*(Placeholder: /assets/images/hinh3_9_tuong_quan_thoi_gian_f1.png - Kích thước khuyến nghị: 14cm x 7cm, căn giữa)*

---

*Nhận định về hiệu năng vận hành thực tế:*
- **Tốc độ suy luận siêu tốc (Ultra-fast Inference Latency):**
  - Các mô hình tuyến tính (Linear SVM, MultinomialNB, ComplementNB) chỉ mất từ **0.44 đến 0.80 micro-giây (µs)** để phân loại xong một bài đánh giá. Tốc độ này tương đương với năng lực xử lý hơn **1.2 triệu đến 2.2 triệu đánh giá mỗi giây** trên một luồng CPU đơn lẻ!
  - Mô hình phức tạp nhất là RBF SVM trên Word2Vec cũng chỉ mất **59.2 micro-giây** cho mỗi mẫu (tương đương tốc độ xử lý khoảng **17,000 bài đánh giá / giây**).
- **Dung lượng lưu trữ siêu nhẹ:** File trọng số mô hình `.pkl` chỉ chiếm từ vài chục KB đến tối đa 814 KB, cho phép tích hợp trực tiếp vào bộ nhớ RAM của bất kỳ vi dịch vụ (Microservice) hoặc thiết bị biên (Edge Device) nào mà không gây áp lực về hạ tầng.

---

#### 4. Phân tích định tính các ca phân loại sai (Qualitative Error Analysis)
Để hiểu sâu sắc cơ chế hoạt động và những giới hạn cố hữu của các mô hình học máy, nhóm tác giả đã tiến hành phân tích chi tiết các file nhật ký lỗi sai (`results/<model>_errors.csv`):

##### A. Phân tích các trường hợp Dương tính giả (False Positives - Ham bị báo nhầm là Spam)
Đây là các trường hợp khách hàng thực sự mua hàng và để lại đánh giá thật, nhưng mô hình lại dự đoán là Spam ($y = 0, \hat{y} = 1$). Bảng 3.13 phân tích các trường hợp tiêu biểu:

*Bảng 3.13: Phân tích định tính các ví dụ thực tế bị phân loại sai dạng Dương tính giả (False Positives).*

| Nội dung đánh giá thực tế (`review`) | Nhãn gốc ($y$) | Dự đoán ($\hat{y}$) | Điểm số quyết định | Mô hình mắc lỗi | Phân tích nguyên nhân kỹ thuật |
| :--- | :---: | :---: | :---: | :--- | :--- |
| `"tốt, tiện thấy ok"` | 0 (Ham) | 1 (Spam) | +0.096 | RBF SVM (WE) | Câu quá ngắn, chỉ chứa các từ khen sáo rỗng (`tốt`, `ok`). Trong không gian Word2Vec, vector trung bình của câu này rơi vào vùng lân cận dày đặc của các bình luận spam seeding khen ảo. |
| `"tiếng máy chạy ồn"` | 0 (Ham) | 1 (Spam) | +0.152 | RBF SVM (WE) & Linear SVM | Chứa từ `"ồn"` và câu cụt lủn không có chủ ngữ/vị ngữ, mang cấu trúc cú pháp tương đồng với các câu spam phàn nàn chê bai ảo. |
| `"Sài oce"` | 0 (Ham) | 1 (Spam) | +0.317 | RBF SVM (WE) | Chứa biến thể teencode dị biệt (`oce` thay vì `ok`). Từ `oce` là từ ngoài từ điển (OOV) hoặc vector không chuẩn, kết hợp độ dài quá ngắn khiến mô hình nghi ngờ tính chân thực. |
| `"Tuyệt vời ông Mặt Trời"` | 0 (Ham) | 1 (Spam) | +0.698 | Linear SVM (BoW) | Câu cảm thán thành ngữ mạng mang tính chất phóng đại (Hyperbolic praise). Các bài spam seeding thường dùng ngôn từ hoa mỹ thái quá này. |
| `"sử dụng tốt diệt khuẩn tốt"` | 0 (Ham) | 1 (Spam) | +0.997 | MultinomialNB (BoW) | Lặp lại từ `"tốt"` 2 lần trong câu ngắn 6 từ. Tần suất từ `"tốt"` tăng đột biến khiến xác suất hậu nghiệm $P(\text{spam} \mid x)$ vọt lên mức cực đại. |
| `"Nhan vien dể thuong"` | 0 (Ham) | 1 (Spam) | +0.978 | MultinomialNB (BoW) | Viết sai chính tả (`dể thuong` thay vì `dễ thương`), không đề cập đến thông số kỹ thuật sản phẩm điện máy mà nhận xét về con người, bị bộ lọc túi từ nghi ngờ là bình luận lạc đề. |

##### B. Phân tích các trường hợp Âm tính giả (False Negatives - Spam bị bỏ sót thành Ham)
Đây là các trường hợp nguy hiểm: bài nhận xét là rác hoặc seeding lừa đảo nhưng mô hình lại bỏ qua và coi là hợp lệ ($y = 1, \hat{y} = 0$). Bảng 3.14 phân tích các trường hợp tiêu biểu:

*Bảng 3.14: Phân tích định tính các ví dụ thực tế bị phân loại sai dạng Âm tính giả (False Negatives).*

| Nội dung đánh giá thực tế (`review`) | Nhãn gốc ($y$) | Dự đoán ($\hat{y}$) | Điểm số quyết định | Mô hình mắc lỗi | Phân tích nguyên nhân kỹ thuật |
| :--- | :---: | :---: | :---: | :--- | :--- |
| `"Tot"` | 1 (Spam) | 0 (Ham) | -0.602 | RBF SVM (WE) | Câu viết hoa chữ cái đầu, không dấu, cực ngắn. Sau khi qua pipeline thành `tot`, từ này có tần suất xuất hiện ở cả hai lớp nhưng trọng số thiên về phản hồi tích cực ngắn, mô hình không đủ bằng chứng quy kết là spam. |
| `"Ok . Qua tuyệt vời"` | 1 (Spam) | 0 (Ham) | -0.073 | RBF SVM (WE) | Spam tinh vi ngụy trang dưới dạng lời khen tích cực ("Qua tuyệt vời"). Nếu không có thông tin siêu dữ liệu người dùng (User ID, IP), văn bản hoàn toàn giống một đánh giá 5 sao hợp lệ. |
| `"Mmmmmm"` | 1 (Spam) | 0 (Ham) | -0.286 | RBF SVM (WE) | Sau khi qua biểu thức chính quy rút gọn ký tự lặp `(\w)\1{2,}`, chuỗi biến thành một ký tự đơn `m`. Token đơn lẻ này không nằm trong vùng phân tách của RBF SVM, dẫn đến việc bị phán đoán nhầm sang nhãn đa số (Ham). |
| `"Chất lượng tốt"` | 1 (Spam) | 0 (Ham) | -0.188 | Linear SVM (BoW) | Đây là câu đánh giá mẫu mặc định (Template review) trên Shopee. Bản thân cụm từ mang nghĩa tích cực chuẩn mực, thuật toán túi từ không thể phát hiện được ý đồ seeding nếu chỉ nhìn vào 2 từ đơn lẻ này. |
| `"ukm"` | 1 (Spam) | 0 (Ham) | +0.175 (ngưỡng 0.5)| MultinomialNB (BoW) | Từ cảm thán đồng thuận teencode (`ukm` = `ừ`). Từ này xuất hiện rải rác ở cả hai lớp trong tập Train, xác suất có điều kiện không đủ lệch về phía Spam để vượt qua ngưỡng quyết định 0.5. |

---

## 3.4. Kết luận và hướng phát triển

### 3.4.1. Kết quả đạt được

Đề tài bài tập lớn đã hoàn thành trọn vẹn toàn bộ các mục tiêu nghiên cứu và yêu cầu kỹ thuật đề ra ban đầu, với các đóng góp cụ thể:
1. **Xây dựng thành công Pipeline tiền xử lý văn bản tiếng Việt chuẩn mực và giải quyết triệt để rủi ro rò rỉ dữ liệu:**
   - Đã hiện thực hóa quy trình chuẩn hóa Unicode NFC, trừu tượng hóa các thực thể nhạy cảm (`urltoken`, `phonetoken`, `numtoken`), xử lý ký tự lặp, tách dấu câu và giải mã từ điển teencode gồm hơn 30 quy tắc đặc thù ngành thương mại điện tử.
   - Phát hiện hiện tượng 55.7% dòng trùng lặp trong dữ liệu thô và giải quyết bài toán chống rò rỉ dữ liệu (Anti-Data Leakage) bằng thuật toán Majority Voting kết hợp loại bỏ trùng lặp trước khi chia phân tầng Train/Test 80/20.
2. **Khảo sát hệ thống 3 không gian biểu diễn văn bản:** Hiện thực hóa thành công không gian rời rạc thưa BoW (11,004 chiều), TF-IDF với sublinear scaling và chuẩn hóa L2, và không gian liên tục dày đặc Word2Vec Skip-gram (100 chiều) với kỹ thuật Pooling câu.
3. **Thực nghiệm toàn diện 6 cấu hình mô hình học máy:**
   - Mô hình **RBF SVM trên Word2Vec** đạt quán quân toàn diện với **F1-Score Spam đạt 88.37%**, **Accuracy đạt 95.85%**, **ROC-AUC đạt 0.9859**, **PR-AUC đạt 0.9265**, duy trì sự cân bằng tối ưu giữa Precision (86.86%) và Recall (89.94%).
   - Mô hình **Linear SVM trên Bag-of-Words** đạt độ nhạy vượt trội với **Recall lên tới 94.67%** (chỉ bỏ sót 9 trên tổng số 169 câu spam).
   - Làm sáng tỏ nguyên nhân lý thuyết khiến **Gaussian Naive Bayes trên Word2Vec thất bại (F1 chỉ đạt 61.24%)** do vi phạm nghiêm trọng giả định độc lập có điều kiện.
4. **Tối ưu hóa hiệu năng tính toán:** Toàn bộ các mô hình có thời gian suy luận siêu tốc (từ 0.4 µs đến 59 µs / mẫu), dung lượng lưu trữ dưới 1 MB, hoàn toàn sẵn sàng triển khai thực tế trên hạ tầng CPU tiết kiệm chi phí.

---

### 3.4.2. Ưu, nhược điểm của phương pháp

#### 1. Ưu điểm nổi bật
- **Tính thực tiễn và khả thi cao (High Practical Feasibility):** Mô hình không đòi hỏi GPU đắt đỏ, tiêu tốn cực ít RAM, tốc độ xử lý hàng chục nghìn đến hàng triệu câu mỗi giây, dễ dàng tích hợp vào hệ thống backend của các sàn TMĐT.
- **Tính minh bạch và khả năng giải thích (Interpretability):** Với các mô hình tuyến tính (Linear SVM, MNB), kỹ sư có thể dễ dàng trích xuất các trọng số đặc trưng lớn nhất để giải thích lý do tại sao một bình luận bị đánh dấu là spam.
- **Tính toàn vẹn khoa học (Methodological Rigor):** Quy trình kiểm thử độc lập, phân tầng, khử trùng lặp và đóng gói Pipeline chuẩn mực bảo đảm kết quả đạt được là hoàn toàn khách quan, không bị thổi phồng ảo bởi data leakage.

#### 2. Nhược điểm và hạn chế tồn đọng
- **Bỏ qua cấu trúc trật tự ngữ pháp phức tạp:** Các phương pháp BoW và TF-IDF coi văn bản là túi từ độc lập, không hiểu được mối liên kết phụ thuộc xa giữa các mệnh đề trong câu dài.
- **Hạn chế của mô hình Word2Vec nội bộ:** Mô hình Word2Vec được huấn luyện trên tập dữ liệu tương đối khiêm tốn (3,856 câu), do đó vốn từ vựng chưa thực sự phong phú và chưa nắm bắt được hết các từ hiếm ngoài miền dữ liệu điện máy.
- **Bất lực trước các đánh giá spam ngụy trang ngữ nghĩa tinh vi:** Các câu khen ngợi chung chung ngắn (*"Ok tốt"*, *"Ngon"*) nhưng được gán nhãn spam do hành vi seeding không thể phân biệt được nếu chỉ dựa thuần túy vào nội dung câu chữ mà không có siêu dữ liệu người dùng.

---

### 3.4.3. Hướng phát triển trong tương lai

Từ những kết quả và hạn chế đã đúc rút, nhóm tác giả đề xuất 4 định hướng nghiên cứu và phát triển mở rộng trong tương lai:

1. **Ứng dụng các Mô hình Ngôn ngữ Tiền huấn luyện chuyên sâu (Pre-trained Transformers):**
   - Tinh chỉnh (Fine-tuning) mô hình **PhoBERT** (Nguyen & Nguyen, 2020) hoặc **ViDeBERTa** trên bài toán phân loại đánh giá rác.
   - Nhờ được tiền huấn luyện trên hàng chục triệu câu tiếng Việt, PhoBERT có khả năng phân tích ngữ cảnh hai chiều sâu sắc, hứa hẹn sẽ giải quyết tốt các bài spam ngắn ngụy trang tinh vi.
2. **Mô hình hóa đa phương thức kết hợp Siêu dữ liệu (Multimodal & Metadata Fusion):**
   - Kết hợp nội dung văn bản đánh giá với các đặc trưng hành vi người dùng (Reviewer Metadata): số lượng đơn hàng đã mua, thời gian từ lúc nhận hàng đến lúc đánh giá, độ lệch giữa số sao đánh giá và cảm xúc văn bản (Rating-Text Inconsistency), địa chỉ IP, và tần suất gửi bình luận trong một khoảng thời gian.
3. **Cơ chế Học chủ động và Tái huấn luyện liên tục (Active Learning & Continuous Retraining):**
   - Xây dựng vòng lặp phản hồi (Feedback Loop): Các bình luận có điểm xác suất dự đoán nằm gần ranh giới quyết định (Uncertain Samples, ví dụ xác suất $0.45 - 0.55$) sẽ được tự động đẩy về cho chuyên viên kiểm duyệt của sàn dán nhãn thủ công, sau đó tái huấn luyện mô hình định kỳ hàng tuần để liên tục cập nhật các từ lóng và biến thể spam mới.
4. **Đóng gói Microservice thời gian thực với FastAPI và Kubernetes:**
   - Xây dựng API RESTful thời gian thực bằng FastAPI, đóng gói Docker Container hoàn chỉnh và triển khai trên cụm máy chủ Kubernetes, cung cấp dịch vụ lọc bình luận rác có độ trễ dưới 5 mili-giây cho các nền tảng thương mại điện tử quy mô lớn.

\newpage

# TÀI LIỆU THAM KHẢO

### TIẾNG VIỆT
1. **Nguyễn Hải Triều, Nguyễn Văn Kiệt, Nguyễn Gia Hưng, & Ngô Bá Tường** (2018). *Xây dựng kho ngữ liệu và đánh giá các mô hình học máy cho bài toán phân tích cảm xúc phản hồi của sinh viên (UIT-VSFC)*. Tạp chí Phát triển Khoa học và Công nghệ - Đại học Quốc gia TP.HCM, Tập 21, Số 4, tr. 45-56.
2. **Phạm Quang Nhật Minh, Lê Hồng Phương, & Nguyễn Thị Minh Huyền** (2014). *Nghiên cứu các phương pháp trích chọn đặc trưng trong phân loại văn bản tiếng Việt*. Kỷ yếu Hội thảo Quốc gia lần thứ XVII về Xử lý Ngôn ngữ Tự nhiên và Khai phá Tri thức (VAKLY 2014), tr. 112-120.
3. **Đinh Điền** (2005). *Xử lý Ngôn ngữ Tự nhiên: Giáo trình chuyên đề Sau đại học*. Nhà xuất bản Đại học Quốc gia TP. Hồ Chí Minh.
4. **Trần Văn Lăng, & Nguyễn Thị Thúy Loan** (2019). *Máy vector hỗ trợ (SVM) và ứng dụng trong khai phá dữ liệu văn bản tiếng Việt*. Nhà xuất bản Khoa học và Kỹ thuật, Hà Nội.
5. **Hiệp hội Thương mại Điện tử Việt Nam (VECOM)** (2024). *Báo cáo Chỉ số Thương mại Điện tử Việt Nam 2024 (E-Business Index 2024)*. Nhà xuất bản Thông tin và Truyền thông, Hà Nội.

---

### TIẾNG ANH
6. **Jindal, N., & Liu, B.** (2007). *Analyzing and detecting review spam*. In *Proceedings of the 7th IEEE International Conference on Data Mining (ICDM 2007)* (pp. 547-552). IEEE. DOI: [10.1109/ICDM.2007.68](https://doi.org/10.1109/ICDM.2007.68).
7. **Jindal, N., & Liu, B.** (2008). *Opinion spam and analysis*. In *Proceedings of the 2008 International Conference on Web Search and Data Mining (WSDM '08)* (pp. 219-230). ACM. DOI: [10.1145/1341531.1341560](https://doi.org/10.1145/1341531.1341560).
8. **Ott, M., Choi, Y., Cardie, C., & Hancock, J. T.** (2011). *Finding deceptive opinion spam by any stretch of the imagination*. In *Proceedings of the 49th Annual Meeting of the Association for Computational Linguistics: Human Language Technologies (ACL 2011)* (pp. 309-319). Association for Computational Linguistics.
9. **Crawford, M., Khoshgoftaar, T. M., Prusa, J. D., Richter, A. N., & Najafabadi, M. M.** (2015). *Survey of review spam detection using machine learning techniques*. *Journal of Big Data*, 2(1), 1-24. DOI: [10.1186/s40537-015-0029-9](https://doi.org/10.1186/s40537-015-0029-9).
10. **Heydari, A., Tavakoli, M. A., Salim, N., & Heydari, Z.** (2015). *Detection of review spam: A review*. *Information Processing & Management*, 51(4), 363-380.
11. **Mikolov, T., Chen, K., Corrado, G., & Dean, J.** (2013). *Efficient estimation of word representations in vector space*. *arXiv preprint arXiv:1301.3781*.
12. **Mikolov, T., Sutskever, I., Chen, K., Corrado, G. S., & Dean, J.** (2013). *Distributed representations of words and phrases and their compositionality*. In *Advances in Neural Information Processing Systems (NeurIPS 2013)* (Vol. 26, pp. 3111-3119).
13. **Cortes, C., & Vapnik, V.** (1995). *Support-vector networks*. *Machine Learning*, 20(3), 273-297. DOI: [10.1007/BF00994018](https://doi.org/10.1007/BF00994018).
14. **Rennie, J. D., Shih, L., Teevan, J., & Karger, D. R.** (2003). *Tackling the poor assumptions of naive bayes text classifiers*. In *Proceedings of the 20th International Conference on Machine Learning (ICML 2003)* (pp. 616-623).
15. **Salton, G., & Buckley, C.** (1988). *Term-weighting approaches in automatic text retrieval*. *Information Processing & Management*, 24(5), 513-523.
16. **Pedregosa, F., Varoquaux, G., Gramfort, A., Michel, V., Thirion, B., Grisel, O., ... & Duchesnay, É.** (2011). *Scikit-learn: Machine learning in Python*. *Journal of Machine Learning Research*, 12, 2825-2830.
17. **Řehůřek, R., & Sojka, P.** (2010). *Software framework for topic modelling with large corpora*. In *Proceedings of the LREC 2010 Workshop on New Challenges for NLP Frameworks* (pp. 45-50).
18. **Nguyen, D. Q., & Nguyen, A. T.** (2020). *PhoBERT: Pre-trained language models for Vietnamese*. In *Findings of the Association for Computational Linguistics: EMNLP 2020* (pp. 1037-1042). Association for Computational Linguistics.
19. **Sun, C., Du, J., & Xing, L.** (2019). *A deep learning approach to review spam detection with word embeddings and behavioral features*. *IEEE Access*, 7, 182390-182400.
20. **Fawcett, T.** (2006). *An introduction to ROC analysis*. *Pattern Recognition Letters*, 27(8), 861-874.
21. **Saito, T., & Rehmsmeier, M.** (2015). *The precision-recall plot is more informative than the ROC plot when evaluating imbalanced datasets*. *PLoS ONE*, 10(3), e0118432.
22. **Devlin, J., Chang, M. W., Lee, K., & Toutanova, K.** (2019). *BERT: Pre-training of deep bidirectional transformers for language understanding*. In *Proceedings of NAACL-HLT 2019* (pp. 4171-4186).
23. **Cover, T. M.** (1965). *Geometrical and statistical properties of systems of linear inequalities with applications in pattern recognition*. *IEEE Transactions on Electronic Computers*, EC-14(3), 326-334.
24. **Harris, Z. S.** (1954). *Distributional structure*. *Word*, 10(2-3), 146-162.
25. **Manning, C. D., Raghavan, P., & Schütze, H.** (2008). *Introduction to Information Retrieval*. Cambridge University Press.

\newpage

---

# PHỤ LỤC

---

### PHỤ LỤC A: HƯỚNG DẪN ĐÓNG GÓI VÀ TRIỂN KHAI HỆ THỐNG VỚI DOCKER

Để bảo đảm tính khả chuyển, dễ dàng cài đặt trên bất kỳ môi trường máy chủ Linux/Windows/macOS nào mà không gặp xung đột về phiên bản thư viện, toàn bộ hệ thống đã được đóng gói dưới dạng container chuẩn Docker.

#### 1. Cấu hình tệp `Dockerfile`
```dockerfile
FROM python:3.11-slim

WORKDIR /app

# Nâng cấp pip và cài đặt các phụ thuộc bắt buộc
COPY requirements.txt .
RUN pip install --upgrade pip && \
    pip install -r requirements.txt && \
    pip install matplotlib scipy joblib

# Sao chép toàn bộ mã nguồn vào container
COPY . .

CMD ["bash"]
```

#### 2. Các lệnh biên dịch và thực thi hệ thống
```bash
# Bước 1: Xây dựng Docker Image từ thư mục gốc dự án
docker build -t nlp-n2-ptit .

# Bước 2: Chạy Docker Container ở chế độ tương tác (Interactive), mount thư mục để lưu kết quả
docker run -it --rm \
  -v $(pwd)/data:/app/data \
  -v $(pwd)/results:/app/results \
  -v $(pwd)/feature_extraction/features:/app/feature_extraction/features \
  nlp-n2-ptit bash

# Bước 3: Thực thi tuần tự toàn bộ quy trình bên trong Container
# 3.1. Tiền xử lý dữ liệu và chia tập Train/Test chống rò rỉ dữ liệu
python preprocess/preprocess.py --input data/raw/reviews_spam_ham_filtered_augmented.csv

# 3.2. Trích chọn 3 bộ đặc trưng (BoW, TF-IDF, Word2Vec)
python feature_extraction/bow.py
python feature_extraction/tfidf.py
python feature_extraction/WE.py

# 3.3. Huấn luyện và đánh giá 6 mô hình học máy
python model/nb-bow.py
python model/nb-tfidf.py
python model/nb-we.py
python model/svm-bow.py
python model/svm-tfidf.py
python model/svm-we.py
```

---

### PHỤ LỤC B: CẤU TRÚC MÃ NGUỒN CHI TIẾT CỦA DỰ ÁN

Toàn bộ cây thư mục mã nguồn và dữ liệu của dự án được tổ chức khoa học theo mô hình module hóa như sau:

```text
nlp-n2-ptit/
├── Dockerfile                                      # Cấu hình containerization triển khai
├── requirements.txt                                # Danh sách các thư viện Python phụ thuộc
├── README.md                                       # Tài liệu hướng dẫn cài đặt và sử dụng nhanh
├── run.sh                                          # Shell script tự động hóa chạy toàn bộ quy trình
│
├── data/
│   ├── raw/                                        # Thư mục lưu trữ dữ liệu thô gốc
│   │   ├── reviews_spam_ham_chuan.csv              # Dữ liệu gốc 10,892 mẫu
│   │   └── reviews_spam_ham_filtered_augmented.csv # Dữ liệu thô đã lọc bổ sung
│   └── processed/                                  # Thư mục lưu dữ liệu sạch sau tiền xử lý
│       └── processed.csv                           # 4,820 mẫu độc nhất (3,856 train, 964 test)
│
├── preprocess/
│   └── preprocess.py                               # Script làm sạch Unicode, teencode, khử trùng, chia train/test
│
├── feature_extraction/
│   ├── bow.py                                      # Module trích chọn đặc trưng Bag-of-Words (n-gram 1-2)
│   ├── tfidf.py                                    # Module trích chọn đặc trưng TF-IDF (sublinear, L2 norm)
│   ├── WE.py                                       # Module huấn luyện Word2Vec Skip-gram và Pooling vector câu
│   └── features/                                   # Thư mục lưu trữ ma trận và mô hình trích chọn (.pkl, .model)
│       ├── bow.pkl, bow_vectorizer.pkl
│       ├── tfidf.pkl, tfidf_vectorizer.pkl
│       └── we.pkl, we_word2vec.model
│
├── model/
│   ├── evaluate.py                                 # Module khung: 5-Fold Stratified CV, đánh giá và ghi log
│   ├── nb-bow.py                                   # Thực nghiệm Multinomial Naive Bayes + BoW
│   ├── nb-tfidf.py                                 # Thực nghiệm Complement Naive Bayes + TF-IDF
│   ├── nb-we.py                                    # Thực nghiệm Gaussian Naive Bayes + Word Embedding
│   ├── svm-bow.py                                  # Thực nghiệm Linear SVM + BoW
│   ├── svm-tfidf.py                                # Thực nghiệm Linear SVM + TF-IDF
│   └── svm-we.py                                   # Thực nghiệm RBF Kernel SVM (Pipeline Scaler) + Word2Vec
│
└── results/                                        # Kết quả đầu ra và báo cáo thực nghiệm
    ├── summary.csv                                 # Bảng tổng hợp các chỉ số hiệu năng 6 mô hình
    ├── <model>.json                                # File JSON lưu chi tiết metrics và ma trận nhầm lẫn
    ├── <model>.pkl                                 # File lưu trữ trọng số mô hình tốt nhất đã huấn luyện
    ├── <model>_confusion_matrix.png               # Hình ảnh biểu đồ nhiệt ma trận nhầm lẫn
    └── <model>_errors.csv                          # Danh sách các câu bị dự đoán sai kèm điểm số quyết định
```

---

### PHỤ LỤC C: BẢNG TỔNG HỢP KHÔNG GIAN TÌM KIẾM SIÊU THAM SỐ TRONG GRIDSEARCHCV

*Bảng C.1: Chi tiết không gian siêu tham số và kết quả tìm kiếm tối ưu bằng 5-Fold Stratified Cross-Validation trên tập Train.*

| Mã mô hình | Thuật toán nền tảng | Không gian đặc trưng | Các siêu tham số đưa vào lưới tìm kiếm (Param Grid) | Số tổ hợp thử nghiệm | Siêu tham số tối ưu tìm được (`best_params_`) | Điểm F1 Spam trung bình CV trên Train |
| :--- | :--- | :--- | :--- | :---: | :--- | :---: |
| `nb-bow` | MultinomialNB | Bag of Words (11,004 chiều) | `alpha`: `[0.001, 0.003, 0.01, 0.03, 0.1, 0.3, 1.0]` | 7 | `{"alpha": 0.003}` | $0.8019 \pm 0.018$ |
| `nb-tfidf` | Pipeline(MultinomialNB / ComplementNB) | TF-IDF (11,004 chiều) | `estimator`: `[MultinomialNB(), ComplementNB()]`<br>`alpha`: `[0.001, 0.003, 0.01, 0.03, 0.1, 0.3, 1.0]` | 14 | `{"nb": ComplementNB(), "nb__alpha": 0.001}` | $0.8108 \pm 0.014$ |
| `nb-we` | GaussianNB | Word2Vec (100 chiều) | `var_smoothing`: `np.logspace(-12, -1, 12)` ($10^{-12} \to 10^{-1}$) | 12 | `{"var_smoothing": 1e-12}` | $0.6032 \pm 0.021$ |
| `svm-bow` | LinearSVC | Bag of Words (11,004 chiều) | `C`: `[0.001, 0.01, 0.05, 0.1, 0.5, 1.0, 5.0]`<br>`class_weight`: `[None, 'balanced']` | 14 | `{"C": 0.5, "class_weight": None}` | $0.8414 \pm 0.012$ |
| `svm-tfidf` | LinearSVC | TF-IDF (11,004 chiều) | `C`: `[0.01, 0.05, 0.1, 0.5, 1.0, 5.0, 10.0]`<br>`class_weight`: `[None, 'balanced']` | 14 | `{"C": 1.0, "class_weight": "balanced"}` | $0.8377 \pm 0.015$ |
| `svm-we` | Pipeline(StandardScaler, SVC(RBF)) | Word2Vec (100 chiều) | `svm__C`: `[0.1, 1.0, 10.0, 100.0]`<br>`svm__gamma`: `['scale', 0.001, 0.01, 0.1]`<br>`svm__class_weight`: `[None, 'balanced']` | 32 | `{"svm__C": 10.0, "svm__class_weight": "balanced", "svm__gamma": "scale"}` | **0.8755 ± 0.009** |

---

<div align="center">
<b>--- HẾT BÁO CÁO BÀI TẬP LỚN ---</b>
</div>
