# num1 = int(input("첫번째 숫자를 입력하세요."))
# num2 = int(input("두번째 숫자를 입력하세요."))
#
# print(num1 + num2)
# print(num1 - num2)
# print(num1 * num2)
# print(num1 / num2)

# score = int(input("점수를 입력하세요."))
#
# if score >= 90:
#     print("A 학점")
# elif score >= 80:
#     print("B 학점")
# elif score >= 70:
#     print("C 학점")
# else:
#     print("F 학점")


# numbers = [1, 2, 3, 4, 5]
#
# for number in numbers:
#     print(number)

# age = int(input("나이를 입력하세요."))
#
# if 20 <= age <= 60:
#     print("적정 연령대입니다.")
# else:
#     print("적정 연령대가 아닙니다.")

# count = [1, 5, 9, 13, 9, 5, 1]
#
# for i in count:
#     print("*" * i)


fruits = ["바나나", "파인애플", "복숭아", "사과", "포도"]

for fruit in fruits:
    if fruit == "사과":
        print("사과를 찾았습니다.")
        break
    else:
        print(fruit)
