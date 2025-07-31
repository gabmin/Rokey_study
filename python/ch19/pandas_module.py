import pandas as pd


data = [10, 20, 30]
series = pd.Series(data)

data2 = [[1, "Alice", 30], [2, "Bob", 35], [3, "Charlie", 25]]

df = pd.DataFrame(data2, columns=["ID", "Name", "Age"])

data3 = {
    "ID": [1, 2, 3],
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [20, 35, 25],
}

df2 = pd.DataFrame(data3)

print(series)
print(df)
print(df2)
