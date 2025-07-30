import turtle


t = turtle.Turtle()
t.shape("turtle")
t.pencolor("skyblue")
t.pensize(3)
t.speed(1)

for i in range(5):
    t.right(360 / 5)
    t.forward(70)

turtle.exitonclick()
