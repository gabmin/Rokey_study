import pandas as pd

df_csv = pd.read_csv("./data.csv")

print(df_csv)
print("-------------")
print(df_csv.head())
print("-------------")
print(df_csv.tail())
print("-------------")
print(df_csv.info())
print("-------------")
print(df_csv.describe())
print("-------------")
print(df_csv.sample(2))  # 랜덤 샘플
print("-------------")
print(df_csv.sample(frac=0.5))
