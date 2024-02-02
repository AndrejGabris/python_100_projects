from turtle import Turtle

ALIGNMENT = "center"
FONT_TYPE = ('Courier', 20, 'normal')


class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.goto(x=0, y=260)
        self.speed("fastest")
        self.color("white")
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score: {self.score}", move=False, align=ALIGNMENT, font=FONT_TYPE)
        
    def point_gained(self):
        self.clear()
        self.score +=1 
        self.update_scoreboard()
        
    def game_over(self):
        self.goto(x=0, y=0)
        self.color("red")
        self.write(f"Game over!", move=False, align=ALIGNMENT, font=FONT_TYPE)
        