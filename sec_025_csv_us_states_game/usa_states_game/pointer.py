from turtle import Turtle

class Pointer(Turtle):
    
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        
    def new_state(self, state, x_pos, y_pos):
        self.home()
        self.goto(x=x_pos, y=y_pos)
        self.write(state, align="center")
        
    