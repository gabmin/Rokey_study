from sklearn.datasets import load_iris
import pandas as pd

iris = load_iris()

df = pd.DataFrame(data=iris.data, columns=iris.feature_names)

df["target"] = iris.target

# target = 0, 1, 2
# 0, 1, 2 를 setosa, versicolor, virginica 로 매핑
target_names = {
    0: iris.target_names[0],
    1: iris.target_names[1],
    2: iris.target_names[2],
}

df["target"] = df["target"].map(target_names)


from sklearn.model_selection import train_test_split

print(df)
iris_data = df[
    [
        "sepal length (cm)",
        "sepal width (cm)",
        "petal length (cm)",
        "petal width (cm)",
    ]
]
iris_label = df["target"]

train_data, test_data, train_label, test_label = train_test_split(
    iris_data, iris_label, test_size=0.3
)

from sklearn import svm, metrics

clf = svm.SVC()
clf.fit(train_data, train_label)
pre = clf.predict(test_data)

ac_score = metrics.accuracy_score(test_label, pre)
print("정답률 =", ac_score)
