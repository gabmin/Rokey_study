import statsmodels.api as sm

data = sm.datasets.get_rdataset("mtcars").data

print(data.head())


X = data[["hp", "wt"]]  # 마력 (독립변수)
y = data["mpg"]  # 연비 (종속변수)

X = sm.add_constant(X)  # 독립 변수 만들기

model = sm.OLS(y, X).fit()  # OSL 선형 회귀 알고리즘

print(model.summary())
