## TÓM TẮT ĐỀ TÀI
Sự bùng nổ của thương mại điện tử (TMĐT) tại Việt Nam trong những năm gần đây đã biến các đánh giá của người dùng (Customer Reviews) trở thành nguồn thông tin tối quan trọng, định hình hành vi mua sắm của người tiêu dùng và quyết định doanh số cũng như danh tiếng của các nhà bán lẻ. Tuy nhiên, tình trạng ô nhiễm thông tin do các "đánh giá rác" (Spam Reviews) — bao gồm các bình luận quảng cáo, lừa đảo, chèo kéo sang kênh cá nhân (Zalo, SĐT), tin nhắn vô nghĩa tích xu thưởng, hay các đánh giá giả mạo nhằm thao túng xếp hạng — đang gây ảnh hưởng nghiêm trọng tới trải nghiệm khách hàng và tính minh bạch của thị trường số. Việc phát hiện và sàng lọc tự động các đánh giá rác là một bài toán cấp thiết nhưng đối mặt với nhiều thách thức lớn: ngôn ngữ mạng tiếng Việt phi hình thức (teencode, viết tắt, từ lóng, biến thể ngữ âm), hiện tượng mất cân bằng lớp trầm trọng (Spam chỉ chiếm thiểu số), và đặc biệt là nguy cơ rò rỉ dữ liệu (Data Leakage) do người dùng thường xuyên để lại các bình luận ngắn trùng lặp ("Tốt", "Ok").

Báo cáo bài tập lớn này trình bày một nghiên cứu thực nghiệm toàn diện, có tính hệ thống cao về bài toán phân loại đánh giá rác tiếng Việt (Spam vs. Ham Reviews) trong lĩnh vực thiết bị điện máy gia dụng. Nhóm tác giả đã xây dựng một pipeline học máy chuẩn mực và khép kín từ khâu thu thập dữ liệu nguồn đến mô hình hóa hiện đại:
1. **Phân hệ thu thập dữ liệu tự động (Web Scraping Subsystem):** Thiết kế và hiện thực hóa công cụ cào dữ liệu chuyên dụng dựa trên Selenium WebDriver nhắm tới hệ sinh thái Điện Máy Xanh (`dienmayxanh.com`). Phân hệ tích hợp các kỹ thuật vượt rào cản chống bot (Anti-Bot Bypass: vô hiệu hóa Blink Automation, loại bỏ cờ tự động hóa, ghi đè thuộc tính JavaScript `navigator.webdriver`), hỗ trợ 2 chế độ cào thích ứng (phân trang `/danh-gia` và cuộn động "Xem thêm"), lọc trùng theo ID bình luận (`data-comment-id`) trực tiếp trong RAM, thu thập thành công 10,238 bài đánh giá khách hàng thực tế thuộc 10 ngành hàng điện máy gia dụng.
2. **Tiền xử lý nâng cao và chống rò rỉ thông tin:** Chuẩn hóa Unicode NFC, chuyển chữ thường, khử ký tự lặp cảm xúc, trừu tượng hóa các thực thể nhạy cảm (URL, Email, SĐT, Số tiền) thành các token đặc trưng (`urltoken`, `phonetoken`, `numtoken`), xây dựng từ điển giải mã teencode chuyên ngành, giải quyết triệt để 55.7% số câu ngắn trùng lặp trước khi phân chia tập dữ liệu phân tầng (Stratified Split 80/20) để đảm bảo tính khách quan tuyệt đối.
3. **Khảo sát đa không gian biểu diễn văn bản:** So sánh từ không gian vector thưa đa chiều (Bag-of-Words kết hợp n-gram 1-2, TF-IDF với sublinear scaling và chuẩn hóa L2 norm), không gian vector nhúng liên tục dày đặc (Word2Vec kiến trúc Skip-gram với kỹ thuật Pooling câu), đến không gian biểu diễn n-gram ký tự con hiện đại (Subword Character n-grams trong FastText).
4. **Mô hình hóa và đối sánh giữa Học máy truyền thống và Mô hình hiện đại:** Đánh giá 6 cấu hình mô hình học máy truyền thống gồm 3 biến thể Naive Bayes (MultinomialNB, ComplementNB, GaussianNB) và 2 cấu hình Máy vector hỗ trợ (Linear SVM và RBF SVM kết hợp StandardScaler và cân bằng trọng số lớp `class_weight='balanced'`), đồng thời đối sánh trực tiếp với **FastText** — một mô hình học máy hiện đại dạng mạng nơ-ron nông tích hợp thông tin n-gram ký tự con và n-gram từ.

Kết quả thực nghiệm trên tập kiểm thử độc lập (964 mẫu) chỉ ra rằng:
- **Mô hình hiện đại FastText** đạt thành tích **Quán quân toàn diện (Top 1)** với **Accuracy đạt 96.37% (0.9637)**, **F1-Score lớp Spam đạt 89.91% (0.8991)**, **PR-AUC đạt 0.9403**, và **F1 Macro đạt 93.85%**, vượt qua toàn bộ các mô hình học máy truyền thống. FastText thể hiện năng lực vượt trội trong việc giải quyết hiện tượng từ ngoài từ điển (Out-Of-Vocabulary - OOV), nhận diện biến thể teencode và lỗi chính tả tiếng Việt nhờ cơ chế n-gram ký tự con ($minn=2, maxn=5$) kết hợp n-gram từ (`wordNgrams=2`).
- Trong nhóm học máy truyền thống, mô hình **RBF SVM kết hợp Word2Vec (dense embedding)** đạt hiệu năng cao nhất với **F1-Score (Spam) đạt 88.37%**, **Accuracy đạt 95.85%**, **ROC-AUC đạt 0.9859**, và **PR-AUC đạt 0.9265**, duy trì độ cân bằng tối ưu giữa Precision (86.86%) và Recall (89.94%).
- Mô hình **Linear SVM kết hợp Bag-of-Words** thể hiện ưu thế vượt trội về độ nhạy phát hiện spam với **Recall đạt tới 94.67%** (chỉ bỏ sót 9 trên tổng số 169 mẫu spam), đạt **F1-Score 84.88%**.
- Ngược lại, **Gaussian Naive Bayes trên Word2Vec** thể hiện hiệu năng kém nhất (**F1-Score chỉ đạt 61.24%**) do vi phạm nghiêm trọng giả định độc lập có điều kiện giữa các chiều vector embedding.
- Toàn bộ các mô hình đề xuất đều có tốc độ suy luận cực nhanh (từ 0.4 µs đến 292 µs trên mỗi mẫu đánh giá trên CPU tiêu chuẩn mà không cần GPU), chứng minh tính khả thi vượt trội để triển khai vận hành thời gian thực tại các hệ thống thương mại điện tử thực tế.

**Từ khóa:** *Xử lý ngôn ngữ tự nhiên (NLP), Thu thập dữ liệu (Web Scraping), Selenium WebDriver, Phân loại đánh giá rác (Spam Reviews Detection), Tiếng Việt, Bag-of-Words, TF-IDF, Word2Vec, FastText, Subword Information, Naive Bayes, Support Vector Machine (SVM), Mất cân bằng dữ liệu, Rò rỉ dữ liệu.*

---


## MỤC LỤC
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
  - 1.2.3. Phương pháp dựa trên Học sâu và Mô hình hiện đại FastText
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
  - 2.2.4. Biểu diễn từ và phân loại văn bản hiện đại với FastText
- **2.3. Huấn luyện mô hình học máy cho bài toán phân loại**
  - 2.3.1. Mô hình phân loại xác suất Naive Bayes
  - 2.3.2. Mô hình Máy vector hỗ trợ - Support Vector Machine (SVM)
  - 2.3.3. Mô hình phân loại học máy hiện đại FastText
  - 2.3.4. Sơ đồ quy trình tổng thể (Pipeline) của hệ thống đề xuất

---

### **CHƯƠNG 3: THỰC NGHIỆM VÀ ĐÁNH GIÁ KẾT QUẢ**
- **3.1. Thu thập và xử lý dữ liệu thực nghiệm**
  - 3.1.1. Quy trình và kiến trúc thu thập dữ liệu tự động (Data Collection) từ Điện Máy Xanh
  - 3.1.2. Mô tả tập dữ liệu thực nghiệm chuẩn và phân bố thống kê
  - 3.1.3. Kỹ thuật lọc, tăng cường dữ liệu và kết quả sau tiền xử lý
- **3.2. Môi trường cài đặt và các độ đo đánh giá**
  - 3.2.1. Môi trường và công cụ triển khai thực nghiệm
  - 3.2.2. Các độ đo đánh giá (Accuracy, Precision, Recall, F1-Score, Confusion Matrix)
- **3.3. Kết quả thực nghiệm**
  - 3.3.1. Kết quả thực nghiệm với mô hình Naive Bayes (trên 3 bộ đặc trưng BoW, TF-IDF, Word2Vec)
  - 3.3.2. Kết quả thực nghiệm với mô hình SVM (trên 3 bộ đặc trưng BoW, TF-IDF, Word2Vec)
  - 3.3.3. Kết quả thực nghiệm với mô hình học máy hiện đại FastText
  - 3.3.4. So sánh tổng hợp và phân tích hiệu năng giữa tất cả các phương pháp
  - 3.3.5. Đánh giá hiệu năng tính toán và dung lượng lưu trữ
  - 3.3.6. Phân tích định tính các ca phân loại sai
- **3.4. Kết luận và hướng phát triển**
### **CHƯƠNG 4: Kết luận và hướng phát triển**
  - 4.1. Kết quả đạt được
  - 4.2. Ưu, nhược điểm của phương pháp
  - 4.3. Hướng phát triển trong tương lai

---

- **TÀI LIỆU THAM KHẢO**
- **PHỤ LỤC**
  - Phụ lục A: Bảng phân công nhiệm vụ từng thành viên

\newpage

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
| **FT** | FastText | Mô hình phân loại văn bản nhanh kết hợp n-gram ký tự con |
| **OOV** | Out-Of-Vocabulary | Hiện tượng từ ngoài từ điển vựng |
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
| **ROC-AUC** | Receiver Operating Characteristic - Area Under Curve | Diện tích dưới đường cong ROC |
| **SOTA** | State-of-the-Art | Hiệu năng tiên tiến / đỉnh cao |
| **SGD** | Stochastic Gradient Descent | Thuật toán hạ độ dốc ngẫu nhiên |
| **DOM** | Document Object Model | Mô hình đối tượng tài liệu HTML |
| **WAF** | Web Application Firewall | Tường lửa ứng dụng web |

\newpage

---

## DANH MỤC BẢNG BIỂU

- **Bảng 1.1:** Phân loại các dạng đánh giá rác (Spam Reviews) trên nền tảng thương mại điện tử.
- **Bảng 1.2:** So sánh tổng hợp các hướng tiếp cận phân loại văn bản (Rule-based, Học máy truyền thống, Mô hình hiện đại FastText, Học sâu Transformer).
- **Bảng 1.3:** Tổng hợp các công trình nghiên cứu tiêu biểu liên quan đến phát hiện đánh giá giả mạo và phân loại văn bản tiếng Việt.
- **Bảng 2.1:** Bảng ánh xạ chuẩn hóa viết tắt và teencode tiếng Việt trong thương mại điện tử.
- **Bảng 2.2:** So sánh các đặc tính không gian đặc trưng giữa BoW, TF-IDF, Word2Vec và FastText (Subword Embeddings).
- **Bảng 2.3:** Bảng tổng hợp các biến thể Naive Bayes và lý do lựa chọn cho từng loại không gian biểu diễn.
- **Bảng 3.1:** Cấu trúc trường thông tin (Schema) của thực thể đánh giá thu thập từ hệ thống Điện Máy Xanh.
- **Bảng 3.2:** Thống kê phân bố 10,238 bài đánh giá thô thu thập từ Điện Máy Xanh theo 10 danh mục sản phẩm.
- **Bảng 3.3:** Thống kê phân bố số lượng đánh giá theo 10 danh mục sản phẩm điện máy trong tập dữ liệu thực nghiệm chuẩn.
- **Bảng 3.4:** Thống kê phân bố số lượng đánh giá theo số sao (Rating) trong tập dữ liệu thực nghiệm.
- **Bảng 3.5:** Thống kê số lượng mẫu và tỷ lệ phân bố lớp trước và sau khi lọc trùng lặp.
- **Bảng 3.6:** Phân bố số lượng mẫu tập Train và Test sau khi phân chia phân tầng (Stratified 80/20).
- **Bảng 3.7:** Một số ví dụ cụ thể về câu đánh giá trước và sau khi thực hiện tiền xử lý làm sạch.
- **Bảng 3.8:** Ma trận nhầm lẫn tổng quát (Confusion Matrix) cho bài toán phân loại nhị phân Spam/Ham.
- **Bảng 3.9:** Kết quả thực nghiệm chi tiết của các biến thể mô hình Naive Bayes trên 3 bộ đặc trưng.
- **Bảng 3.10:** Ma trận nhầm lẫn chi tiết của 3 biến thể mô hình Naive Bayes trên tập Test.
- **Bảng 3.11:** Kết quả thực nghiệm chi tiết của các biến thể mô hình SVM trên 3 bộ đặc trưng.
- **Bảng 3.12:** Ma trận nhầm lẫn chi tiết của 3 biến thể mô hình SVM trên tập Test.
- **Bảng 3.13:** Kết quả thực nghiệm chi tiết của mô hình FastText trên tập Test Benchmark và tập cào mở rộng.
- **Bảng 3.14:** Ma trận nhầm lẫn chi tiết của mô hình FastText trên tập Test Benchmark (964 mẫu).
- **Bảng 3.15:** Bảng so sánh tổng hợp hiệu năng phân loại của toàn bộ 7 mô hình thực nghiệm trên tập Test (FastText + 6 mô hình ML truyền thống).
- **Bảng 3.16:** Đánh giá hiệu năng tính toán và dung lượng lưu trữ của các mô hình thực nghiệm (bao gồm FastText).
- **Bảng 3.17:** Phân tích định tính các ví dụ thực tế bị phân loại sai dạng Dương tính giả (False Positives - Ham bị báo nhầm là Spam).
- **Bảng 3.18:** Phân tích định tính các ví dụ thực tế bị phân loại sai dạng Âm tính giả (False Negatives - Spam bị bỏ sót thành Ham).

\newpage

---

## DANH MỤC HÌNH VẼ

- **Hình 0.1:** Logo Học viện Công nghệ Bưu chính Viễn thông (PTIT).
- **Hình 1.1:** Minh họa các dạng đánh giá rác (Spam reviews) điển hình trên các sàn thương mại điện tử Việt Nam.
- **Hình 2.1:** Quy trình chuẩn hóa và làm sạch văn bản tiếng Việt cho bài toán phân loại đánh giá.
- **Hình 2.2:** Minh họa trực quan không gian vector thưa trong mô hình Bag-of-Words (BoW).
- **Hình 2.3:** Đồ thị phân phối giá trị nghịch đảo tần suất văn bản (IDF) giữa các từ phổ biến và từ đặc trưng.
- **Hình 2.4:** Kiến trúc mạng nơ-ron Skip-gram trong mô hình Word2Vec.
- **Hình 2.5:** Cơ chế tìm siêu phẳng phân tách tối ưu và khoảng cách lề (Margin) trong Support Vector Machine.
- **Hình 2.6:** Kiến trúc mạng nơ-ron phân loại và cơ chế n-gram ký tự con trong mô hình FastText.
- **Hình 2.7:** Sơ đồ quy trình tổng thể (Pipeline) của hệ thống phân loại đánh giá rác đề xuất (tích hợp Data Collection và FastText).
- **Hình 3.1:** Kiến trúc module và luồng thu thập dữ liệu tự động với Selenium Crawler từ Điện Máy Xanh.
- **Hình 3.2:** Phân bố độ dài câu (số lượng token) trong tập dữ liệu sau bước làm sạch tiền xử lý.
- **Hình 3.3:** Ma trận nhầm lẫn (Confusion Matrix) của mô hình Multinomial Naive Bayes + Bag of Words (`results/nb-bow_confusion_matrix.png`).
- **Hình 3.4:** Ma trận nhầm lẫn (Confusion Matrix) của mô hình Complement Naive Bayes + TF-IDF (`results/nb-tfidf_confusion_matrix.png`).
- **Hình 3.5:** Ma trận nhầm lẫn (Confusion Matrix) của mô hình Gaussian Naive Bayes + Word Embedding (`results/nb-we_confusion_matrix.png`).
- **Hình 3.6:** Ma trận nhầm lẫn (Confusion Matrix) của mô hình Linear SVM + Bag of Words (`results/svm-bow_confusion_matrix.png`).
- **Hình 3.7:** Ma trận nhầm lẫn (Confusion Matrix) của mô hình Linear SVM + TF-IDF (`results/svm-tfidf_confusion_matrix.png`).
- **Hình 3.8:** Ma trận nhầm lẫn (Confusion Matrix) của mô hình RBF SVM + Word Embedding (`results/svm-we_confusion_matrix.png`).
- **Hình 3.9:** Ma trận nhầm lẫn (Confusion Matrix) của mô hình học máy hiện đại FastText (`results/fasttext_confusion_matrix.png`).
- **Hình 3.10:** Biểu đồ cột đối sánh các chỉ số hiệu năng chính (Accuracy, Precision, Recall, F1-Spam, ROC-AUC, PR-AUC) giữa 7 mô hình.
- **Hình 3.11:** Đồ thị tương quan giữa thời gian huấn luyện và hiệu năng F1-Score của các mô hình thực nghiệm.

\newpage

# CHƯƠNG 1: TỔNG QUAN

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

### 1.2.3. Phương pháp dựa trên Học sâu và Mô hình hiện đại FastText

Từ những năm 2015 trở lại đây, sự bùng nổ của Học sâu (Deep Learning) và đặc biệt là kiến trúc Transformer (Vaswani et al., 2017) cùng các mô hình mạng nơ-ron nhúng từ mở rộng như **FastText** (Bojanowski et al., 2017; Joulin et al., 2016) đã tái định hình toàn bộ lĩnh vực Xử lý Ngôn ngữ Tự nhiên.

#### 1. Cơ chế hoạt động của Học sâu truyền thống (Deep Neural Networks)
Học sâu cho phép mô hình tự động học các biểu diễn phân cấp (Hierarchical Representations) từ dữ liệu thô dạng chuỗi ký tự mà không cần trích xuất đặc trưng thủ công:
- **Mạng nơ-ron tích chập cho văn bản (TextCNN - Kim, 2014):** Sử dụng các bộ lọc tích chập (Convolutional Filters) có kích thước khác nhau trượt qua các vector từ nhúng để nắm bắt các cụm từ (Phrase-level features) then chốt.
- **Mạng nơ-ron hồi quy (RNN, LSTM, BiLSTM):** Xử lý văn bản như một chuỗi thời gian, ghi nhớ ngữ cảnh thông qua các trạng thái ẩn (Hidden States) và cổng nhớ (Gating Mechanisms), nắm bắt được sự phụ thuộc xa giữa các từ trong câu.
- **Mô hình ngôn ngữ tiền huấn luyện dựa trên Transformer (Pre-trained Language Models):**
  - Các mô hình dựa trên BERT (Devlin et al., 2018), RoBERTa (Liu et al., 2019) được tiền huấn luyện trên các kho ngữ liệu khổng lồ bằng các tác vụ như Masked Language Modeling (MLM).
  - Đối với tiếng Việt, các mô hình tiêu biểu gồm có **PhoBERT** (Nguyen & Nguyen, 2020) được huấn luyện trên 20GB văn bản tiếng Việt báo chí và Wikipedia, **ViDeBERTa**, hay **mBERT**.
  - Người nghiên cứu chỉ cần tinh chỉnh (Fine-tuning) thêm một tầng phân loại (Classification Head) trên tập dữ liệu đánh giá rác là có thể đạt được độ hiểu ngữ nghĩa sâu sắc.

#### 2. Mô hình hiện đại FastText — Cầu nối đột phá giữa Học máy và Mạng nơ-ron
Nhận thấy các mô hình học sâu sâu tầng (Deep Neural Networks) đòi hỏi chi phí tính toán khổng lồ và độ trễ suy luận lớn, nhóm nghiên cứu tại Facebook AI Research (FAIR) do Joulin, Bojanowski và Mikolov dẫn đầu đã đề xuất **FastText** (2016, 2017) như một giải pháp dung hòa hoàn hảo:
- **Kiến trúc mạng nơ-ron nông (Shallow Neural Network):** FastText chỉ sử dụng một tầng ẩn tuyến tính duy nhất kết hợp cơ chế gộp trung bình (Average Pooling) các vector từ/ký tự con, sau đó trực tiếp đưa vào hàm kích hoạt Softmax hoặc Hierarchical Softmax. Kiến trúc này loại bỏ hoàn toàn các phép biến đổi phi tuyến nhiều tầng phức tạp, giúp tốc độ huấn luyện nhanh gấp hàng trăm lần so với CNN hay LSTM.
- **Biểu diễn n-gram ký tự con (Subword Information):** Đột phá quan trọng nhất của FastText là xem mỗi từ như một tập hợp các n-gram ký tự (character n-grams) có độ dài từ $n_{min}$ đến $n_{max}$. Vector của một từ được tổng hợp từ tổng các vector của các n-gram ký tự con cấu thành. Nhờ đó, FastText giải quyết triệt để vấn đề từ ngoài từ điển (Out-Of-Vocabulary - OOV) và nắm bắt xuất sắc các hiện tượng hình thái, từ ghép, lỗi gõ sai chính tả và teencode trong thương mại điện tử tiếng Việt.
- **Tích hợp n-gram từ (Word n-grams):** FastText tự động kết hợp các cặp từ liền kề (bi-grams) vào không gian phân loại thông qua kỹ thuật băm (Hashing trick), giúp mô hình nắm bắt trật tự cú pháp và cụm từ phủ định (`không lạnh`, `quá tệ`) tương tự như mạng nơ-ron phức tạp.

#### 3. Bảng đối sánh tổng hợp giữa các hướng tiếp cận

*Bảng 1.2: So sánh tổng hợp các hướng tiếp cận phân loại văn bản.*

| Tiêu chí so sánh | Dựa trên luật & Từ điển | Học máy truyền thống (ML) | Mô hình hiện đại FastText | Học sâu & Transformer (DL) |
| :--- | :--- | :--- | :--- | :--- |
| **Bản chất trích xuất đặc trưng** | Thủ công (Regex, Blacklist) | Thủ công rời rạc (BoW, TF-IDF) hoặc WE tĩnh | Tự động hóa qua Subword & Word n-grams | Tự động hóa qua các tầng Transformer |
| **Xử lý từ mới (OOV) & Teencode** | Kém, phụ thuộc từ điển luật | Rất kém (gán `<UNK>` hoặc bỏ qua) | **Xuất sắc (nhờ subword n-grams)** | Tốt (nhờ BPE / WordPiece) |
| **Yêu cầu dữ liệu gán nhãn** | Không cần | Vừa phải (vài nghìn mẫu) | Vừa phải (vài nghìn mẫu) | Lớn (hoặc cần Pre-trained models) |
| **Yêu cầu phần cứng** | CPU cơ bản | CPU cơ bản, RAM thấp | **CPU cơ bản (không cần GPU)** | Yêu cầu máy chủ GPU mạnh |
| **Thời gian huấn luyện** | 0 giây | Rất nhanh (vài giây đến vài phút) | **Siêu nhanh (vài giây đến chục giây)** | Chậm (nhiều giờ đến nhiều ngày) |
| **Thời gian suy luận / mẫu** | $pprox 0.1 - 1$ µs | $pprox 0.4 - 60$ µs | **$pprox 50 - 300$ µs (Cực nhanh)** | $pprox 1,000 - 50,000$ µs |
| **Khả năng giải thích quyết định** | Tường minh 100% | Rất cao (trọng số đặc trưng) | Khá cao (trọng số n-gram nổi bật) | Rất thấp (Hộp đen nơ-ron sâu) |
| **Khả năng tổng quát hóa** | Kém, dễ bị lách luật | Khá tốt | **Rất tốt trên dữ liệu nhiễu/teencode** | Xuất sắc |
| **Khả năng triển khai thực tế** | Rất dễ, nhưng khó duy trì | Rất dễ, chi phí thấp, tối ưu cao | **Tối ưu toàn diện, triển khai siêu nhẹ** | Phức tạp, chi phí máy chủ cao |

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


4. **Các nghiên cứu về kỹ thuật n-gram ký tự con và mô hình FastText:**
   - **Joulin et al. (2016)** tại Facebook AI Research đã công bố công trình kinh điển *"Bag of Tricks for Efficient Text Classification"*, chứng minh rằng một mạng nơ-ron nông tuyến tính kết hợp biểu diễn n-gram từ và thuật toán tối ưu hóa phân cấp có thể đạt độ chính xác tương đương với các mô hình học sâu phức tạp (như Char-CNN, VDCNN) nhưng với tốc độ huấn luyện nhanh hơn từ hàng trăm đến hàng nghìn lần.
   - **Bojanowski et al. (2017)** trong nghiên cứu *"Enriching Word Vectors with Subword Information"* đã phát triển cơ chế nhúng từ dựa trên n-gram ký tự (Character n-grams), giải quyết triệt để điểm yếu của Word2Vec trước các ngôn ngữ biến hình và các kho ngữ liệu phi chuẩn (nhiều lỗi chính tả, từ lóng trên mạng xã hội).
   - Tại Việt Nam, nhiều nghiên cứu ứng dụng FastText trong bài toán phân tích quan điểm (Sentiment Analysis) và phân loại ý định người dùng (Intent Detection) đã khẳng định tính ưu việt của FastText khi đối phó với hiện tượng teencode, viết tắt và lỗi chính tả tiếng Việt so với các mô hình Word2Vec truyền thống.

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
1. **Thiết kế và hiện thực hóa phân hệ tự động thu thập dữ liệu (Automated Web Scraping Subsystem):**
   - Xây dựng công cụ thu thập tự động dựa trên Selenium WebDriver nhắm tới hệ sinh thái bán lẻ Điện Máy Xanh (`dienmayxanh.com`).
   - Cài đặt các cơ chế phòng chống phát hiện bot (Anti-Bot Bypass: vô hiệu hóa Blink Automation, ghi đè biến điều hướng `navigator.webdriver`, hỗ trợ mô hình Human-in-the-Loop vượt CAPTCHA).
   - Tự động hóa 2 chế độ cào linh hoạt: cào đa trang phân tầng (`/danh-gia`) và cào cuộn động 1 trang ("Xem thêm"), kết hợp cơ chế chống trùng lặp theo ID bài đánh giá (`data-comment-id`) trực tiếp trong bộ nhớ RAM, thu thập kho ngữ liệu thực tế hơn 10.200 bài đánh giá.
2. **Xây dựng Pipeline tiền xử lý văn bản tiếng Việt chuyên sâu và chống rò rỉ dữ liệu:**
   - Xây dựng quy trình làm sạch chuẩn mực: chuẩn hóa Unicode NFC, chuyển đổi chữ thường, khử ký tự lặp cảm xúc, trừu tượng hóa các thực thể nhạy cảm (URL, Email, SĐT, Số tiền) thành các token khái quát (`urltoken`, `phonetoken`, `numtoken`).
   - Xây dựng từ điển chuẩn hóa Teencode / viết tắt đặc thù cho thương mại điện tử Việt Nam.
   - Hiện thực hóa thuật toán xử lý mâu thuẫn nhãn bằng biểu quyết đa số (Majority Voting) và khử trùng lặp triệt để trước khi phân chia dữ liệu, bảo đảm tính độc lập tuyệt đối giữa tập huấn luyện và kiểm thử.
3. **Khảo sát đa không gian biểu diễn văn bản:**
   - Không gian rời rạc thưa: Túi từ (Bag of Words - BoW) kết hợp n-gram range (1, 2) và Trọng số TF-IDF kết hợp kỹ thuật nén logarithm (sublinear TF scaling) và chuẩn hóa vector L2 norm.
   - Không gian liên tục dày đặc: Nhúng từ (Word2Vec) với kiến trúc Skip-gram và kỹ thuật tổng hợp vector câu (Document Vector Pooling).
   - Không gian biểu diễn n-gram ký tự con hiện đại: Tích hợp thông tin ký tự con (Subword Information) và n-gram từ thông qua FastText.
4. **Cài đặt, tối ưu hóa và thực nghiệm đối sánh giữa Học máy truyền thống và Mô hình hiện đại:**
   - Khảo sát 3 biến thể xác suất Naive Bayes: Multinomial Naive Bayes (trên BoW), Complement Naive Bayes (trên TF-IDF), và Gaussian Naive Bayes (trên Word2Vec).
   - Khảo sát 2 cấu hình Máy vector hỗ trợ (SVM): Linear SVM (trên BoW và TF-IDF) và Kernel RBF SVM kết hợp bộ chuẩn hóa StandardScaler và kỹ thuật cân bằng trọng số lớp (`class_weight='balanced'`) trên Word2Vec.
   - Nghiên cứu và huấn luyện mô hình học máy hiện đại **FastText** (mạng nơ-ron nông tích hợp subword và word n-grams), thực hiện đối sánh đa chiều về hiệu năng phân loại, độ trễ suy luận và khả năng kháng lỗi chính tả / teencode.
   - Tối ưu hóa siêu tham số bằng kỹ thuật 5-Fold Stratified Cross-Validation chỉ thực hiện trên tập huấn luyện.
5. **Đánh giá toàn diện và phân tích chuyên sâu:**
   - Đo lường hiệu năng thông qua hệ thống 7 chỉ số khoa học: Accuracy, Precision (Spam), Recall (Spam), F1-Score (Spam), Macro F1, ROC-AUC, và PR-AUC.
   - Phân tích định tính các trường hợp phân loại sai (False Positives, False Negatives) để làm sáng tỏ cơ chế hoạt động của từng mô hình và rút ra các khuyến nghị thực tiễn cho bài toán triển khai thực tế.

### 1.4.2. Phạm vi nghiên cứu
Để bảo đảm tính tập trung và khả thi của đề tài trong khuôn khổ môn học Xử lý Ngôn ngữ Tự nhiên, phạm vi nghiên cứu được xác định cụ thể như sau:

- **Về miền dữ liệu (Domain):** Đề tài tập trung nghiên cứu trên tập dữ liệu đánh giá sản phẩm điện tử tiêu dùng và thiết bị điện máy gia dụng tại Việt Nam (bao gồm 10 danh mục sản phẩm chính: *Tủ lạnh, Nồi cơm điện, Điều hòa, Máy giặt, Tivi, Máy lọc nước, Máy lọc không khí, Máy sấy quần áo, Camera giám sát, và Khác*) thu thập từ hệ thống bán lẻ Điện Máy Xanh và các sàn thương mại điện tử lớn với gần 200 dòng sản phẩm riêng biệt và đầy đủ các thang đo từ 1 sao đến 5 sao.
- **Về không gian nhãn:** Bài toán được định dạng là bài toán **Phân loại nhị phân (Binary Classification)** với hai lớp: Nhãn 1 là **Spam** (đánh giá rác, quảng cáo, chèo kéo, lừa đảo, vô nghĩa) và Nhãn 0 là **Ham** (đánh giá hợp lệ, trải nghiệm thật của khách hàng).
- **Về mặt công nghệ và thuật toán:** Đề tài nghiên cứu sâu vào các phương pháp học máy truyền thống (Naive Bayes, SVM) kết hợp với các kỹ thuật biểu diễn vector nền tảng, đồng thời mở rộng nghiên cứu sang **mô hình học máy hiện đại FastText** (mạng nơ-ron nông dựa trên subword n-grams). Đề tài không sử dụng các mô hình ngôn ngữ lớn (LLMs) cồng kềnh nhằm duy trì mục tiêu xây dựng một hệ thống có tốc độ suy luận siêu tốc (Micro-seconds), tiết kiệm tài nguyên và khả năng đóng gói triển khai microservice nhẹ nhàng trên hạ tầng CPU thông thường.

\newpage

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

### 2.2.4. Biểu diễn từ và phân loại văn bản hiện đại với FastText

#### 1. Đặt vấn đề và Hạn chế của các mô hình vector từ truyền thống
Mô hình Word2Vec (Mikolov et al., 2013) xem mỗi từ như một đơn vị nguyên tử độc lập (Atomic Entity) và gán cho mỗi từ trong từ điển một vector riêng biệt $\mathbf{v}_w \in \mathbb{R}^d$. Cách tiếp cận này bộc lộ hai điểm yếu chí mạng khi áp dụng vào ngôn ngữ thương mại điện tử tiếng Việt:
1. **Bất lực trước hiện tượng Từ ngoài từ điển (Out-Of-Vocabulary - OOV):**
   Nếu một từ không xuất hiện trong tập huấn luyện (do người dùng gõ sai chính tả như *"mays"*, *"đẹppp"*, viết tắt teencode *"k00"*, *"chẹp"*, hoặc từ ghép mới), Word2Vec buộc phải gán vector mặc định bằng $0$ hoặc ký hiệu rỗng `<UNK>`, khiến toàn bộ thông tin ngữ nghĩa của từ đó bị xóa sạch.
2. **Bỏ qua cấu trúc hình thái nội tại của từ ngữ:**
   Trong tiếng Việt, các từ láy và từ ghép chia sẻ chung các âm tiết gốc mang ý nghĩa tương đồng (ví dụ: *"sạch sẽ"*, *"máy móc"*, *"xịn sò"*). Tuy nhiên, Word2Vec xử lý chúng như các vector hoàn toàn độc lập, không tận dụng được sự tương đồng về mặt hình thái và ngữ âm.

#### 2. Nguyên lý n-gram ký tự con (Character n-grams / Subword Information)
Để giải quyết triệt để hai hạn chế trên, Bojanowski et al. (2017) tại Facebook AI Research đã phát triển mô hình **FastText**, mở rộng kiến trúc Skip-gram bằng cách nhúng trực tiếp thông tin các **n-gram ký tự con (Subwords)**:
- **Ký tự ranh giới đặc biệt:** Mỗi từ $w$ được bao bọc bởi hai ký tự biên đặc biệt là `<` (bắt đầu) và `>` (kết thúc) để phân biệt tiền tố, hậu tố và chính từ gốc.
- **Tập hợp n-gram ký tự con:** Một từ $w$ được biểu diễn như một túi các n-gram ký tự có độ dài từ $n_{min}$ đến $n_{max}$, đồng thời bổ sung chính chuỗi đầy đủ `<w>` vào tập hợp:
  $$\mathcal{G}_w \subset \{1, 2, \dots, G\}$$
- **Ví dụ minh họa cụ thể với tiếng Việt:**
  Giả sử từ gốc là $w = 	ext{"máy"}$ với cấu hình $n_{min} = 2, n_{max} = 3$:
  - Khi thêm ký tự biên, từ trở thành chuỗi: `<máy>`
  - Các n-gram ký tự độ dài $n=2$: `<m`, `má`, `áy`, `y>`
  - Các n-gram ký tự độ dài $n=3$: `<má`, `máy`, `áy>`
  - Chuỗi đặc biệt đại diện cho chính từ: `<máy>`
  - Tập hợp $\mathcal{G}_{	ext{máy}} = \{ 	ext{<m}, 	ext{má}, 	ext{áy}, 	ext{y>}, 	ext{<má}, 	ext{máy}, 	ext{áy>}, 	ext{<máy>} \}$

#### 3. Công thức toán học biểu diễn vector từ FastText
Mỗi n-gram ký tự $g \in \mathcal{G}_w$ được ánh xạ tới một vector embedding riêng biệt $\mathbf{z}_g \in \mathbb{R}^d$. Vector biểu diễn cuối cùng của từ $w$ được tính bằng **tổng của toàn bộ các vector n-gram ký tự con** cấu thành nên nó:
$$\mathbf{v}_w = \sum_{g \in \mathcal{G}_w} \mathbf{z}_g$$

*Cơ chế giải quyết OOV thần kỳ:*
Khi gặp một từ hoàn toàn mới chưa từng xuất hiện trong tập huấn luyện (ví dụ người dùng gõ nhầm *"mays"* hoặc teencode *"đẹpp"*):
- FastText phân tách từ mới này thành các n-gram: `<m`, `ma`, `ay`, `ys`, `s>`, `<may`, `ays`, `ys>`...
- Vì các n-gram con như `<m`, `ma`, `ay` đã từng xuất hiện trong các từ huấn luyện khác (như *"máy"*, *"may"*), mô hình vẫn tra cứu được các vector $\mathbf{z}_g$ tương ứng.
- Bằng cách cộng tổng các vector n-gram đã biết, FastText tự động nội suy ra một vector ngữ nghĩa xấp xỉ vô cùng chính xác cho từ mới mà không bao giờ gặp lỗi OOV!

#### 4. Kỹ thuật băm không gian đặc trưng (Hashing Trick with Buckets)
Do số lượng n-gram ký tự có thể bùng nổ lên tới hàng trăm triệu chuỗi khác nhau, FastText áp dụng kỹ thuật băm **Fowler-Noll-Vo (FNV-1a Hash)** để ánh xạ mọi chuỗi n-gram vào một bảng băm có kích thước cố định gồm $K$ phần tử (buckets, trong đề tài chọn $K = 50,000$ buckets):
$$	ext{bucket\_id}(g) = 	ext{hash}(g) \pmod K$$
Nhờ bảng băm cố định, mô hình FastText kiểm soát dung lượng bộ nhớ cực kỳ nhỏ gọn, không phụ thuộc vào quy mô phát sinh của từ vựng ngoài từ điển.

---

#### 5. Bảng đối sánh 4 không gian đặc trưng văn bản

*Bảng 2.2: So sánh các đặc tính không gian đặc trưng giữa BoW, TF-IDF, Word2Vec và FastText (Subword Embeddings).*

| Tiêu chí kỹ thuật | Túi từ (Bag of Words) | Trọng số TF-IDF | Word2Vec (Skip-gram) | FastText (Subword Embeddings) |
| :--- | :--- | :--- | :--- | :--- |
| **Bản chất biểu diễn** | Tần số xuất hiện rời rạc | Tần số nhân nghịch đảo văn bản | Vector ngữ nghĩa liên tục (Dense) | Vector ngữ nghĩa liên tục đa mức độ |
| **Đơn vị biểu diễn** | Token (Từ / Cụm từ) | Token (Từ / Cụm từ) | Từ đơn lẻ nguyên tử (Atomic Word) | **Túi n-gram ký tự con + n-gram từ** |
| **Kích thước chiều không gian** | Rất lớn (11,004 chiều) | Rất lớn (11,004 chiều) | Nhỏ gọn ($d = 100$ chiều) | **Nhỏ gọn ($d = 50$ chiều)** |
| **Tính chất ma trận dữ liệu** | Thưa nghiêm trọng (Sparsity > 99%)| Thưa nghiêm trọng (Sparsity > 99%)| Dày đặc hoàn toàn (Dense Matrix) | **Dày đặc hoàn toàn (Dense Matrix)** |
| **Khả năng nắm bắt ngữ nghĩa** | Không (Chỉ dựa vào mặt chữ) | Không (Chỉ dựa vào mặt chữ) | Rất tốt (Khoảng cách Cosine) | **Xuất sắc cả ngữ nghĩa lẫn hình thái** |
| **Xử lý từ ngoài từ điển (OOV)**| Hoàn toàn bỏ qua | Hoàn toàn bỏ qua | Gán vector 0 / `<UNK>` | **Nội suy chính xác qua subword n-grams** |
| **Kháng nhiễu Teencode & Lỗi chính tả** | Kém (Mỗi lỗi tạo 1 cột thưa mới)| Kém (Lỗi chính tả bị phạt điểm IDF)| Rất kém (Tạo vector UNK rỗng) | **Xuất sắc (Chia sẻ subword với từ chuẩn)**|
| **Yêu cầu tài nguyên bộ nhớ** | Nhẹ (Lưu trữ ma trận `csr_matrix`)| Nhẹ (Lưu trữ ma trận `csr_matrix`)| Trung bình (Lưu ma trận từ nhúng) | **Rất nhẹ (Bảng băm 50,000 buckets)** |

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

### 2.3.3. Mô hình phân loại học máy hiện đại FastText

Bên cạnh các mô hình học máy truyền thống (Naive Bayes và Support Vector Machine) hoạt động trên các vector đặc trưng cố định được trích xuất từ trước, đề tài cài đặt và thực nghiệm **FastText Classifier** (Joulin et al., 2016) — một mô hình học máy hiện đại dạng mạng nơ-ron nông (Shallow Neural Network) có khả năng **học biểu diễn đặc trưng và tối ưu hóa ranh giới phân loại đồng thời (End-to-End Joint Learning)**.

#### 1. Kiến trúc mạng nơ-ron nông phân loại văn bản nhanh
Kiến trúc của FastText Classifier được tinh giản tối đa để đạt tốc độ xử lý siêu tốc nhưng vẫn bảo tồn khả năng phân biệt mạnh mẽ:
1. **Tầng vào (Input Layer):**
   Văn bản đánh giá $D$ gồm chuỗi các từ $\{w_1, w_2, \dots, w_N\}$. Mỗi từ $w_i$ được biểu diễn bởi tập hợp các n-gram ký tự con $\mathcal{G}_{w_i}$ và chính từ đó. Đồng thời, mô hình tích hợp thêm các **n-gram từ (Word n-grams)** bậc 2 (`wordNgrams=2`).
2. **Tầng ẩn tuyến tính (Linear Hidden Layer):**
   Thay vì sử dụng các hàm kích hoạt phi tuyến đắt đỏ (như ReLU, Sigmoid hay cơ chế Self-Attention trong Transformer), FastText thực hiện phép chiếu tuyến tính và **gộp trung bình (Average Pooling)** trên toàn bộ các vector từ và vector n-gram ký tự cấu thành văn bản:
   $$\mathbf{x}_D = rac{1}{|V_D|} \sum_{v \in V_D} \mathbf{e}_v$$
   trong đó $V_D$ là tập hợp toàn bộ các n-gram ký tự và n-gram từ xuất hiện trong bài đánh giá $D$, còn $\mathbf{e}_v \in \mathbb{R}^d$ là vector nhúng của phần tử $v$.
3. **Tầng ra phân loại (Output Classification Layer):**
   Vector biểu diễn văn bản $\mathbf{x}_D \in \mathbb{R}^d$ được nhân trực tiếp với ma trận trọng số phân loại $\mathbf{W} \in \mathbb{R}^{C 	imes d}$ để sinh ra phân phối xác suất trên hai lớp (Spam vs. Ham) thông qua hàm Softmax:
   $$P(y = c | \mathbf{x}_D) = rac{\exp(\mathbf{w}_c^	op \mathbf{x}_D + b_c)}{\sum_{k=1}^C \exp(\mathbf{w}_k^	op \mathbf{x}_D + b_k)}$$
   trong đó $C=2$ (nhị phân), $\mathbf{w}_c$ là vector trọng số của lớp $c$, và $b_c$ là hệ số điều chỉnh (bias).

---

[CHÈN HÌNH 2.6 TẠI ĐÂY: Kiến trúc mạng nơ-ron phân loại và cơ chế n-gram ký tự con trong mô hình FastText]
*(Placeholder: /assets/images/hinh2_6_fasttext_architecture.png - Kích thước khuyến nghị: 14cm x 8cm, căn giữa)*

---

#### 2. Kết hợp n-gram từ (Word n-grams) và Kỹ thuật Hashing
Điểm vượt trội của FastText so với mô hình BoW thông thường nằm ở tham số `wordNgrams=2`:
- Khi $wordNgrams=1$, mô hình coi các từ độc lập, bỏ qua trật tự cú pháp (tương tự túi từ).
- Khi kích hoạt $wordNgrams=2$, FastText tự động học thêm các cặp từ đi liền nhau. Ví dụ: câu *"máy không lạnh"* sẽ sinh ra các đặc trưng bi-gram là `"máy_không"` và `"không_lạnh"`. Điều này cho phép FastText phân biệt rạch ròi giữa *"không lạnh"* (phàn nàn của khách hàng) và *"lạnh"* (khen ngợi).
- Để tránh hiện tượng bùng nổ số lượng tham số khi kết hợp cả n-gram từ và n-gram ký tự, FastText sử dụng chung bảng băm $K = 50,000$ buckets. Nhờ đó, hàng triệu tổ hợp n-gram được nén gọn gàng vào không gian tham số cố định.

#### 3. Hàm mục tiêu và Thuật toán tối ưu hóa
Hàm mục tiêu của mô hình phân loại FastText là tối thiểu hóa hàm mất mát mất mát entropy chéo nhị phân (Binary Cross-Entropy Loss) trên toàn bộ tập dữ liệu huấn luyện:
$$\mathcal{L}(\Theta) = - rac{1}{M} \sum_{i=1}^M \left[ y_i \log P(y_i = 1 | \mathbf{x}_{D_i}) + (1 - y_i) \log (1 - P(y_i = 1 | \mathbf{x}_{D_i})) 
ight]$$
trong đó $\Theta = \{\mathbf{E}, \mathbf{W}, \mathbf{b}\}$ là toàn bộ không gian tham số cần tối ưu hóa.

FastText sử dụng thuật toán **Hạ độ dốc ngẫu nhiên không đồng bộ (Asynchronous Stochastic Gradient Descent - Hogwild SGD)**. Thuật toán này cho phép cập nhật song song các trọng số trên nhiều lõi CPU mà không cần khóa bộ nhớ (Lock-free), mang lại tốc độ huấn luyện phi thường: xử lý hàng trăm nghìn mẫu văn bản chỉ trong vài giây.

#### 4. Cấu hình siêu tham số tối ưu cho bài toán phân loại đánh giá rác
Qua các bước thử nghiệm và đánh giá thực nghiệm trên dữ liệu đánh giá tiếng Việt, cấu hình siêu tham số tối ưu của FastText được thiết lập như sau:
- Tốc độ học (Learning Rate): `lr = 0.3`.
- Số lượng Epoch huấn luyện: `epoch = 35`.
- Số chiều vector nhúng: `dim = 50`.
- Bậc n-gram từ: `wordNgrams = 2` (nắm bắt cụm 2 từ liền kề).
- Dải n-gram ký tự con: `minn = 2, maxn = 5` (nắm bắt từ 2 đến 5 ký tự liên tiếp).
- Số lượng Buckets băm: `bucket = 50,000`.
- Tần số xuất hiện tối thiểu của từ: `minCount = 1` (giữ lại cả các từ hiếm và biến thể teencode để phục vụ subword).
- Hàm mất mát tầng ra: `loss = 'softmax'`.

---

### 2.3.4. Sơ đồ quy trình tổng thể (Pipeline) của hệ thống đề xuất

Toàn bộ kiến trúc và luồng xử lý dữ liệu của hệ thống phân loại đánh giá rác đề xuất — tích hợp từ phân hệ thu thập dữ liệu tự động, tiền xử lý chống rò rỉ, đến hai luồng phân loại học máy truyền thống và học máy hiện đại FastText — được mô tả tổng hợp qua sơ đồ kiến trúc khối tại **Hình 2.7**:

```
+---------------------------------------------------------------------------------+
|               1. PHÂN HỆ THU THẬP DỮ LIỆU TỰ ĐỘNG (WEB SCRAPING)                |
|  - Nền tảng: Hệ thống bán lẻ Điện Máy Xanh (dienmayxanh.com)                    |
|  - Công cụ: Selenium WebDriver (Chrome) + Kỹ thuật vượt rào cản Anti-Bot Bypass |
|  - 2 chế độ cào: Phân trang (/danh-gia) và Cuộn động Xem thêm (Infinite Scroll) |
|  - Chống trùng lặp theo ID đánh giá (data-comment-id) thời gian thực trong RAM  |
|  - Kết quả: 10,238 đánh giá thực tế từ 10 ngành hàng -> data/raw/               |
+---------------------------------------------------------------------------------+
                                         |
                                         v
+---------------------------------------------------------------------------------+
|                  2. TIỀN XỬ LÝ VĂN BẢN & CHỐNG RÒ RỈ DỮ LIỆU                    |
|  - Chuẩn hóa Unicode NFC, chuyển chữ thường (lowercase)                         |
|  - Thay URL -> urltoken, Email -> emailtoken, SĐT -> phonetoken                 |
|  - Thay số/tiền -> numtoken, rút gọn ký tự lặp, tách dấu câu                    |
|  - Chuẩn hóa Teencode & từ viết tắt theo từ điển chuyên ngành TMĐT              |
|  - Biểu quyết đa số (Majority Voting) cho các câu mâu thuẫn nhãn                |
|  - KHỬ TRÙNG LẶP TRIỆT ĐỂ: 10,892 -> 4,820 câu độc nhất (loại 55.7%)            |
|  - Phân chia phân tầng 80/20: Train (3,856 mẫu) | Test (964 mẫu)                |
+---------------------------------------------------------------------------------+
                                         |
                    +--------------------+--------------------+
                    |                                         |
                    v                                         v
+---------------------------------------+ +---------------------------------------+
| 3A. TRÍCH CHỌN ĐẶC TRƯNG HỌC MÁY (ML) | | 3B. MÔ HÌNH HỌC MÁY HIỆN ĐẠI FASTTEXT |
| (Fit bộ vectorizer CHỈ TRÊN TẬP TRAIN)| | (End-to-End Joint Feature & Classifier|
| - [BoW]: CountVectorizer(ngram=(1,2)) | | - Character n-grams (minn=2, maxn=5)  |
|   -> 11,004 features                  | |   xóa bỏ hoàn toàn hiện tượng OOV     |
| - [TF-IDF]: TfidfVectorizer(sublinear)| | - Word n-grams (wordNgrams=2)         |
|   -> 11,004 features                  | |   nắm bắt ngữ cảnh cụm từ phủ định    |
| - [WE]: Word2Vec Skip-gram(dim=100)   | | - Hashing Trick: 50,000 buckets       |
|   + Sentence Mean Pooling -> 100 dims | | - Shallow Neural Net + Softmax Loss   |
+---------------------------------------+ +---------------------------------------+
                    |                                         |
                    v                                         v
+---------------------------------------+ +---------------------------------------+
| 4A. HUẤN LUYỆN ML TRUYỀN THỐNG        | | 4B. HUẤN LUYỆN FASTTEXT               |
| - 5-Fold Stratified Cross-Validation  | | - Huấn luyện đa luồng Asynchronous SGD|
| - Tiêu chí tối ưu: F1-Score lớp Spam  | | - lr=0.3, epoch=35, dim=50, loss=sm   |
| - Dò siêu tham số cho 6 mô hình:      | | - Thời gian huấn luyện: ~18 giây      |
|   * MultinomialNB + BoW               | +---------------------------------------+
|   * ComplementNB + TF-IDF             |                     |
|   * GaussianNB + Word2Vec             |                     |
|   * Linear SVM + BoW                  |                     |
|   * Linear SVM + TF-IDF               |                     |
|   * RBF SVM (Pipeline Scaler) + WE    |                     |
+---------------------------------------+                     |
                    |                                         |
                    +--------------------+--------------------+
                                         |
                                         v
+---------------------------------------------------------------------------------+
|             5. KIỂM THỬ ĐỘC LẬP TRÊN TẬP TEST CHUNG (964 MẪU)                   |
|  - Kiểm thử đồng nhất không rò rỉ dữ liệu cho toàn bộ 7 mô hình                 |
|  - Đánh giá 7 chỉ số: Accuracy, Precision, Recall, F1-Spam, Macro-F1, ROC, PR   |
|  - Xuất ma trận nhầm lẫn (PNG) và file nhật ký lỗi sai (errors.csv)             |
|  - Cập nhật tự động bảng đối sánh tổng hợp vào results/summary.csv              |
+---------------------------------------------------------------------------------+
```

---

[CHÈN HÌNH 2.7 TẠI ĐÂY: Sơ đồ quy trình tổng thể (Pipeline) của hệ thống phân loại đánh giá rác đề xuất]
*(Placeholder: /assets/images/hinh2_7_pipeline_tong_the.png - Kích thước khuyến nghị: 15cm x 11cm, căn giữa)*

---

*Nguyên tắc thiết kế bất biến của Pipeline:* Toàn bộ các bộ chuyển đổi vector (`CountVectorizer`, `TfidfVectorizer`), mô hình `Word2Vec`, bộ chuẩn hóa `StandardScaler` và mô hình `FastText` **chỉ được phép gọi hàm `.fit()` hoặc huấn luyện duy nhất trên tập Train**. Tập Test hoàn toàn đóng vai trò là dữ liệu "chưa từng nhìn thấy" (Unseen Data) và chỉ được thực hiện phép biến đổi chiếu hoặc dự đoán (`.predict()`). Bất kỳ sự vi phạm nào đối với nguyên tắc này đều cấu thành lỗi rò rỉ thông tin trong học máy.

\newpage

# CHƯƠNG 3: THỰC NGHIỆM VÀ ĐÁNH GIÁ KẾT QUẢ

Chương 3 trình bày toàn bộ quá trình thu thập, xử lý dữ liệu thực nghiệm, thiết lập môi trường kỹ thuật, định nghĩa các độ đo khoa học, và đặc biệt là phân tích chuyên sâu các kết quả thực nghiệm đạt được từ 6 cấu hình mô hình học máy trên tập kiểm thử độc lập. Mọi số liệu, bảng biểu và ma trận nhầm lẫn trong chương này được trích xuất trực tiếp từ các file nhật ký thực nghiệm trong thư mục `results/` của dự án.

---

## 3.1. Thu thập và xử lý dữ liệu thực nghiệm

### 3.1.1. Quy trình và kiến trúc thu thập dữ liệu tự động (Data Collection) từ Điện Máy Xanh

#### 1. Đặt vấn đề và Nhu cầu thu thập dữ liệu thực tế tại Việt Nam
Trong các bài toán Xử lý Ngôn ngữ Tự nhiên ứng dụng cho thương mại điện tử, chất lượng và tính đại diện của tập dữ liệu huấn luyện đóng vai trò sống còn. Các bộ dữ liệu dịch máy hoặc dữ liệu mẫu giả lập thường đánh mất những nét ngữ dụng đặc thù của người tiêu dùng Việt Nam: từ lóng, teencode, viết tắt địa phương, lỗi chính tả vô ý, cũng như các chiêu trò spam seeding tinh vi (chèo kéo qua Zalo, số điện thoại, tích xu đánh giá ảo). Để xây dựng một hệ thống học máy có độ tin cậy cao và năng lực tổng quát hóa sát thực tế nhất, nhóm tác giả đã thiết kế và triển khai một **Phân hệ thu thập dữ liệu tự động (Automated Web Scraping Subsystem)** độc lập, nhắm trực tiếp vào hệ thống siêu thị bán lẻ điện máy và gia dụng lớn nhất Việt Nam: **Điện Máy Xanh (`dienmayxanh.com`)**.

#### 2. Kiến trúc Module hóa của Phân hệ Thu thập dữ liệu (`data_collection/`)
Toàn bộ mã nguồn thu thập dữ liệu được thiết kế theo nguyên lý module hóa chặt chẽ (Separation of Concerns), đặt trong thư mục `data_collection/` của dự án với cấu trúc gồm 6 tệp thành phần:

```text
data_collection/
├── main.py                     # Điều phối phiên làm việc tương tác CLI và quản lý RAM deduplication
├── crawler/
│   └── dmxcrawler.py           # Module lõi: Bóc tách DOM, nhận diện URL, điều hướng phân trang
├── utils/
│   └── driver_setup.py         # Khởi tạo Selenium Chrome WebDriver với cơ chế ngụy trang chống Bot
├── models/
│   └── review.py               # Định nghĩa thực thể dữ liệu nghiệp vụ Review chuẩn hóa
├── storage/
│   └── csv_storage.py          # Xử lý làm sạch và lưu trữ bền vững ra file CSV UTF-8-SIG
├── config/
│   └── settings.py             # Cấu hình đường dẫn lưu trữ tập trung của dự án
└── README.md                   # Hướng dẫn chi tiết quy trình chạy và bảo trì Crawler
```

---

[CHÈN HÌNH 3.1 TẠI ĐÂY: Kiến trúc module và luồng thu thập dữ liệu tự động với Selenium Crawler từ Điện Máy Xanh]
*(Placeholder: /assets/images/hinh3_1_kien_truc_crawler.png - Kích thước khuyến nghị: 15cm x 8cm, căn giữa)*

---

#### 3. Kỹ thuật vượt rào cản phát hiện tự động (Anti-Bot & Stealth Crawling Mechanism)
Các sàn thương mại điện tử hiện đại triển khai nhiều lớp phòng thủ tường lửa ứng dụng web (WAF - Cloudflare, BotGuard) nhằm ngăn chặn bot quét dữ liệu. Nếu sử dụng trình duyệt tự động mặc định, Selenium sẽ bị phát hiện và chặn truy cập ngay lập tức. Để bảo đảm tính ổn định tuyệt đối trong suốt quá trình cào dữ liệu, module `utils/driver_setup.py` áp dụng chuỗi kỹ thuật ngụy trang chuyên sâu:
- **Vô hiệu hóa cờ kiểm soát tự động của Blink Engine:** Thiết lập tham số `--disable-blink-features=AutomationControlled` để trình duyệt không gửi cờ báo hiệu tự động hóa lên máy chủ.
- **Loại bỏ thanh thông báo tự động:** Cấu hình `excludeSwitches=["enable-automation"]` và tắt tiện ích mở rộng tự động `useAutomationExtension=False`.
- **Ghi đè thuộc tính JavaScript qua Chrome DevTools Protocol (CDP):** Thực thi đoạn mã JavaScript can thiệp sâu vào đối tượng điều hướng trước khi trang tải:
  ```javascript
  Object.defineProperty(navigator, 'webdriver', {get: () => undefined})
  ```
  Thao tác này loại bỏ biến `navigator.webdriver = true` — vốn là dấu hiệu nhận biết hàng đầu của mọi hệ thống phát hiện bot.
- **Mô hình tương tác Người - Máy (Human-in-the-Loop):** Công cụ mở cửa sổ Chrome đầy đủ tính năng; khi trang web yêu cầu xác thực người dùng thật (CAPTCHA hoặc Cloudflare Turnstile), người vận hành có thể trực tiếp giải quyết trên giao diện đồ họa. Sau đó, người vận hành chỉ cần nhấn `Enter` trong terminal để công cụ tự động kích hoạt tiến trình bóc tách dữ liệu mà không làm đứt gãy phiên kết nối.

#### 4. Hai chế độ thu thập dữ liệu thích ứng (Adaptive Dual-Mode Crawling)
Tùy thuộc vào cấu trúc giao diện của từng sản phẩm trên trang Điện Máy Xanh, module `crawler/dmxcrawler.py` tự động chuyển đổi giữa 2 chế độ cào linh hoạt:
1. **Chế độ cào đa trang chuyên sâu (`/danh-gia` multi-page pagination):**
   - Tự động tìm kiếm và nhấn vào các liên kết chuyển hướng sang trang tổng hợp đánh giá riêng biệt có tiền tố đường dẫn `/danh-gia`.
   - Thuật toán tự động định vị nút sang trang tiếp theo (`_click_next_page`).
   - Sử dụng lớp `ActionChains` mô phỏng hành vi di chuột của người thật kết hợp lệnh JavaScript `scrollIntoView({block: 'center'})` để cuộn mượt màn hình tới đúng vị trí nút bấm, tránh lỗi phần tử bị che khuất (Element Click Intercepted).
   - Vòng lặp tự động chuyển trang tuần tự từ trang 1 cho đến khi phát hiện nút chuyển trang chuyển sang trạng thái vô hiệu hóa (`disabled` hoặc `text-gray`).
2. **Chế độ tải động một trang (Dynamic Load More / Infinite Scroll):**
   - Áp dụng cho các sản phẩm có số lượng đánh giá ít hoặc sử dụng nút "Xem thêm" trực tiếp trên trang chi tiết sản phẩm.
   - Hàm `_load_more_reviews` sử dụng danh sách bộ chọn XPath đa ngữ tìm kiếm cụm từ *"Xem thêm"*, tự động cuộn màn hình và kích hoạt sự kiện click lặp lại lên tới 50 lần liên tục, ép toàn bộ các bình luận ẩn phải hiển thị ra cây DOM trước khi bóc tách.

#### 5. Bóc tách DOM chi tiết và Cơ chế chống trùng lặp tại nguồn
- **Phân loại ngành hàng tự động từ URL:** Hàm `_get_category_from_url` phân tích cấu trúc chuỗi URL của sản phẩm để tự động gán nhãn ngành hàng chuẩn xác (ví dụ: chuỗi chứa `may-giat` $\to$ gán nhãn *"Máy giặt"*, `dieu-hoa` hoặc `may-lanh` $\to$ gán nhãn *"Điều hòa"*, `tu-lanh` $\to$ gán nhãn *"Tủ lạnh"*...).
- **Cấu trúc trường dữ liệu chuẩn hóa (Review Schema):** Mỗi đánh giá sau khi trích xuất được đóng gói thành một đối tượng thuộc lớp `Review` (`models/review.py`) gồm 6 trường thông tin chuẩn mực mô tả tại **Bảng 3.1**:

*Bảng 3.1: Cấu trúc trường thông tin (Schema) của thực thể đánh giá thu thập từ hệ thống Điện Máy Xanh.*

| Tên trường (Cột CSV) | Kiểu dữ liệu | Bộ chọn DOM / Cơ chế trích xuất | Ý nghĩa nghiệp vụ |
| :--- | :---: | :--- | :--- |
| `phan_loai` | Chuỗi (String) | Regex phân tích đường dẫn URL tĩnh | Ngành hàng thiết bị điện máy |
| `san_pham` | Chuỗi (String) | Bộ chọn CSS thẻ `h1` hoặc tiêu đề sản phẩm | Tên định danh thương mại của sản phẩm |
| `nguoi_danh_gia` | Chuỗi (String) | Bộ chọn CSS `:scope > p.gap-10px.flex > span:first-child` | Tên người dùng hiển thị gửi đánh giá |
| `so_sao` | Số nguyên (1-5)| Đếm số thẻ `i[class*='icon__row-6-col-1']` | Điểm hài lòng của khách hàng (Rating) |
| `noi_dung` | Chuỗi (String) | Bộ chọn CSS `:scope > p:nth-child(3)` | Nội dung văn bản bình luận |
| `link` | Chuỗi (URL) | `driver.current_url` | Đường dẫn nguồn phục vụ kiểm chứng |

- **Cơ chế chống trùng lặp theo ID bài đánh giá (In-memory Deduplication):**
  Trên hệ thống Điện Máy Xanh, mỗi bình luận mang một định danh duy nhất lưu tại thuộc tính HTML `data-comment-id`. Trong suốt phiên làm việc, module `main.py` duy trì một tập hợp băm `scraped_review_ids = set()` trong bộ nhớ RAM. Khi crawler quét qua danh sách phần tử DOM, nếu phát hiện `review_id` đã có trong tập hợp, đánh giá sẽ bị bỏ qua ngay lập tức. Cơ chế này loại bỏ hoàn toàn hiện tượng trùng lặp dữ liệu do thao tác cuộn trang hoặc tải lại trang gây ra.

#### 6. Quy mô và Đặc tính tập dữ liệu thu thập thực tế
Sau các phiên thu thập tự động trên hệ thống Điện Máy Xanh, phân hệ đã thu thập thành công **10,238 bài đánh giá khách hàng thực tế**, bao quát 193 dòng sản phẩm riêng biệt và được lưu trữ bền vững tại tệp `data/raw/commentdienmayxanh.csv` với bảng mã UTF-8-SIG. Thống kê phân bố số lượng đánh giá theo 10 danh mục sản phẩm được trình bày chi tiết tại **Bảng 3.2**:

*Bảng 3.2: Thống kê phân bố 10,238 bài đánh giá thô thu thập từ Điện Máy Xanh theo 10 danh mục sản phẩm.*

| STT | Ngành hàng (Category) | Số lượng đánh giá thu thập | Tỷ lệ phần trăm (%) | Các sản phẩm tiêu biểu |
| :---: | :--- | :---: | :---: | :--- |
| 1 | **Điều hòa (Máy lạnh)** | 1,677 | 16.38% | Daikin Inverter, Panasonic 1 HP, Casper, Toshiba |
| 2 | **Máy giặt** | 1,627 | 15.89% | LG Inverter lồng ngang, Electrolux 9kg, Toshiba |
| 3 | **Nồi cơm điện** | 1,625 | 15.87% | Nồi cao tần Cuckoo, Sunhouse, Sharp nắp gài |
| 4 | **Tủ lạnh** | 1,610 | 15.73% | Inverter Panasonic 2 cánh, Toshiba Inverter, Samsung |
| 5 | **Máy lọc nước** | 1,265 | 12.36% | Karofi 10 lõi RO, Kangaroo Hydrogen nóng nguội |
| 6 | **Tivi** | 931 | 9.09% | Smart Tivi Sony 4K, Samsung Crystal UHD 55 inch |
| 7 | **Máy sấy quần áo** | 724 | 7.07% | Máy sấy thông hơi Electrolux 8.5kg, Candy Inverter |
| 8 | **Gia dụng khác** | 392 | 3.83% | Quạt điều hòa Sunhouse, máy ép hoa quả, bàn ủi |
| 9 | **Máy lọc không khí** | 219 | 2.14% | Xiaomi Smart Air Purifier 4, Sharp lọc khí tạo ion |
| 10 | **Camera giám sát** | 168 | 1.64% | Camera IP Wifi Ezviz C6N, Imou 360 ngoài trời |
| **Tổng** | **10 danh mục sản phẩm** | **10,238** | **100.0%** | **193 dòng sản phẩm riêng biệt** |

*Ý nghĩa của nguồn dữ liệu cào thực tế:*
Tập dữ liệu 10,238 đánh giá thu thập từ Điện Máy Xanh phản ánh trung thực toàn diện thị trường bán lẻ điện máy tại Việt Nam: từ những bình luận chất lượng cao, các phản ánh phàn nàn kỹ thuật thực tế, cho đến các biến thể từ ngữ đời thường và các chiêu trò spam chèo kéo Zalo, tích xu đổi quà. Bộ dữ liệu này đã được gán nhãn tỉ mỉ để tạo thành tài nguyên dồi dào phục vụ quá trình huấn luyện và kiểm chứng năng lực của mô hình hiện đại FastText.

---

### 3.1.2. Mô tả tập dữ liệu thực nghiệm chuẩn và phân bố thống kê

Tập dữ liệu thô phục vụ cho nghiên cứu được thu thập từ hệ thống đánh giá sản phẩm của các sàn thương mại điện tử lớn tại Việt Nam (Shopee, Tiki, Lazada và hệ thống siêu thị Điện Máy Xanh), tập trung vào các thiết bị điện tử, điện máy và đồ gia dụng thông minh:
- **Tổng số lượng bản ghi gốc:** 10,892 bài đánh giá (dòng dữ liệu).
- **Cấu trúc trường thông tin:** Mỗi bản ghi gồm 5 thuộc tính:
  1. `category`: Tên danh mục thiết bị sản phẩm.
  2. `product`: Tên định danh hoặc model cụ thể của sản phẩm (gồm 114 dòng sản phẩm khác nhau).
  3. `review`: Nội dung chuỗi văn bản nhận xét của người dùng.
  4. `rating`: Điểm đánh giá mức độ hài lòng theo thang điểm từ 1 đến 5 sao.
  5. `label`: Nhãn phân loại nhị phân (1 = Spam, 0 = Ham).

#### 1. Phân bố theo danh mục sản phẩm (Category Distribution)
Tập dữ liệu bao quát 10 ngành hàng điện máy gia dụng phổ biến nhất trên thị trường, được mô tả chi tiết tại **Bảng 3.3**:

*Bảng 3.3: Thống kê phân bố số lượng đánh giá theo 10 danh mục sản phẩm điện máy trong tập dữ liệu thực nghiệm chuẩn.*

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
Thống kê điểm số hài lòng của khách hàng cho thấy mức phân bố tự nhiên trên các sàn thương mại điện tử, tập trung chủ yếu ở mức 5 sao và 4 sao, được mô tả tại **Bảng 3.4**:

*Bảng 3.4: Thống kê phân bố số lượng đánh giá theo số sao (Rating) trong tập dữ liệu thực nghiệm.*

| Mức đánh giá (Rating) | Số lượng đánh giá | Tỷ lệ phần trăm (%) | Nhận xét xu hướng |
| :---: | :---: | :---: | :--- |
| **5 sao (Rất hài lòng)** | 2,253 | 46.74% | Chiếm tỷ trọng lớn nhất; khách hàng hài lòng hoặc spam khen ảo |
| **4 sao (Hài lòng)** | 1,022 | 21.20% | Đánh giá tích cực vừa phải |
| **3 sao (Bình thường)** | 560 | 11.62% | Trải nghiệm trung tính |
| **2 sao (Không hài lòng)**| 352 | 7.30% | Phản ánh sản phẩm có lỗi nhỏ hoặc dịch vụ chưa tốt |
| **1 sao (Rất tệ)** | 633 | 13.13% | Phản ánh khiếu nại gay gắt hoặc spam bôi nhọ đối thủ |
| **Tổng cộng** | **4,820** | **100.0%** | **Trung bình rating đạt 3.82 sao** |

---

### 3.1.3. Kỹ thuật lọc, tăng cường dữ liệu và kết quả sau tiền xử lý

#### 1. Xử lý câu trùng lặp và mâu thuẫn nhãn
Trong tập dữ liệu thô ban đầu (10,892 bản ghi):
- Hơn một nửa số lượng bình luận là các câu ngắn bị lặp lại hàng trăm lần (câu *"Tốt"* xuất hiện 450 lần, *"Ok"* xuất hiện 340 lần).
- Một số ít câu có nội dung giống hệt nhau nhưng bị gán nhãn mâu thuẫn (cùng một câu nhưng lúc gán nhãn 1, lúc gán nhãn 0). Hệ thống đã áp dụng luật **Biểu quyết đa số (Majority Voting)** để đưa về nhãn nhất quán duy nhất.
- Tiến hành **loại bỏ trùng lặp triệt để** dựa trên nội dung đã làm sạch (`clean_text`). 

Kết quả biến động số lượng mẫu trước và sau bước khử trùng lặp được trình bày chi tiết tại **Bảng 3.7**:

*Bảng 3.7: Thống kê số lượng mẫu và tỷ lệ phân bố lớp trước và sau khi lọc trùng lặp.*

| Tập dữ liệu | Tổng số mẫu | Số mẫu Ham ($y=0$) | Số mẫu Spam ($y=1$) | Tỷ lệ Spam (%) | Tỷ lệ giảm dòng |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Dữ liệu thô ban đầu (Raw)** | 10,892 | 6,449 | 4,443 | 40.79% | - |
| **Dữ liệu sau lọc trùng (Processed)** | **4,820** | **3,976** | **844** | **17.51%** | **Giảm 55.74%** |

*Nhận định quan trọng:* Sau khi loại bỏ 6,072 dòng trùng lặp, tỷ lệ Spam thực tế giảm từ 40.79% xuống còn **17.51%**. Con số 17.51% này phản ánh chính xác cấu trúc mất cân bằng tự nhiên của bài toán thực tế (Spam chiếm khoảng 15 - 20%), chứng minh rằng phần lớn các câu trùng lặp trong dữ liệu thô trước đó là các đánh giá ngắn bị nhân bản nhân tạo.

#### 2. Phân chia tập huấn luyện và kiểm thử phân tầng (Stratified 80/20)
Sau khi lọc trùng lặp, tập dữ liệu gồm 4,820 mẫu độc nhất được phân chia thành hai tập độc lập: **Tập huấn luyện (Train Set - 80%)** và **Tập kiểm thử (Test Set - 20%)** có phân tầng theo nhãn (`stratify=df['label']`, `random_state=42`), được mô tả tại **Bảng 3.6**:

*Bảng 3.6: Phân bố số lượng mẫu tập Train và Test sau khi phân chia phân tầng (Stratified 80/20).*

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

[CHÈN HÌNH 3.2 TẠI ĐÂY: Phân bố độ dài câu (số lượng token) trong tập dữ liệu sau bước làm sạch tiền xử lý]
*(Placeholder: /assets/images/hinh3_2_phan_bo_do_dai_cau.png - Kích thước khuyến nghị: 14cm x 6cm, căn giữa)*

---

#### 4. Minh họa trực quan các câu đánh giá trước và sau làm sạch
Để làm rõ tác động tích cực của pipeline tiền xử lý, **Bảng 3.7** minh họa một số mẫu câu thực tế được trích xuất từ dữ liệu:

*Bảng 3.7: Một số ví dụ cụ thể về câu đánh giá trước và sau khi thực hiện tiền xử lý làm sạch.*

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
Ma trận nhầm lẫn là công cụ biểu diễn trực quan mối quan hệ giữa nhãn thực tế (Ground Truth) và nhãn dự đoán (Predicted Label) của mô hình phân loại nhị phân, được định nghĩa tại **Bảng 3.8**:

*Bảng 3.8: Ma trận nhầm lẫn tổng quát (Confusion Matrix) cho bài toán phân loại nhị phân Spam/Ham.*

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

*Bảng 3.11: Kết quả thực nghiệm chi tiết của các biến thể mô hình Naive Bayes trên 3 bộ đặc trưng.*

| Mô hình | Bộ đặc trưng | Siêu tham số tối ưu | CV F1 (Train) | Accuracy | Precision (Spam) | Recall (Spam) | F1-Score (Spam) | F1 Macro | ROC-AUC | PR-AUC |
| :--- | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **MultinomialNB** | **Bag of Words** | $\alpha = 0.003$ | 0.8019 | **93.36%** | **83.02%** | 78.11% | **80.49%** | **88.24%** | **0.9769** | 0.8839 |
| **ComplementNB** | **TF-IDF** | $\alpha = 0.001$ | **0.8108** | 93.05% | 81.10% | **78.70%** | 79.88% | 87.84% | 0.9765 | **0.8926** |
| **GaussianNB** | **Word2Vec (WE)** | `var_smoothing` $= 10^{-12}$ | 0.6032 | 83.20% | 51.41% | 75.74% | 61.24% | 75.26% | 0.8966 | 0.5870 |

*Bảng 3.12: Ma trận nhầm lẫn chi tiết của 3 biến thể mô hình Naive Bayes trên tập Test (964 mẫu).*

| Mô hình Naive Bayes | True Negative (TN) | False Positive (FP) | False Negative (FN) | True Positive (TP) | Tổng lỗi sai |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **MultinomialNB + BoW** | 768 | 27 | 37 | 132 | 64 |
| **ComplementNB + TF-IDF** | 764 | 31 | 36 | 133 | 67 |
| **GaussianNB + Word2Vec** | 674 | 121 | 41 | 128 | 162 |

---

[CHÈN HÌNH 3.8 TẠI ĐÂY: Ma trận nhầm lẫn (Confusion Matrix) của mô hình Multinomial Naive Bayes + Bag of Words]
*(Placeholder: results/nb-bow_confusion_matrix.png - Kích thước khuyến nghị: 8cm x 7cm, căn giữa)*

[CHÈN HÌNH 3.8 TẠI ĐÂY: Ma trận nhầm lẫn (Confusion Matrix) của mô hình Complement Naive Bayes + TF-IDF]
*(Placeholder: results/nb-tfidf_confusion_matrix.png - Kích thước khuyến nghị: 8cm x 7cm, căn giữa)*

[CHÈN HÌNH 3.8 TẠI ĐÂY: Ma trận nhầm lẫn (Confusion Matrix) của mô hình Gaussian Naive Bayes + Word Embedding]
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

*Bảng 3.11: Kết quả thực nghiệm chi tiết của các biến thể mô hình SVM trên 3 bộ đặc trưng.*

| Mô hình | Bộ đặc trưng | Siêu tham số tối ưu | CV F1 (Train) | Accuracy | Precision (Spam) | Recall (Spam) | F1-Score (Spam) | F1 Macro | ROC-AUC | PR-AUC |
| :--- | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Linear SVM** | **Bag of Words** | $C = 0.5$, `weight`=None | 0.8414 | 94.09% | 76.92% | **94.67%** | 84.88% | 90.60% | 0.9793 | 0.8674 |
| **Linear SVM** | **TF-IDF** | $C = 1.0$, `weight`='balanced'| 0.8377 | 93.57% | 75.60% | 93.49% | 83.60% | 89.80% | 0.9772 | 0.8579 |
| **RBF SVM** | **Word2Vec (WE)**| $C = 10.0$, `gamma`='scale', 'balanced'| **0.8755** | **95.85%** | **86.86%** | 89.94% | **88.37%** | **92.92%** | **0.9859** | **0.9265** |

*Bảng 3.12: Ma trận nhầm lẫn chi tiết của 3 biến thể mô hình SVM trên tập Test (964 mẫu).*

| Mô hình SVM | True Negative (TN) | False Positive (FP) | False Negative (FN) | True Positive (TP) | Tổng lỗi sai |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Linear SVM + BoW** | 747 | 48 | **9** | **160** | 57 |
| **Linear SVM + TF-IDF** | 744 | 51 | 11 | 158 | 62 |
| **RBF SVM + Word2Vec** | **772** | **23** | 17 | 152 | **40** |

---

[CHÈN HÌNH 3.8 TẠI ĐÂY: Ma trận nhầm lẫn (Confusion Matrix) của mô hình Linear SVM + Bag of Words]
*(Placeholder: results/svm-bow_confusion_matrix.png - Kích thước khuyến nghị: 8cm x 7cm, căn giữa)*

[CHÈN HÌNH 3.8 TẠI ĐÂY: Ma trận nhầm lẫn (Confusion Matrix) của mô hình Linear SVM + TF-IDF]
*(Placeholder: results/svm-tfidf_confusion_matrix.png - Kích thước khuyến nghị: 8cm x 7cm, căn giữa)*

[CHÈN HÌNH 3.8 TẠI ĐÂY: Ma trận nhầm lẫn (Confusion Matrix) của mô hình RBF SVM + Word Embedding]
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

### 3.3.3. Kết quả thực nghiệm với mô hình học máy hiện đại FastText

Để kiểm chứng tính ưu việt của hướng tiếp cận mạng nơ-ron nông tích hợp thông tin n-gram ký tự con và n-gram từ, nhóm tác giả đã tiến hành huấn luyện và đánh giá mô hình **FastText** trên cả hai kịch bản thực nghiệm:
1. **Kịch bản Benchmark chuẩn hóa (Held-out Test 964 mẫu):** Huấn luyện trên 3,856 mẫu train và kiểm thử trên đúng 964 mẫu test độc lập của bộ dữ liệu chuẩn (`data/processed/processed.csv`) — cùng một phân chia với 6 mô hình Naive Bayes và SVM để đảm bảo tính công bằng tuyệt đối.
2. **Kịch bản Mở rộng trên Dữ liệu cào thực tế (`FastText_Performance/`):** Huấn luyện và đánh giá trên kho dữ liệu cào thực tế từ Điện Máy Xanh (`reviews_spam_ham.csv` gồm 7,583 câu độc nhất sau làm sạch, chia 80/20: 6,066 train / 1,517 test).

Kết quả định lượng chi tiết của FastText trên cả hai kịch bản được tổng hợp tại **Bảng 3.13** và ma trận nhầm lẫn tại **Bảng 3.14**:

*Bảng 3.13: Kết quả thực nghiệm chi tiết của mô hình FastText trên tập Test Benchmark và tập cào mở rộng.*

| Kịch bản thực nghiệm | Số mẫu Train | Số mẫu Test | Siêu tham số tối ưu | Accuracy | Precision (Spam) | Recall (Spam) | F1-Score (Spam) | F1 Macro | ROC-AUC | PR-AUC |
| :--- | :---: | :---: | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **FastText (Benchmark chuẩn)** | **3,856** | **964** | `lr=0.3`, `epoch=35`, `dim=50`, `wordNgrams=2`, `minn=2`, `maxn=5` | **96.37%** | **87.64%** | **92.31%** | **89.91%** | **93.85%** | **0.9848** | **0.9403** |
| **FastText (Dữ liệu cào mở rộng)** | 6,066 | 1,517 | `lr=0.3`, `epoch=35`, `dim=50`, `wordNgrams=2`, `minn=2`, `maxn=5` | **99.27%** | 65.00% | 76.47% | **70.27%** | **84.95%** | 0.9560 | 0.8065 |

*Bảng 3.14: Ma trận nhầm lẫn chi tiết của mô hình FastText trên tập Test Benchmark (964 mẫu).*

| Mô hình thuật toán | True Negative (TN) | False Positive (FP) | False Negative (FN) | True Positive (TP) | Tổng số lỗi sai | Tỷ lệ lỗi (%) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **FastText (Subwords + Word n-grams)** | **773** | **22** | **13** | **156** | **35** | **3.63%** |

---

[CHÈN HÌNH 3.9 TẠI ĐÂY: Ma trận nhầm lẫn (Confusion Matrix) của mô hình học máy hiện đại FastText]
*(Placeholder: results/fasttext_confusion_matrix.png - Kích thước khuyến nghị: 8cm x 7cm, căn giữa)*

---

#### Phân tích chuyên sâu kết quả thực nghiệm của FastText:
1. **Xác lập kỷ lục hiệu năng mới trên tập Benchmark chuẩn (Vị trí Quán quân Top 1):**
   - **F1-Score lớp Spam đạt 89.91% (0.8991):** Đây là điểm số cao nhất trong toàn bộ các cấu hình thực nghiệm của đề tài, vượt qua quán quân nhóm truyền thống là RBF SVM trên Word2Vec ($88.37\%$, tăng $+1.54\%$) và bỏ xa Linear SVM trên BoW ($84.88\%$, tăng $+5.03\%$).
   - **Độ chính xác tổng thể (Accuracy) đạt 96.37%:** FastText phân loại chính xác 929 trên tổng số 964 bài đánh giá kiểm thử độc lập.
   - **Diện tích dưới đường cong PR-AUC đạt đỉnh 0.9403 (94.03%):** So với RBF SVM ($0.9265$) và MultinomialNB ($0.8839$), chỉ số PR-AUC vượt trội khẳng định FastText duy trì độ tin cậy phân loại cực kỳ bền vững trên tập dữ liệu mất cân bằng nghiêm trọng.
   - **Tổng số lỗi sai thấp nhất toàn hệ thống:** FastText chỉ phạm tổng cộng **35 lỗi sai** trên toàn bộ 964 mẫu kiểm thử (gồm 22 mẫu báo nhầm FP và 13 mẫu bỏ sót FN). Trong khi đó, RBF SVM phạm 40 lỗi, Linear SVM BoW phạm 57 lỗi, và MultinomialNB phạm 64 lỗi!
2. **Cơ chế bứt phá của FastText trước ngôn ngữ TMĐT tiếng Việt:**
   - **Triệt tiêu hoàn toàn điểm mù Out-Of-Vocabulary (OOV):** Trong khi BoW và Word2Vec hoàn toàn "mù" trước các từ viết sai chính tả hoặc biến thể teencode mới, FastText sử dụng n-gram ký tự con ($minn=2, maxn=5$) để chia nhỏ các từ này thành các mẩu ký tự quen thuộc. Nhờ vậy, ngay cả khi người dùng gõ *"sài rất đẹpppp"*, FastText vẫn nhận ra các n-gram `đẹp`, `đẹp_`, `ẹpp` để tổng hợp thành vector tích cực chính xác.
   - **Nắm bắt ngữ cảnh cụm từ đảo ngược nhờ Word n-grams (`wordNgrams=2`):** Sự xuất hiện của các cặp từ phủ định như *"không lạnh"*, *"chưa ưng"*, *"hơi ồn"* được mô hình ghi nhận trực tiếp như một đặc trưng riêng biệt, ngăn chặn tình trạng thuật toán túi từ bị đánh lừa bởi từ đơn lẻ *"lạnh"* hay *"ưng"*.
3. **Hiệu năng xuất sắc trên tập dữ liệu cào thực tế mở rộng (`FastText_Performance`):**
   - Trên tập kiểm thử mở rộng 1,517 câu độc nhất từ Điện Máy Xanh, FastText đạt độ chính xác ấn tượng **99.27%** và **Macro F1 đạt 84.95%**.
   - Dù lớp Spam trong tập dữ liệu cào này cực kỳ hiếm (chỉ có 17 mẫu spam trong 1,517 mẫu test, chiếm tỷ lệ $\approx 1.12\%$), FastText vẫn phát hiện chuẩn xác **13/17 mẫu spam** ($Recall = 76.47\%$), đạt điểm **F1 lớp Spam 70.27%**. Kết quả này khẳng định khả năng khái quát hóa mạnh mẽ của FastText trên dữ liệu đời thực quy mô lớn mà không gặp hiện tượng quá khớp (Overfitting).

---

### 3.3.4. So sánh tổng hợp và phân tích hiệu năng giữa tất cả các phương pháp

#### 1. Bảng đối sánh tổng thể 7 mô hình thực nghiệm

*Bảng 3.15: Bảng so sánh tổng hợp hiệu năng phân loại của toàn bộ 7 mô hình thực nghiệm trên tập Test Benchmark 964 mẫu (sắp xếp theo thứ tự giảm dần của F1-Score Spam).*

| Thứ hạng | Mô hình thuật toán | Bộ đặc trưng biểu diễn | Accuracy | Precision (Spam) | Recall (Spam) | F1-Score (Spam) | F1 Macro | ROC-AUC | PR-AUC | Đánh giá tổng quan |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| 🥇 **1** | **FastText (Supervised)** | **Subwords + Word n-grams**| **96.37%** | **87.64%** | 92.31% | **89.91%** | **93.85%** | 0.9848 | **0.9403** | **Quán quân toàn diện, hiệu năng SOTA, xử lý OOV và teencode xuất sắc nhất** |
| 🥈 **2** | **RBF SVM** | **Word2Vec (WE)**| 95.85% | 86.86% | 89.94% | 88.37% | 92.92% | **0.9859** | 0.9265 | **Á quân, tốt nhất nhóm ML truyền thống, cân bằng tối ưu** |
| 🥉 **3** | **Linear SVM** | BoW (11,004 chiều) | 94.09% | 76.92% | **94.67%** | 84.88% | 90.60% | 0.9793 | 0.8674 | **Recall cao nhất nhóm truyền thống (chỉ sót 9 spam)** |
| 4 | **Linear SVM** | TF-IDF (11,004 chiều) | 93.57% | 75.60% | 93.49% | 83.60% | 89.80% | 0.9772 | 0.8579 | Hiệu năng cao, quét sạch spam, thiên lệch Recall |
| 5 | **MultinomialNB**| BoW (11,004 chiều) | 93.36% | 83.02% | 78.11% | 80.49% | 88.24% | 0.9769 | 0.8839 | Rất nhanh, ít báo nhầm ($FP=27$), thiên lệch Precision |
| 6 | **ComplementNB** | TF-IDF (11,004 chiều) | 93.05% | 81.10% | 78.70% | 79.88% | 87.84% | 0.9765 | 0.8926 | Ổn định trên dữ liệu lệch lớp, PR-AUC khá cao |
| 7 | **GaussianNB** | Word2Vec (100 chiều) | 83.20% | 51.41% | 75.74% | 61.24% | 75.26% | 0.8966 | 0.5870 | Thấp nhất, vi phạm nghiêm trọng giả định độc lập |

---

[CHÈN HÌNH 3.10 TẠI ĐÂY: Biểu đồ cột đối sánh các chỉ số hiệu năng chính (Accuracy, Precision, Recall, F1-Spam, ROC-AUC, PR-AUC) giữa 7 mô hình]
*(Placeholder: /assets/images/hinh3_10_bieu_do_doi_sanh_hieu_nang.png - Kích thước khuyến nghị: 15cm x 8cm, căn giữa)*

---

#### 2. Phân tích sự đánh đổi giữa Precision và Recall (Precision-Recall Trade-off)
Khi quan sát bức tranh đối sánh tổng thể giữa các mô hình học máy truyền thống và mô hình hiện đại, quy luật đánh đổi giữa Precision và Recall thể hiện rất rõ ràng:
- **Nhóm mô hình SVM tuyến tính (Linear SVM trên BoW/TF-IDF):** Thiên hẳn về **Recall** (Recall đạt 93.5% - 94.7%, nhưng Precision bị nén xuống mức 75.6% - 76.9%). Thuật toán sẵn sàng chấp nhận bắt nhầm nhiều bình luận hợp lệ (FP lên tới 48 - 51 câu) để không bỏ sót các biến thể spam.
- **Nhóm mô hình Naive Bayes xác suất (MNB / CNB):** Thiên hẳn về **Precision** (Precision đạt 81.1% - 83.0%, nhưng Recall bị giới hạn ở mức ~78.1% - 78.7%). Mô hình chỉ gắn nhãn Spam khi bằng chứng xác suất tích lũy là áp đảo, ít báo nhầm ($FP \approx 27 - 31$) nhưng lại để lọt nhiều bài spam ngụy trang khéo ($FN \approx 36 - 37$).
- **Mô hình RBF SVM trên Word2Vec:** Đạt trạng thái cân bằng rất tốt trong nhóm truyền thống (Precision 86.86%, Recall 89.94%).
- **Mô hình hiện đại FastText — Phá vỡ ranh giới đánh đổi (Breaking the Pareto Frontier):**
  FastText tạo nên bước nhảy vọt khi duy trì đồng thời cả **Precision cực cao (87.64%)** lẫn **Recall rất lớn (92.31%)**. Bằng cách kết hợp n-gram ký tự con để hiểu sâu sắc các biến thể từ vựng và n-gram từ để nắm bắt trật tự cú pháp, FastText không cần phải hy sinh Precision để đổi lấy Recall như Linear SVM, cũng không bị rụt rè bỏ sót dữ liệu như Naive Bayes. Đây là minh chứng thuyết phục nhất cho sức mạnh của biểu diễn n-gram phân cấp trong NLP hiện đại.

---

### 3.3.5. Đánh giá hiệu năng tính toán và dung lượng lưu trữ (Computational Efficiency)

*Bảng 3.16: Đánh giá hiệu năng tính toán và dung lượng lưu trữ của các mô hình thực nghiệm.*

| Mô hình thuật toán | Bộ đặc trưng biểu diễn | Thời gian huấn luyện lại (Train Time) | Thời gian dự đoán tập Test (964 mẫu) | Thời gian suy luận trung bình / 1 mẫu | Dung lượng file mô hình lưu trữ |
| :--- | :--- | :---: | :---: | :---: | :---: |
| **MultinomialNB** | BoW (11,004 chiều) | **3.8 ms** | **0.62 ms** | **0.64 µs / mẫu** | 352 KB |
| **ComplementNB** | TF-IDF (11,004 chiều) | **2.5 ms** | **0.42 ms** | **0.44 µs / mẫu** | 441 KB |
| **GaussianNB** | Word2Vec (100 chiều) | 4.0 ms | 0.94 ms | 0.97 µs / mẫu | **2.4 KB** |
| **Linear SVM** | BoW (11,004 chiều) | 58.0 ms | 0.45 ms | **0.47 µs / mẫu** | 88 KB |
| **Linear SVM** | TF-IDF (11,004 chiều) | 15.9 ms | 0.77 ms | 0.80 µs / mẫu | 88 KB |
| **RBF SVM** | Word2Vec (100 chiều) | 198.8 ms | 57.08 ms | 59.21 µs / mẫu | 814 KB |
| **FastText** | **Subwords + Word n-grams**| **18.00 s** | **281.82 ms** | **292.35 µs / mẫu** | **~38 MB** |

---

[CHÈN HÌNH 3.11 TẠI ĐÂY: Đồ thị tương quan giữa thời gian huấn luyện và hiệu năng F1-Score của các mô hình thực nghiệm]
*(Placeholder: /assets/images/hinh3_11_tuong_quan_thoi_gian_f1.png - Kích thước khuyến nghị: 14cm x 7cm, căn giữa)*

---

*Nhận định về hiệu năng vận hành thực tế:*
- **Tốc độ suy luận siêu tốc (Ultra-fast Real-time Inference):**
  - Các mô hình ML tuyến tính truyền thống (Linear SVM, MultinomialNB, ComplementNB) chỉ mất từ **0.44 đến 0.80 micro-giây (µs)** cho mỗi mẫu đánh giá.
  - Mô hình học máy hiện đại FastText, dù phải tính toán hàng loạt phép băm n-gram ký tự con và n-gram từ, chỉ mất **292 micro-giây (0.29 mili-giây)** để phân loại xong một bài đánh giá. Tốc độ này tương đương với năng lực thông lượng đạt hơn **3,400 bài đánh giá mỗi giây** trên một luồng CPU tiêu chuẩn — hoàn toàn đáp ứng xuất sắc yêu cầu kiểm duyệt thời gian thực (Real-time Filtering Pipeline) của các sàn thương mại điện tử lớn với hàng triệu giao dịch mỗi ngày.
- **Tính khả thi về mặt tài nguyên và triển khai:**
  - FastText chỉ mất vỏn vẹn **18 giây** để hoàn tất toàn bộ quá trình huấn luyện 35 epochs trên CPU thông thường mà không cần bất kỳ card đồ họa GPU chuyên dụng nào.
  - Dung lượng file mô hình của FastText (~38 MB) chứa toàn bộ bảng băm 50,000 buckets n-gram và ma trận trọng số phân loại. Dung lượng này đủ gọn nhẹ để nạp trực tiếp vào RAM của bất kỳ container microservice hoặc thiết bị biên nào.

---

### 3.3.6. Phân tích định tính các ca phân loại sai (Qualitative Error Analysis)
Để hiểu sâu sắc cơ chế hoạt động và ranh giới quyết định của các mô hình học máy, nhóm tác giả đã tiến hành rà soát chi tiết các file nhật ký phân loại sai (`results/*_errors.csv`):

#### 1. Phân tích các trường hợp Dương tính giả (False Positives - Ham bị báo nhầm là Spam)
Dương tính giả là lỗi hệ thống nhận diện nhầm một đánh giá chân chính của người dùng thành rác quảng cáo/lừa đảo. Trong thực tế, loại lỗi này gây ảnh hưởng nghiêm trọng tới trải nghiệm khách hàng và uy tín của gian hàng. **Bảng 3.17** phân tích các ca FP điển hình:

*Bảng 3.17: Phân tích định tính các ví dụ thực tế bị phân loại sai dạng Dương tính giả (False Positives - Ham bị báo nhầm là Spam).*

| Đánh giá thực tế của khách hàng | Nhãn thực | Dự đoán | Điểm số quyết định | Mô hình phạm lỗi | Phân tích nguyên nhân ngữ nghĩa sâu xa |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `"Sài rất okla nha shop"` | 0 (Ham) | 1 (Spam) | +1.124 | Linear SVM (BoW) | Từ `"okla"` là biến thể teencode mới lạ, không nằm trong từ điển teencode chuẩn hóa, xuất hiện ngẫu nhiên trong vài mẫu spam quảng cáo train nên SVM gán trọng số dương lớn. |
| `"Mới lắp hôm qua, thợ nhiệt tình, cho 5 sao"` | 0 (Ham) | 1 (Spam) | +0.432 | Linear SVM (TF-IDF) | Cụm từ `"cho 5 sao"` bị thuật toán TF-IDF phạt do tần suất xuất hiện dày đặc trong các bài đánh giá mồi chài tích xu (Seeding reviews). |
| `"sài oce"` | 0 (Ham) | 1 (Spam) | 0.9997 (Xác suất) | FastText | Từ `"oce"` (biến thể của ok). Do câu quá ngắn (chỉ 2 từ) và chứa biến thể teencode cực đoan, các subword n-gram kích hoạt trọng số spam cao tương tự các câu đánh giá vô nghĩa tích xu. |
| `"tuyet zoi"` | 0 (Ham) | 1 (Spam) | 0.9997 (Xác suất) | FastText | Từ `"zoi"` viết sai chính tả theo phong cách teencode tuổi teen. Mô hình nhầm lẫn với các mẫu spam ngụy trang lời khen sáo rỗng. |
| `"Shop ơi cho hỏi còn khuyến mãi tặng kèm không ạ"` | 0 (Ham) | 1 (Spam) | +0.781 (ngưỡng 0.5) | MultinomialNB (BoW) | Khách hỏi tư vấn thay vì đánh giá sản phẩm. Chứa các từ `"khuyến mãi"`, `"tặng kèm"` — vốn là các từ mang trọng số spam cực cao trong phân phối đa thức. |
| `"Máy êm, làm đá nhanh, đáng tiền"` | 0 (Ham) | 1 (Spam) | +0.108 | RBF SVM (WE) | Vector biểu diễn trung bình của câu ngắn này nằm rất sát siêu phẳng phân tách trong không gian 100 chiều do cấu trúc cú pháp ngắn tương tự các câu spam khen ảo. |

#### 2. Phân tích các trường hợp Âm tính giả (False Negatives - Spam bị bỏ sót thành Ham)
Âm tính giả là lỗi hệ thống để lọt các bài đánh giá rác, khiến người tiêu dùng tiếp cận phải thông tin giả mạo hoặc lừa đảo. **Bảng 3.18** phân tích các ca FN điển hình:

*Bảng 3.18: Phân tích định tính các ví dụ thực tế bị phân loại sai dạng Âm tính giả (False Negatives - Spam bị bỏ sót thành Ham).*

| Đánh giá rác thực tế | Nhãn thực | Dự đoán | Điểm số quyết định | Mô hình phạm lỗi | Phân tích nguyên nhân ngụy trang tinh vi |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `"Tot"` | 1 (Spam) | 0 (Ham) | -0.602 | RBF SVM (WE) | Câu viết hoa không dấu, cực ngắn (`tot`). Từ này xuất hiện ở cả hai lớp nhưng trọng số thiên về phản hồi tích cực ngắn, mô hình không đủ bằng chứng quy kết là spam. |
| `"m"` | 1 (Spam) | 0 (Ham) | 0.00001 (Xác suất) | FastText | Đánh giá vô nghĩa chỉ gồm 1 ký tự duy nhất (`m`). Chuỗi ký tự quá ngắn không đủ sinh ra các n-gram từ và subword đặc trưng, FastText mặc định gán theo phân phối tiên nghiệm lớp đa số (Ham). |
| `"aqua dùng tốt"` | 1 (Spam) | 0 (Ham) | 0.2687 (Xác suất) | FastText | Spam ngụy trang cực kỳ tinh vi dưới dạng lời khen chuẩn mực (`aqua dùng tốt`). Nếu chỉ phân tích nội dung văn bản thuần túy mà không có siêu dữ liệu (IP, lịch sử mua hàng), mô hình văn bản không thể phát hiện được hành vi seeding. |
| `"Ok . Qua tuyệt vời"` | 1 (Spam) | 0 (Ham) | -0.073 | RBF SVM (WE) | Spam tinh vi ngụy trang lời khen ("Qua tuyệt vời"). Thuật toán vector ngữ nghĩa đánh giá độ tương đồng ngữ nghĩa tích cực rất cao nên xếp vào nhãn Ham. |
| `"Mmmmmm"` | 1 (Spam) | 0 (Ham) | -0.286 | RBF SVM (WE) | Sau khi qua biểu thức chính quy rút gọn ký tự lặp `(\w)\1{2,}`, chuỗi biến thành ký tự đơn `m`. Token đơn lẻ này rơi vào vùng quyết định của lớp đa số. |
| `"Chất lượng tốt"` | 1 (Spam) | 0 (Ham) | -0.188 | Linear SVM (BoW) | Câu đánh giá mẫu mặc định (Template review). Cụm từ mang nghĩa tích cực chuẩn mực, thuật toán túi từ không thể phát hiện ý đồ seeding nếu chỉ nhìn vào 2 từ đơn lẻ này. |

---

### CHƯƠNG 4: Kết luận và hướng phát triển

## 4.1. Kết quả đạt được

Đề tài bài tập lớn đã hoàn thành trọn vẹn toàn bộ các mục tiêu nghiên cứu và yêu cầu kỹ thuật đề ra ban đầu, với các đóng góp cụ thể:
1. **Thiết kế và hiện thực hóa thành công Phân hệ thu thập dữ liệu tự động (Selenium Web Crawler) từ hệ sinh thái Điện Máy Xanh:**
   - Xây dựng kiến trúc module hóa hoàn chỉnh trong `data_collection/` với các cơ chế phòng vệ vượt tường lửa chống bot hiện đại (vô hiệu hóa Blink Automation, ghi đè biến điều hướng `navigator.webdriver`, hỗ trợ Human-in-the-Loop).
   - Tự động hóa 2 chế độ cào linh hoạt (phân trang `/danh-gia` và cuộn động "Xem thêm"), tích hợp cơ chế chống trùng lặp theo ID bài đánh giá (`data-comment-id`) trực tiếp trong RAM.
   - Thu thập thành công kho ngữ liệu thực tế gồm **10,238 bài đánh giá khách hàng** bao quát 10 ngành hàng điện máy gia dụng và 193 dòng sản phẩm riêng biệt (`commentdienmayxanh.csv`).
2. **Xây dựng thành công Pipeline tiền xử lý văn bản tiếng Việt chuyên sâu và giải quyết triệt để rủi ro rò rỉ dữ liệu:**
   - Đã hiện thực hóa quy trình chuẩn hóa Unicode NFC, trừu tượng hóa các thực thể nhạy cảm (`urltoken`, `phonetoken`, `numtoken`), xử lý ký tự lặp, tách dấu câu và giải mã từ điển teencode gồm hơn 30 quy tắc đặc thù ngành thương mại điện tử.
   - Phát hiện hiện tượng 55.7% dòng trùng lặp trong dữ liệu thô và giải quyết bài toán chống rò rỉ dữ liệu (Anti-Data Leakage) bằng thuật toán Majority Voting kết hợp loại bỏ trùng lặp trước khi chia phân tầng Train/Test 80/20.
3. **Khảo sát hệ thống đa không gian biểu diễn văn bản:** Hiện thực hóa thành công không gian rời rạc thưa BoW (11,004 chiều), TF-IDF với sublinear scaling và chuẩn hóa L2, không gian liên tục dày đặc Word2Vec Skip-gram (100 chiều) với kỹ thuật Pooling câu, và không gian n-gram ký tự con hiện đại (FastText Subwords).
4. **Thực nghiệm đối sánh toàn diện giữa Học máy truyền thống và Mô hình hiện đại FastText:**
   - **Mô hình học máy hiện đại FastText** đạt danh hiệu **Quán quân toàn diện (Top 1 SOTA)** với **F1-Score lớp Spam đạt 89.91%**, **Accuracy đạt 96.37%**, **PR-AUC đạt 0.9403**, và **F1 Macro đạt 93.85%**. FastText giải quyết xuất sắc điểm nghẽn từ ngoài từ điển (OOV) và teencode tiếng Việt nhờ cơ chế n-gram ký tự con.
   - Mô hình **RBF SVM trên Word2Vec** đạt Á quân toàn diện trong nhóm truyền thống với **F1-Score Spam đạt 88.37%**, **Accuracy đạt 95.85%**, **ROC-AUC đạt 0.9859**, **PR-AUC đạt 0.9265**, duy trì sự cân bằng tối ưu giữa Precision (86.86%) và Recall (89.94%).
   - Mô hình **Linear SVM trên Bag-of-Words** đạt độ nhạy vượt trội với **Recall lên tới 94.67%** (chỉ bỏ sót 9 trên tổng số 169 câu spam).
   - Làm sáng tỏ nguyên nhân lý thuyết khiến **Gaussian Naive Bayes trên Word2Vec thất bại (F1 chỉ đạt 61.24%)** do vi phạm nghiêm trọng giả định độc lập có điều kiện giữa các chiều vector ngữ nghĩa.
5. **Tối ưu hóa hiệu năng tính toán và sẵn sàng triển khai thực tế:** Toàn bộ các mô hình có thời gian suy luận siêu tốc (từ 0.4 µs đến 292 µs / mẫu trên CPU tiêu chuẩn mà không cần GPU), dung lượng lưu trữ gọn nhẹ (dưới 40 MB), hoàn toàn sẵn sàng đóng gói triển khai microservice thời gian thực trên hạ tầng sản xuất thực tế.

---

## 4.2. Ưu, nhược điểm của phương pháp

### 1. Ưu điểm nổi bật
- **Tính thực tiễn và khả thi cao (High Practical Feasibility):** Toàn bộ pipeline từ khâu thu thập dữ liệu tự động đến mô hình hóa FastText không đòi hỏi máy chủ GPU đắt đỏ, tiêu tốn ít RAM, tốc độ xử lý hàng nghìn đến hàng triệu câu mỗi giây, dễ dàng tích hợp vào hệ thống backend của các sàn TMĐT.
- **Tính ưu việt trong xử lý ngôn ngữ tiếng Việt phi chuẩn:** Sự kết hợp giữa bộ lọc tiền xử lý teencode và cơ chế n-gram ký tự con của FastText giúp hệ thống có khả năng "miễn nhiễm" cao trước các biến thể gõ sai chính tả, từ ghép địa phương và ngôn ngữ mạng.
- **Tính toàn vẹn khoa học (Methodological Rigor):** Quy trình kiểm thử độc lập, phân tầng, khử trùng lặp và đóng gói Pipeline chuẩn mực bảo đảm kết quả đạt được là hoàn toàn khách quan, không bị thổi phồng ảo bởi data leakage.
- **Khả năng giải thích và tính minh bạch:** Các mô hình tuyến tính (Linear SVM, MNB) cho phép trích xuất trọng số tường minh, trong khi FastText cung cấp cơ chế phân tích đóng góp của từng subword n-gram.

### 2. Nhược điểm và hạn chế tồn đọng
- **Bất lực trước các đánh giá rác ngụy trang bằng lời khen chuẩn mực (Deceptive Positive Spam):**
  Khi kẻ xấu cố tình viết các bài đánh giá 5 sao bằng từ ngữ tích cực hoàn hảo như *"Máy dùng rất tốt, giao hàng nhanh"* để đẩy thứ hạng sản phẩm, các mô hình xử lý văn bản thuần túy hoàn toàn không thể phát hiện được nếu không kết hợp với siêu dữ liệu hành vi (Behavioral Features).
- **Hiện tượng nhầm lẫn với các câu đánh giá ngắn chứa teencode:** Các bình luận khách hàng thật nhưng quá ngắn và viết tắt nhiều (`"sài oce"`, `"tuyet zoi"`) đôi khi bị mô hình nhầm lẫn với spam tích xu vô nghĩa.

---

## 4.3. Hướng phát triển trong tương lai

Từ các kết quả nghiên cứu và những hạn chế đã được chỉ ra, nhóm tác giả đề xuất 4 hướng phát triển trọng tâm trong tương lai:
1. **Tích hợp Đặc trưng Hành vi Người dùng (Behavioral & Metadata Fusion):**
   Kết hợp văn bản với các thuộc tính siêu dữ liệu như: lịch sử mua hàng, địa chỉ IP, tần suất gửi đánh giá của tài khoản trong ngày, độ lệch giữa số sao đánh giá và nội dung văn bản, tỷ lệ bài đánh giá trùng lặp của cùng một User ID. Đây là giải pháp duy nhất để bóc trần các bài spam ngụy trang lời khen hoàn hảo.
2. **Mở rộng Hệ thống Thu thập Dữ liệu Đa nền tảng:**
   Mở rộng phân hệ crawler tự động sang các nền tảng thương mại điện tử lớn khác như Shopee, TikTok Shop, Lazada, Tiki nhằm xây dựng một kho ngữ liệu đánh giá tiếng Việt mở quy mô hàng triệu mẫu, phục vụ cộng đồng nghiên cứu NLP trong nước.
3. **Nghiên cứu Kiến trúc Lai (Hybrid Architectures) và Tinh chỉnh Subword Embeddings:**
   Khảo sát việc kết hợp vector nhúng subword của FastText làm tầng đầu vào (Input Layer) cho các bộ phân loại RBF SVM hoặc mạng nơ-ron tích chập nhẹ (Lightweight CNN), đồng thời thử nghiệm tiền huấn luyện FastText trên toàn bộ kho ngữ liệu báo chí tiếng Việt trước khi fine-tuning trên tập đánh giá TMĐT.
4. **Đóng gói Hệ thống thành Dịch vụ Kiểm duyệt Tự động (End-to-End Spam Moderation API):**
   Xây dựng RESTful API dựa trên FastAPI kết hợp cơ chế hàng đợi bất đồng bộ (Celery + Redis) để cung cấp dịch vụ kiểm duyệt bình luận thời gian thực cho các doanh nghiệp thương mại điện tử vừa và nhỏ tại Việt Nam.

\\newpage\n\n# TÀI LIỆU THAM KHẢO
---
1. Slide môn học Phân tích và khai phá dữ liệu văn bản

# PHỤ LỤC

---

### PHỤ LỤC A: Bảng phân công nhiệm vụ từng thành viên