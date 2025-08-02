import statsmodels.api as sm
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]


X = sm.add_constant(x)

model = sm.OLS(y, X).fit()

const = model.params[0]
hp = model.params[1]

y_pred = list(map(lambda i: hp * i + const, x))


plt.plot(x, y_pred, color="red")
plt.scatter(x, y_pred, color="skyblue")
plt.title("Linear Regression")
plt.xlabel("x")
plt.ylabel("y")

plt.show()


from sklearn import svm

X = [[1], [2], [3], [4], [5], [6], [7], [8], [9], [10]]
y = [0, 0, 0, 0, 1, 1, 1, 1, 1, 1]

clf = svm.SVC()

clf.fit(X, y)

pre = clf.predict([[4.5], [6.5]])

print(pre)


from scipy.optimize import root


def equation(x):
    return (x - 3) ** 2


sol = root(equation, x0=1)
print(sol.x)


from scipy.stats import describe

data = [80, 85, 90, 75, 95]
stats = describe(data)
print(stats)
