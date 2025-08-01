from sklearn import svm
from sklearn import metrics
import pandas as pd


xor_data = [
    # P  Q  result
    [0, 0, 0],
    [0, 1, 1],
    [1, 0, 1],
    [1, 1, 0],
]

xor_df = pd.DataFrame(xor_data)

data = xor_df.loc[:, 0:1]  # 1열, 2열
label = xor_df.loc[:, 2]  # 3열

clf = svm.SVC()  # 알고리즘 선택

clf.fit(data, label)

# 데이터 예측하기
pre = clf.predict(data)

print(pre)

# 결과 확인
ac_score = metrics.accuracy_score(label, pre)
print(f"정답률: {ac_score}")
