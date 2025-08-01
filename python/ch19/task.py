import pandas as pd

data = pd.read_csv("./data.csv")

print(
    f"Age 평균: {data['Age'].mean()}, "
    f"최댓값: {data['Age'].max()}, "
    f"최솟값: {data['Age'].min()}"
)

print(
    f"Salary 평균: {data['Salary'].mean()}, "
    f"최댓값: {data['Salary'].max()}, "
    f"최솟값: {data['Salary'].min()}"
)


df_data = pd.DataFrame(data)

print(df_data[df_data["Age"] >= 30])


import numpy as np

array = np.array(range(1, 11))

print(f"원본 배열: {array}")
print(f"제곱 배열: {array**2}")
print(f"평균: {array.mean()}, 최댓값: {array.max()}, 최솟값: {array.min()}")


array1 = np.random.randint(1, 12, (3, 4))
print(f"원본 행렬: \n {array1}")
print(f"각 행의 최댓값: {array1.max(axis=1)}")


import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 4, 5, 8, 10]

plt.rcParams["font.family"] = "Malgun Gothic"
plt.rcParams["axes.unicode_minus"] = False

plt.plot(x, y)
plt.xlabel("x축")
plt.ylabel("y축")
plt.grid(True)

plt.show()
