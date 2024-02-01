from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet.", prompt="Which turtle will win the race? Enter a color: ")

all_turtles = []
turtles_color = ["red", "orange", "yellow", "green", "blue", "black"]
turtles_x_start_position = -230
turtles_y_start_postions = [-70, -40, -10, 20, 50, 80]


for turtle_index in range(0, 6):
    new_turtle = Turtle("turtle")
    new_turtle.penup()
    new_turtle.color(turtles_color[turtle_index])
    new_turtle.goto(x=turtles_x_start_position, y=turtles_y_start_postions[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True
    
while is_race_on:
    
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            winning_turtle = turtle.pencolor()
            is_race_on = False
                                    
        random_distance = random.randint(10, 20)
        turtle.forward(random_distance)

if winning_turtle == user_bet:
    print(f"You have won! The {winning_turtle} turtle is the winner.")
else:
    print(f"You have lost! The {winning_turtle} turtle is the winner.")



screen.exitonclick()






