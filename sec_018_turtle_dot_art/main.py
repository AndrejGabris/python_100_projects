from turtle import Turtle, Screen, colormode
import random

color_list = [(202, 164, 109), (238, 240, 245), (150, 75, 49), (223, 201, 135), (52, 93, 124), (172, 154, 40), (140, 30, 19), (133, 163, 185), (198, 91, 71), (46, 122, 86), (72, 43, 35), (145, 178, 148), (13, 99, 71),
              (233, 175, 164), (161, 142, 158), (105, 74, 77), (55, 46, 50), (183, 205, 171), (36, 60, 74), (18, 86, 90), (81, 148, 129), (148, 17, 20), (14, 70, 64), (30, 68, 100), (107, 127, 153), (174, 94, 97), (176, 192, 209)]

turtle = Turtle()
turtle.speed("fastest")
turtle.hideturtle()
colormode(255)


def line_of_dots():
    turtle.setheading(0)
    random_color = random.choice(color_list)
    turtle.pencolor(random_color)
    turtle.dot(size=20)
    turtle.penup()
    turtle.forward(50)
     
for i in range(10):
    turtle.penup()
    turtle.home()
    turtle.setheading(225)
    turtle.forward(300)
    turtle.setheading(0)
    turtle.lt(90)
    y_postion = float((i+1)*50)
    turtle.forward(y_postion)
    for _ in range(10):
        line_of_dots()



screen = Screen()
screen.exitonclick()