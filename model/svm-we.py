"""
MODEL: SVM + Word Embedding

Vector WE chỉ có ~100 chiều và dày, nên khác BoW/TF-IDF, dữ liệu khó tách tuyến tính
hơn -> dùng SVC với nhân RBF (Gaussian) để học biên phi tuyến:

    K(x, x') = exp(-gamma · ||x - x'||²)

Trước SVM có StandardScaler (đưa mỗi chiều về trung bình 0, độ lệch chuẩn 1) vì nhân RBF
dựa trên khoảng cách: chiều nào có thang đo lớn sẽ lấn át các chiều khác. Scaler nằm
TRONG Pipeline nên khi cross-validation nó chỉ fit trên phần train của mỗi fold
(không rò rỉ).

Siêu tham số dò: C, gamma, class_weight.

Chạy (đứng trong thư mục BTL1, sau khi đã chạy preprocess.py và WE.py):
    python 3_model/svm-we.py
"""
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC

from evaluate import run_experiment

# Pipeline gồm 2 bước: chuẩn hóa thang đo rồi SVM. Tên tham số dạng "<tên bước>__<tham số>".
estimator = Pipeline([
    ("scaler", StandardScaler()),
    ("svm", SVC(kernel="rbf", random_state=42)),
])
param_grid = {
    "svm__C": [0.1, 1.0, 10.0, 100.0],
    "svm__gamma": ["scale", 0.001, 0.01, 0.1],
    "svm__class_weight": [None, "balanced"],
}

if __name__ == "__main__":
    run_experiment(
        model_name="svm-we",
        feature="we",
        estimator=estimator,
        param_grid=param_grid,
        note="SVC (nhân RBF) + StandardScaler trên vector Word2Vec trung bình của câu",
    )