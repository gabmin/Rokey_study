# def is_odd(num):
#     if num % 2 == 0:
#         print("짝수 입니다.")
#     else:
#         print("홀수 입니다.")
#
#
# is_odd(5)


def list_average(data):
    result = 0

    for i in data:
        result += i

    return result / len(data)


print(list_average([1, 2, 3, 4, 5]))
