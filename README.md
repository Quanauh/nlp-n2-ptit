BTL1 — Phân loại bình luận spam/ham
Cấu trúc thư mục
BTL1/
├── data/
│   ├── raw/reviews_spam_ham_filtered_augmented.csv   # dữ liệu gốc
│   └── processed/processed.csv                       # (sinh ra) dữ liệu sau tiền xử lí
├── 1_tien_xu_li/
│   └── preprocess.py        # làm sạch, bỏ trùng, chia train/test 80/20
├── 2_trich_chon_dac_trung/
│   ├── bow.py               # -> features/bow.pkl
│   ├── tfidf.py             # -> features/tfidf.pkl
│   └── WE.py                # -> features/we.pkl (Word2Vec, gensim)
├── 3_model/
│   ├── evaluate.py          # hàm dùng chung: grid search + in performance
│   ├── nb-bow.py   nb-tfidf.py   nb-we.py
│   └── svm-bow.py  svm-tfidf.py  svm-we.py
├── features/                # (sinh ra) file đặc trưng
└── results/                 # (sinh ra) kết quả từng model + summary.csv
Cài đặt
pip install pandas numpy scikit-learn scipy joblib gensim matplotlib
Chạy (đứng ở thư mục BTL1/)
# Bước 1: tiền xử lí
python 1_tien_xu_li/preprocess.py

# Bước 2: trích chọn đặc trưng
python 2_trich_chon_dac_trung/bow.py
python 2_trich_chon_dac_trung/tfidf.py
python 2_trich_chon_dac_trung/WE.py

# Bước 3: huấn luyện + in performance (chạy file nào cũng được)
python 3_model/nb-bow.py
python 3_model/nb-tfidf.py
python 3_model/nb-we.py
python 3_model/svm-bow.py
python 3_model/svm-tfidf.py
python 3_model/svm-we.py
Mỗi file model in ra: siêu tham số tốt nhất (5-fold CV trên train), Accuracy, Precision / Recall / F1 lớp spam, F1 macro, ROC-AUC, PR-AUC, ma trận nhầm lẫn, classification report, thời gian train/predict và ví dụ đoán sai; cuối cùng in bảng so sánh mọi model đã chạy (results/summary.csv).

Lưu ý thiết kế
Bỏ trùng trước khi chia: ~56% dòng là câu lặp lại ("Tốt", "Ok"...). Không bỏ trùng thì cùng một câu nằm ở cả train và test -> điểm test bị thổi phồng.
Chia train/test một lần ở bước 1, cả 3 loại đặc trưng dùng chung -> so sánh công bằng.
Vectorizer / Word2Vec chỉ fit trên train, test chỉ transform.
Chọn siêu tham số bằng cross-validation trên train, tập test chỉ dùng để báo cáo.
Nhãn: 1 = spam, 0 = ham. Dữ liệu lệch lớp (spam ~17.5% sau bỏ trùng), nên F1 lớp spam là chỉ số chính, accuracy dễ gây ảo tưởng.