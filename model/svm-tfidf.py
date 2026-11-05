"""
MODEL: SVM + TF-IDF

LinearSVC trên vector TF-IDF, thường là baseline mạnh nhất cho phân loại văn bản cổ
điển: TF-IDF đã chuẩn hóa L2 nên câu dài/ngắn cùng thang đo, rất hợp với SVM.

Siêu tham số dò:
  - C: độ mạnh regularization (C nhỏ = lề rộng, mô hình đơn giản hơn).
  - class_weight: None hoặc "balanced" (tăng trọng số lỗi cho lớp spam ít mẫu).

Chạy (đứng trong thư mục BTL1, sau khi đã chạy preprocess.py và tfidf.py):
    python 3_model/svm-tfidf.py
"""
from sklearn.svm import LinearSVC

from evaluate import run_experiment

C_VALUES = [0.01, 0.05, 0.1, 0.5, 1.0, 5.0, 10.0]
CLASS_WEIGHTS = [None, "balanced"]

if __name__ == "__main__":
    run_experiment(
        model_name="svm-tfidf",
        feature="tfidf",
        estimator=LinearSVC(max_iter=20000, random_state=42),
        param_grid={"C": C_VALUES, "class_weight": CLASS_WEIGHTS},
        note="LinearSVC trên vector TF-IDF",
    )