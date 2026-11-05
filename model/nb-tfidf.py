"""
MODEL: Naive Bayes + TF-IDF

Multinomial Naive Bayes vốn dành cho số đếm nguyên, nhưng dùng với TF-IDF (số thực
không âm) vẫn chạy tốt: TF-IDF đóng vai trò "số đếm có trọng số".

Thử thêm ComplementNB: biến thể ước lượng tham số từ các lớp CÒN LẠI, thường ổn định
hơn khi dữ liệu lệch lớp (ở đây ham ≈ 4,7 lần spam).

Siêu tham số dò: loại Naive Bayes (Multinomial / Complement) và alpha.

Chạy (đứng trong thư mục BTL1, sau khi đã chạy preprocess.py và tfidf.py):
    python 3_model/nb-tfidf.py
"""
from sklearn.naive_bayes import ComplementNB, MultinomialNB
from sklearn.pipeline import Pipeline

from evaluate import run_experiment

ALPHAS = [0.001, 0.003, 0.01, 0.03, 0.1, 0.3, 1.0]

# Pipeline chỉ có 1 bước tên "nb". Bước này được GridSearchCV thay lần lượt bằng
# MultinomialNB rồi ComplementNB, nhờ đó dò được cả LOẠI mô hình lẫn alpha.
estimator = Pipeline([("nb", MultinomialNB())])
param_grid = [
    {"nb": [MultinomialNB()], "nb__alpha": ALPHAS},   # thử MultinomialNB với từng alpha
    {"nb": [ComplementNB()], "nb__alpha": ALPHAS},    # thử ComplementNB với từng alpha
]

if __name__ == "__main__":
    run_experiment(
        model_name="nb-tfidf",
        feature="tfidf",
        estimator=estimator,
        param_grid=param_grid,
        note="Naive Bayes (Multinomial / Complement) trên vector TF-IDF",
    )