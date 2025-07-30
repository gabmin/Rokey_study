import turtle

turtle.title("사각형 그리기")
turtle.setup(500, 500)

t = turtle.Turtle()

t.pencolor("skyblue")
t.pensize(5)
t.shape("turtle")
t.speed(1)

for i in range(4):
    t.right(90)
    t.fd(70)


turtle.exitonclick()
