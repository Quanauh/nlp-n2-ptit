"""
MODEL: Naive Bayes + Word Embedding

Vector WE là vector DÀY, giá trị thực có thể ÂM -> KHÔNG dùng được MultinomialNB
(nó yêu cầu đặc trưng không âm, dạng đếm).

Dùng Gaussian Naive Bayes: giả sử mỗi chiều của vector, trong từng lớp, theo phân phối
chuẩn N(μ, σ²) và các chiều độc lập với nhau:

    P(spam | x) ∝ P(spam) · Π_j N(x_j ; μ_j,spam , σ²_j,spam)

Giả định "các chiều độc lập" khá sai với embedding (các chiều tương quan mạnh), nên
NB + WE thường là tổ hợp yếu nhất. Đây cũng là một điểm đáng phân tích trong báo cáo.

Siêu tham số dò: var_smoothing (cộng thêm một lượng nhỏ vào phương sai để ổn định).

Chạy (đứng trong thư mục BTL1, sau khi đã chạy preprocess.py và WE.py):
    python 3_model/nb-we.py
"""
import numpy as np
from sklearn.naive_bayes import GaussianNB

from evaluate import run_experiment

VAR_SMOOTHING = np.logspace(-12, -1, 12).tolist()   # 12 giá trị từ 1e-12 đến 1e-1

if __name__ == "__main__":
    run_experiment(
        model_name="nb-we",
        feature="we",
        estimator=GaussianNB(),
        param_grid={"var_smoothing": VAR_SMOOTHING},
        note="GaussianNB trên vector Word2Vec trung bình của câu",
    )