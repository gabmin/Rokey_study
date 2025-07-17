# a = [1, 2, 3, 4]
# a[0], a[3] = a[3], a[0]
#
# print(a)


# arr = [3, 6, 9, 12]
# arr[0], arr[2] = arr[2], arr[0]
#
# print(arr)
#
# a = [1, 2, 3]
# b = a
#
# print(id(a) == id(b))
#
# x = 42
# y = 42
#
# print(id(x) == id(y))

# c = [10, 20, 30]
# d = c.copy()
# print(id(c) == id(d))


# arr = [4, 32, 12, 8, 22]
#
# max_value = 0
#
# for i in arr:
#     if i > max_value:
#         max_value = i
#
# print(max_value)

dict = {"a": 10, "b": 20, "c": 30}


def sum_dict(dic):
    values = dic.values()
    total = 0
    for value in values:
        total += value
    return total


print(sum_dict(dict))
