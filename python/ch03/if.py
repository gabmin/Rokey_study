na = 21
if na % 2 == 0:
    print(na, "짝수")
else:
    print(na, "홀수")

score = int(input("토익 점수를 입력해주세요."))

if score >= 900:
    print("당신의 토익 점수는", score, "상위권 점수입니다.")
elif score >= 700:
    print("당신의 토익 점수는", score, "중위권 점수입니다.")
else:
    print("당신의 토익 점수는", score, "하위권 점수입니다.")
