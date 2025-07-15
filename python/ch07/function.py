def swap_function(a, b):
    temp = a
    a = b
    b = temp
    return a, b


a = 10
b = 11

print(a, b)

a, b = swap_function(a, b)

print(a, b)


def global_swap_function(x, y):
    global a1, b1
    a1 = y
    b1 = x


a1 = 10
b1 = 11

print(a1, b1)

global_swap_function(a1, b1)

print(a1, b1)
