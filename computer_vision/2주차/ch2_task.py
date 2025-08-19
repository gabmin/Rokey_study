import numpy as np

arr1 = np.arange(12)
A = arr1.reshape(3, -1)

print(A)

B = A[1:, :3]

print(B)


sparse = np.zeros([4, 4])
sparse[1, 3] = 1

print(sparse)

array1 = [[1, 3, 5]]
array2 = [[2, 4, 6]]

array3 = np.concat((array1, array2), axis=1)
print(array3)


A = np.random.rand(3, 2)
mean = A.mean(axis=1)

print(mean)

C = np.random.randint(1, 21, (4, 3))
print(C)

def sigmoid(x, a):
    return 1/(1 + np.exp(-a*x))