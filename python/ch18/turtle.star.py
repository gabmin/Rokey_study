import turtle


turtle.setup(410, 310)
turtle.bgcolor("black")

star = turtle.Turtle()
star.speed(1)
star.pensize(2)

color = [
    "red",
    "green",
    "blue",
    "yellow",
    "magenta",
]


def draw_star():
    for i in range(5):
        star.pencolor(color[i])
        star.forward(100)
        star.right(144)


draw_star()
star.hideturtle()

turtle.mainloop()
