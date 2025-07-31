import turtle

turtle.setup(800, 600)
turtle.bgcolor("black")

moon = turtle.Turtle()
moon.shape("turtle")
star = turtle.Turtle()
star.shape("turtle")


def drawMoon(x, y, size, color):
    moon.penup()
    moon.goto(x, y)
    moon.pendown()

    moon.color(color)

    moon.begin_fill()
    moon.circle(size)
    moon.end_fill()


def drawStar(x, y, size, color):
    star.color(color)

    star.penup()
    star.goto(x, y)
    star.pendown()

    for i in range(5):
        star.fd(size)
        star.right(144)


moon_x = int(input("달의 x 좌표를 입력하세요 : "))
moon_y = int(input("달의 y 좌표를 입력하세요: "))
moon_size = int(input("달의 크기를 입력하세요: "))
moon_color = input("달의 색상을 입력하세요: ")

star_x = int(input("별의 x 좌표를 입력하세요 : "))
star_y = int(input("별의 y 좌표를 입력하세요: "))
star_size = int(input("별의 크기를 입력하세요: "))
star_color = input("별의 색상을 입력하세요: ")

drawMoon(moon_x, moon_y, moon_size, moon_color)
drawStar(star_x, star_y, star_size, star_color)

moon.hideturtle()
star.hideturtle()

turtle.exitonclick()
