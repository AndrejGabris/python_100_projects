from turtle import Turtle, Screen

timmy_the_turtle = Turtle()
# timmy_the_turtle.shape("turtle")
# timmy_the_turtle.color("red")






# DRAW a square

# for _ in range(4):
#     timmy_the_turtle.forward(100)
#     timmy_the_turtle.rt(90)




# DRAW a dashed line

# for _ in range(15):
#     timmy_the_turtle.pd()
#     timmy_the_turtle.forward(10)
#     timmy_the_turtle.pu()
#     timmy_the_turtle.forward(10)





# DRAW a n-tagons every n-tagon is drawn by random color

# import random
# for i in range(3, 11):
#     count = 1
#     r = random.random()
#     g = random.random()
#     b = random.random()
#     color_pallet = (r, g, b) #tuple (0,1)
#     timmy_the_turtle.pencolor(color_pallet)
#     while count <= i:
#         timmy_the_turtle.forward(100)
#         timmy_the_turtle.rt(360/i)
#         count += 1





# DRAW a radnom walk with random color

# import random
# counter = 0
# timmy_the_turtle.pensize(10)
# timmy_the_turtle.speed("fastest")
# while counter < 200:
#     timmy_the_turtle
#     r = random.random()
#     g = random.random()
#     b = random.random()
#     color_pallet = (r, g, b) #tuple (0,1)
#     timmy_the_turtle.pencolor(color_pallet)
#     timmy_the_turtle.forward(30)
#     random_angle = random.choice([0, 90, 180, 270])
#     timmy_the_turtle.rt(random_angle)
#     counter += 1





# DRAW a spyrograph

import random
timmy_the_turtle.speed("fastest")
angle = 5
circle_radius = 100
for _ in range(0,361, angle):
    timmy_the_turtle
    r = random.random()
    g = random.random()
    b = random.random()
    color_pallet = (r, g, b) #tuple (0,1)
    timmy_the_turtle.pencolor(color_pallet)
    timmy_the_turtle.circle(circle_radius)
    timmy_the_turtle.lt(angle)





screen = Screen()
screen.exitonclick()
