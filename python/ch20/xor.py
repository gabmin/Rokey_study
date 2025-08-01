from sklearn import svm
from sklearn import metrics

clf = svm.SVC()  # 알고리즘 선택

clf.fit(  #  학습
    [
        [0, 0],
        [0, 1],
        [1, 0],
        [1, 1],
    ],
    [0, 1, 1, 0],  # 레이블 (정답)
)

# 데이터 예측하기
pre = clf.predict([[0, 1], [1, 1]])

print(pre)

# 결과 확인
ac_score = metrics.accuracy_score([1, 0], pre)
print(f"정답률: {ac_score}")
