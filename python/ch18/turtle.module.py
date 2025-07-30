import turtle


turtle.title("터틀 그래픽스")
turtle.setup(410, 310)
turtle.bgcolor("beige")

t = turtle.Turtle()

t.shape("turtle")

# 커서 색상
t.color("black", "green")

# 회전
# t.right(180)
# t.left(90)

# 문자열 출력
t.write("거북이", font=("바탕체", 30, "bold"))

# 속도
t.speed(1)

# 펜 색상
t.pencolor("blue")
t.pensize(3)

# 이동
# 그리기
t.penup()
t.forward(80)

t.pendown()
t.backward(100)


t.left(90)
t.fd(50)
t.right(90)
t.fd(150)
t.right(90)
t.fd(50)
t.right(90)
t.fd(150)
t.left(180)


# 초기화
t.reset()

turtle.mainloop()
