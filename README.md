# BTL1 — Phân loại bình luận Spam / Ham tiếng Việt

Dự án xây dựng pipeline máy học phân loại bình luận sản phẩm thương mại điện tử thành **Spam** (quảng cáo, rác, chèo kéo) hoặc **Ham** (bình luận hợp lệ, đánh giá thật của người dùng).

---

## 1. Cấu trúc thư mục

```text
nlp-n2-ptit/
├── data/
│   ├── raw/                                        # Dữ liệu thu thập chưa gán nhãn
│   │   └── commentdienmayxanh.csv                  # Đánh giá nguồn từ Điện Máy Xanh
│   ├── labeled/                                    # Các bộ dữ liệu đã gán nhãn
│   │   └── reviews_spam_ham.csv
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
├── data_collection/                                # Mã thu thập dữ liệu nguồn
│   ├── main.py
│   └── README.md
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

### Bước 1: Tiền xử lý dữ liệu

Lệnh này làm sạch văn bản, lọc câu trùng và tạo một lần chia Train/Test dùng chung cho BoW, TF-IDF và Word2Vec:

```bash
python preprocess/preprocess.py --input data/labeled/reviews_spam_ham.csv
```

Đầu ra: `data/processed/processed.csv`. Có thể xem nhanh dữ liệu đã chia bằng:

```bash
python -c "import pandas as pd; d=pd.read_csv('data/processed/processed.csv'); print(d.groupby(['split','label']).size()); print(d[['review','clean_text','label','split']].head())"
```

### Bước 2: Tạo đặc trưng

Chạy cả ba lệnh để sẵn sàng demo đủ sáu tổ hợp Naive Bayes/SVM với BoW, TF-IDF và Word2Vec:

```bash
# Bag-of-Words: tạo ma trận đếm và vectorizer
python feature_extraction/bow.py

# TF-IDF: tạo ma trận trọng số và vectorizer
python feature_extraction/tfidf.py

# Word Embedding: huấn luyện Word2Vec trên train và tạo vector câu
python feature_extraction/WE.py
```

Đầu ra được lưu trong `feature_extraction/features/`. Nếu chỉ demo một mô hình, chỉ cần chạy bước tạo đặc trưng tương ứng trước đó.

### Bước 3: Demo từng mô hình

Mỗi lệnh dưới đây dò siêu tham số bằng 5-fold cross-validation trên tập train, sau đó đánh giá trên tập test. Các lệnh có thể chạy độc lập sau khi đã tạo đặc trưng tương ứng:

```bash
# Naive Bayes + BoW
python model/nb-bow.py

# Naive Bayes + TF-IDF
python model/nb-tfidf.py

# Naive Bayes + Word Embedding (Word2Vec)
python model/nb-we.py

# SVM tuyến tính + BoW
python model/svm-bow.py

# SVM tuyến tính + TF-IDF
python model/svm-tfidf.py

# SVM RBF + Word Embedding (Word2Vec)
python model/svm-we.py
```

Mỗi lần chạy sẽ in các chỉ số, ma trận nhầm lẫn và ví dụ dự đoán sai; đồng thời cập nhật `results/summary.csv` và lưu mô hình, JSON, ảnh ma trận nhầm lẫn, CSV lỗi vào `results/`.

### Bước 4: Demo FastText

FastText là pipeline độc lập, tự đọc và chia dữ liệu từ `data/labeled/reviews_spam_ham.csv`; không cần chạy trước các bước tiền xử lý/trích đặc trưng ở trên. Cài dependency riêng và chạy từ thư mục gốc:

```bash
pip install -r FastText_Performance/requirements.txt
python FastText_Performance/main.py
```

Có thể truyền một CSV khác nếu file có hai cột `review` và `label` (0 = ham, 1 = spam):

```bash
python FastText_Performance/main.py data/labeled/reviews_spam_ham.csv
```

FastText in các chỉ số đánh giá ra terminal, nhưng không lưu checkpoint hoặc kết quả vào `results/`.

### Chạy toàn bộ demo lần lượt

Sau khi cài dependencies, có thể copy/chạy nguyên khối dưới đây từ thư mục gốc:

```bash
python preprocess/preprocess.py --input data/labeled/reviews_spam_ham_filtered_augmented.csv
python feature_extraction/bow.py
python feature_extraction/tfidf.py
python feature_extraction/WE.py
python model/nb-bow.py
python model/nb-tfidf.py
python model/nb-we.py
python model/svm-bow.py
python model/svm-tfidf.py
python model/svm-we.py
pip install -r FastText_Performance/requirements.txt
python FastText_Performance/main.py
```

Các lệnh huấn luyện có thể mất thời gian do dò siêu tham số; để demo riêng từng mô hình, chỉ chạy script đặc trưng tương ứng và script mô hình tương ứng.

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

## ✅ Chạy dự án bằng Docker

### Bước 1 — Kiểm tra Docker đã cài chưa

docker --version

### Bước 2 — Build image từ Dockerfile có sẵn

docker build -t nlp-n2-ptit .

### Bước 3 — Chạy container (mount thư mục để lưu kết quả ra ngoài)

docker run -it --rm \
  -v $(pwd)/data:/app/data \
  -v $(pwd)/results:/app/results \
  -v $(pwd)/feature_extraction/features:/app/feature_extraction/features \
  nlp-n2-ptit bash

———

### Bước 4 — Trong container, chạy lần lượt:

# Tiền xử lý
python preprocess/preprocess.py --input data/labeled/reviews_spam_ham.csv

# Trích chọn đặc trưng
python feature_extraction/bow.py
python feature_extraction/tfidf.py
python feature_extraction/WE.py

# Huấn luyện mô hình
python model/nb-bow.py
python model/nb-tfidf.py
python model/nb-we.py
python model/svm-bow.py
python model/svm-tfidf.py
python model/svm-we.py

# FastText (cài dependency riêng)
pip install -r FastText_Performance/requirements.txt
python FastText_Performance/main.py

———
