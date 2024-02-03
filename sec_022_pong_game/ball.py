from turtle import Turtle
import time

STARTING_BALL_SPPED = 0.05

class Ball(Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("green")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = STARTING_BALL_SPPED
    
    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        
        self.goto(x=new_x, y=new_y)
        
    def bounce_y(self):
        self.y_move *= -1
    
    def bounce_x_to_left(self):
        self.x_move = -10 
        self.move_speed *= 0.9   
        
    def bounce_x_to_right(self):
        self.x_move = 10
        self.move_speed *= 0.9
          
        
    def left_lost(self):
        self.home()
        time.sleep(0.5)
        self.x_move = 10
        self.y_move = 10
        self.move_speed = STARTING_BALL_SPPED
        self.move()
        
    def right_lost(self):
        self.home()
        time.sleep(0.5)
        self.x_move = -10
        self.y_move = -10
        self.move_speed = STARTING_BALL_SPPED
        self.move()
