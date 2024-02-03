from turtle import Turtle

FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    
    
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.score = 0
        self.goto(x=-290, y=250)
        self.update_score()

    def level_up(self):
        self.score += 1
        self.update_score()        
        
    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score}", align="left", font=FONT)
        
    def game_over(self):
        self.home()
        self.color("red")
        self.write("Game is over", align="center", font=FONT)