import turtle

t = turtle.Turtle()
t.shape("turtle")
t.pencolor("skyblue")
t.color("black", "gold")

t.pensize(3)
t.speed(1)


n = int(input("입력: "))

t.begin_fill()
for i in range(n):
    t.right(360 / n)
    t.forward(70)
t.end_fill()


turtle.exitonclick()
