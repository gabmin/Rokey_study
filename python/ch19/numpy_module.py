import numpy as np

arr = np.array([1, 2, 3, 4, 5])

print(arr)
print(arr.shape)
print(arr.dtype)

print("0으로 초기화 된 배열 --------------")
zeros = np.zeros((3, 3))
print(zeros)

print("값으로 채운 배열 -----------------")
full = np.full((3, 3), 7)
print(full)

print("단위 행렬-----------------------")
id1 = np.eye(2, 3)
print(id1)
id2 = np.identity(3)
print(id2)

print("난수 배열-----------------------")
random = np.random.random((3, 3))
print(random)

print("정수 난수 배열 (범위) ------------------")
random1 = np.random.randint(1, 10, (3, 3))
print(random1)

print("기본 산술 연산 ---------------------")
arr = np.array([1, 2, 3, 4, 5])
print(arr + 5)
print(arr * 2)

print(arr.sum())
print(arr.mean())
print(arr.max())
print(arr.min())


print("브로드캐스팅----------------------")
arr1 = np.array([1, 2, 3])
arr2 = np.array([[1], [2], [3]])
result = arr1 + arr2
print(result)

print("선형 대수 연산-------------------")
matrix1 = np.array([[1, 2], [3, 4]])
matrix2 = np.array([[5, 6], [7, 8]])
result = np.dot(matrix1, matrix2)  # 행렬 곱
"""
  1  2   x   5  6
  3  4       7  8
  
  1 x 5 + 2 x 7     1 x 6 + 2 x 8
  3 x 5 + 4 x 7     3 x 6 + 4 x 8
"""
print(result)

print("기본 인덱싱 및 슬라이싱 --------------------")
arr3 = np.array([10, 20, 30, 40])
print(arr3[2])

arr4 = np.array([[1, 2, 3], [4, 5, 6]])
print(arr4[1, 2])

print(arr4[0, :])
print(arr4[:, 1])


print("조건부 필더링 --------------------------")
arr5 = np.array([1, 2, 3, 4, 5])
filtered = arr5[arr5 > 3]
print(filtered)

import pandas as pd

df = pd.DataFrame(arr5, columns=["values"])
print(df)
