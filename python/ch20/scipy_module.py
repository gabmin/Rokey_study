from scipy.linalg import solve

A = [[3, 1], [1, 2]]
b = [9, 8]

x = solve(A, b)
print(x)


from scipy.optimize import minimize, root


def f(x):
    return x**2 + 4 * x + 4


result = minimize(f, x0=0)
print(result.x)


def equation(x):
    return x**2 - 4


sol = root(equation, x0=2)
print(sol.x)


from scipy.sparse import csr_matrix

data = [[0, 0, 3], [4, 0, 0], [0, 5, 0]]

sparse_matrix = csr_matrix(data)
print(sparse_matrix)
