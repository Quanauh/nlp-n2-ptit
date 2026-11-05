"""
MODEL: SVM + Bag of Words

SVM tìm siêu phẳng phân tách 2 lớp với LỀ (margin) lớn nhất. Với văn bản (vector thưa,
hàng chục nghìn chiều) dữ liệu thường gần như tách được tuyến tính, nên dùng LinearSVC
(SVM nhân tuyến tính, nhanh hơn SVC(kernel="linear") rất nhiều).

Siêu tham số dò:
  - C: nghịch đảo độ mạnh regularization. C nhỏ -> lề rộng, chấp nhận sai nhiều hơn
       (chống overfit); C lớn -> cố phân loại đúng mọi mẫu train.
  - class_weight = "balanced": phạt lỗi trên lớp spam (lớp ít) nặng hơn theo tỉ lệ
       nghịch tần suất -> tăng recall spam.

Chạy (đứng trong thư mục BTL1, sau khi đã chạy preprocess.py và bow.py):
    python 3_model/svm-bow.py
"""
from sklearn.svm import LinearSVC

from evaluate import run_experiment

C_VALUES = [0.001, 0.01, 0.05, 0.1, 0.5, 1.0, 5.0]
CLASS_WEIGHTS = [None, "balanced"]

if __name__ == "__main__":
    run_experiment(
        model_name="svm-bow",
        feature="bow",
        estimator=LinearSVC(max_iter=20000, random_state=42),
        param_grid={"C": C_VALUES, "class_weight": CLASS_WEIGHTS},
        note="LinearSVC trên vector đếm từ (BoW)",
    )