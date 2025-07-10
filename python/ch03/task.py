# value = int(input("숫자를 입력하세요."))
#
# if value % 2 == 0:
#     print("해당 숫자는 짝수입니다.")
# else:
#     print("해당 숫자는 홀수입니다.")


# value = int(input("값을 입력하세요."))
#
# result = value + 20
#
# if value > 255 or result > 255:
#     print(255)
# else:
#     print(result)

# value = int(input("값을 입력하세요."))
#
# result = value - 20
#
# if result < 0:
#     print(0)
# elif result > 255:
#     print(255)
# else:
#     print(result)

# value = input("시간을 입력하세요.")
#
# minute = value[-2:]
#
# if minute == "00":
#     print("정각 입니다.")
# else:
#     print("정각이 아닙니다.")


value = int(input("점수를 입력하세요."))

if 81 <= value <= 100:
    print("A")
elif 61 <= value <= 80:
    print("B")
elif 41 <= value <= 60:
    print("C")
elif 21 <= value <= 40:
    print("D")
else:
    print("E")