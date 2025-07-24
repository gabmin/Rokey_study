# try:
#     x = int("abc")
# except (ValueError, TypeError):
#     print("ValueError occurred!")
# finally:
#     print("Execution finished.")


# try:
#     x = 10 / 0
# except ZeroDivisionError:
#     print("Cannot divide by zero!")


# a = {}
# a["A"] = "Apple"
# a["B"] = "Banana"
#
# try:
#     data = a["C"]
#     print(data)
# except KeyError:
#     print("Key is missing!")


# add = lambda x, y: x + y
# print(add(3, 5))


# per = ["10.31", "", "8.00"]
#
# for i in per:
#     try:
#         print(float(i))
#     except ValueError:
#         print(0)

a = int(input("첫번째 값을 입력하세요."))
b = int(input("두번재 값을 입력하세요."))

try:
    print(a / b)
except ZeroDivisionError:
    print("0으로 나눌 수 없습니다.")
