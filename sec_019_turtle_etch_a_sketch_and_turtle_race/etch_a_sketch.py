from turtle import Turtle, Screen, clear

tim = Turtle()
screen = Screen()


def move_forwards():
    tim.forward(10)

def turn_left():
    tim.lt(10)

def turn_right():
    tim.rt(10)
    
def move_backward():
    tim.backward(10)

def reset_screen():
    tim.reset()


screen.listen()
screen.onkeypress(key="w", fun=move_forwards)
screen.onkeypress(key="a", fun=turn_left)
screen.onkeypress(key="d", fun=turn_right)
screen.onkeypress(key="s", fun=move_backward)
screen.onkeypress(key="c", fun=reset_screen)
screen.exitonclick()





