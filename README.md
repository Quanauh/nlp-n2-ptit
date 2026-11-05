# BTL1 — Phân loại bình luận Spam / Ham tiếng Việt

Dự án xây dựng pipeline máy học phân loại bình luận sản phẩm thương mại điện tử thành **Spam** (quảng cáo, rác, chèo kéo) hoặc **Ham** (bình luận hợp lệ, đánh giá thật của người dùng).

---

## 1. Cấu trúc thư mục

```text
nlp-n2-ptit/
├── data/
│   ├── raw/                                        # Dữ liệu gốc
│   │   ├── reviews_spam_ham_chuan.csv
│   │   └── reviews_spam_ham_filtered_augmented.csv
│   └── processed/                                  # Dữ liệu sau tiền xử lý
│       └── processed.csv                           # Đã làm sạch, lọc trùng, gắn nhãn train/test
├── preprocess/
│   └── preprocess.py                               # Làm sạch, chuẩn hóa teencode, loại bỏ trùng, chia train/test 80/20
├── feature_extraction/
│   ├── bow.py                                      # Trích chọn đặc trưng Bag-of-Words (n-gram 1-2)
│   ├── tfidf.py                                    # Trích chọn đặc trưng TF-IDF (n-gram 1-2, L2 norm)
│   ├── WE.py                                       # Huấn luyện Word2Vec (Skip-gram) và tạo vector embedding
│   └── features/                                   # Thư mục lưu file đặc trưng và vectorizer (.pkl, .model)
│       ├── bow.pkl, bow_vectorizer.pkl
│       ├── tfidf.pkl, tfidf_vectorizer.pkl
│       └── we.pkl, we_word2vec.model
├── model/
│   ├── evaluate.py                                 # Module dùng chung: GridSearchCV 5-fold, đánh giá, ghi log
│   ├── nb-bow.py                                   # Multinomial Naive Bayes + BoW
│   ├── nb-tfidf.py                                 # Complement Naive Bayes + TF-IDF
│   ├── nb-we.py                                    # Gaussian Naive Bayes + Word Embedding
│   ├── svm-bow.py                                  # Linear SVM + BoW
│   ├── svm-tfidf.py                                # Linear SVM + TF-IDF
│   └── svm-we.py                                   # RBF SVM (Pipeline StandardScaler) + Word Embedding
├── results/                                        # Kết quả thực nghiệm từng mô hình
│   ├── summary.csv                                 # Bảng tổng hợp performance tất cả các mô hình
│   ├── <model>.json                                # Chỉ số chi tiết (Accuracy, F1, ROC-AUC, CV score, ...)
│   ├── <model>.pkl                                 # Trọng số mô hình đã huấn luyện
│   ├── <model>_confusion_matrix.png               # Ma trận nhầm lẫn trực quan hóa
│   └── <model>_errors.csv                          # Danh sách các câu phân loại sai để phân tích lỗi
├── main.py
├── requirements.txt
└── README.md
```

---

## 2. Cài đặt môi trường

Cài đặt các gói thư viện cần thiết:

```bash
pip install -r requirements.txt
pip install matplotlib scipy joblib
```

Danh sách thư viện chính:
- `pandas`, `numpy`: Xử lý và thao tác dữ liệu bảng.
- `scikit-learn`: Tiền xử lý, trích xuất đặc trưng (BoW, TF-IDF), các mô hình phân loại và hàm đánh giá.
- `gensim`: Huấn luyện mô hình biểu diễn từ Word2Vec (Skip-gram).
- `matplotlib`: Trực quan hóa ma trận nhầm lẫn.
- `joblib`: Lưu trữ và nạp các ma trận đặc trưng, pipeline và mô hình.

---

## 3. Hướng dẫn chạy

Chạy các lệnh bên dưới từ thư mục gốc của dự án (`nlp-n2-ptit/`):

### Bước 1: Tiền xử lý dữ liệu và chia tập Train / Test
```bash
python preprocess/preprocess.py --input data/raw/reviews_spam_ham_filtered_augmented.csv
```
- **Đầu vào**: File dữ liệu gốc trong `data/raw/`.
- **Đầu ra**: `data/processed/processed.csv` (gồm 3.856 mẫu train và 964 mẫu test, phân tầng theo nhãn).

### Bước 2: Trích chọn đặc trưng
```bash
# 1. Bag-of-Words
python feature_extraction/bow.py

# 2. TF-IDF
python feature_extraction/tfidf.py

# 3. Word Embedding (Word2Vec)
python feature_extraction/WE.py
```
- **Đầu ra**: Các file đặc trưng `.pkl` và vectorizer / model tương ứng được lưu trong thư mục `feature_extraction/features/`.

### Bước 3: Huấn luyện và đánh giá mô hình
Có thể chạy từng mô hình riêng lẻ:

```bash
# Mô hình Naive Bayes
python model/nb-bow.py
python model/nb-tfidf.py
python model/nb-we.py

# Mô hình SVM
python model/svm-bow.py
python model/svm-tfidf.py
python model/svm-we.py
```

Mỗi mô hình khi chạy sẽ:
1. Dò tìm siêu tham số tối ưu bằng **5-Fold Stratified Cross-Validation** trên tập Train (tiêu chí tối ưu là F1-score của lớp Spam).
2. Huấn luyện lại trên toàn bộ tập Train và kiểm thử trên tập Test (964 mẫu).
3. In kết quả chi tiết: Accuracy, Precision, Recall, F1-score (Spam), Macro F1, ROC-AUC, PR-AUC, Confusion Matrix, Classification Report và các ví dụ đoán sai.
4. Tự động lưu checkpoint, ma trận nhầm lẫn dạng ảnh, phân tích lỗi và cập nhật bảng so sánh tổng hợp vào `results/summary.csv`.

---

## 4. Kết quả thực nghiệm

Kết quả kiểm thử trên tập Test (964 mẫu, gồm 758 câu Ham và 206 câu Spam, tỉ lệ Spam ~21.4%):

| Mô hình | Đặc trưng | Accuracy | Precision (Spam) | Recall (Spam) | F1-Score (Spam) | F1 Macro | ROC-AUC | PR-AUC |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **SVM (RBF Kernel)** | **Word2Vec (WE)** | **95.64%** | **91.41%** | 87.86% | **89.60%** | **93.42%** | **0.9779** | **0.9340** |
| **SVM (Linear)** | BoW | 95.02% | 84.35% | **94.17%** | 88.99% | 92.89% | 0.9772 | 0.9078 |
| **SVM (Linear)** | TF-IDF | 94.61% | 85.98% | 89.32% | 87.62% | 92.09% | 0.9737 | 0.8950 |
| **Complement Naive Bayes** | TF-IDF | 93.98% | 84.58% | 87.86% | 86.19% | 91.17% | 0.9747 | 0.9212 |
| **Multinomial Naive Bayes** | BoW | 93.98% | 87.76% | 83.50% | 85.57% | 90.89% | 0.9739 | 0.9125 |
| **Gaussian Naive Bayes** | Word2Vec (WE) | 80.91% | 54.17% | 69.42% | 60.85% | 74.12% | 0.8754 | 0.5862 |

---

## 5. Các lưu ý quan trọng trong thiết kế hệ thống

1. **Loại bỏ trùng lặp trước khi chia Train / Test**:
   - Dữ liệu thô có hơn 50% câu đánh giá trùng lặp ngắn (như *"Tốt"*, *"Ok"*, *"Hàng đẹp"*...).
   - Nếu chia ngẫu nhiên trước khi lọc trùng, các câu giống hệt nhau sẽ rơi vào cả tập Train và Test (data leakage), dẫn đến điểm số test cao ảo. Việc lọc trùng câu sau khi làm sạch đảm bảo mô hình thực sự học được năng lực tổng quát hóa.
2. **Chia Train / Test phân tầng và dùng chung**:
   - Chia một lần duy nhất ở bước tiền xử lý theo tỷ lệ 80/20 có phân tầng theo nhãn (`stratified`).
   - Cả 3 phương pháp trích xuất đặc trưng (BoW, TF-IDF, WE) dùng chung một phân chia này, bảo đảm tính công bằng tuyệt đối khi so sánh các mô hình.
3. **Chống rò rỉ thông tin (Data Leakage)**:
   - Các bộ vectorizer (`CountVectorizer`, `TfidfVectorizer`) và mô hình Word2Vec **chỉ được `fit` trên tập Train**, tập Test chỉ thực hiện `transform`.
   - Với SVM trên Word2Vec, bộ chuẩn hóa `StandardScaler` được đặt trong `Pipeline` để đảm bảo khi Cross-Validation, thang đo chỉ được tính trên các fold train con.
4. **Đánh giá trên tập dữ liệu lệch lớp (Imbalanced Data)**:
   - Tỷ lệ Spam trong tập dữ liệu là ~21.4%.
   - Do dữ liệu mất cân bằng, chỉ số **F1-score lớp Spam** và **PR-AUC** được ưu tiên làm tiêu chí đánh giá cốt lõi thay vì chỉ dựa vào Accuracy thông thường.
