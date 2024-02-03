from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20

class Snake:
       
    def __init__(self):
        self.segments = []
        self.create_snake()    
        self.snake_head = self.segments[0]  
        self.snake_head.color("coral")  
        
    def create_snake(self):    
        for position in STARTING_POSITIONS:
            self.add_segment(position)
         
    def add_segment(self, new_position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup(),
        new_segment.goto(new_position)
        self.segments.append(new_segment)
        
    def extend(self):
        self.add_segment(self.segments[-1].position())  # position of last segment
            
    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.snake_head.forward(MOVE_DISTANCE)
        
    def up(self):
        if self.snake_head.heading() != 270:
            self.snake_head.setheading(90)
        
    def down(self):
        if self.snake_head.heading() != 90:
            self.snake_head.setheading(270)
        
    def left(self):
        if self.snake_head.heading() != 0:
            self.snake_head.setheading(180)
    
    def right(self):
        if self.snake_head.heading() != 180:
            self.snake_head.setheading(0)
          
    def reset(self):
        for segment in self.segments:
            segment.goto(x=1000, y=1000)
        self.segments.clear()
        self.create_snake()
        self.snake_head = self.segments[0]  
        self.snake_head.color("coral") 