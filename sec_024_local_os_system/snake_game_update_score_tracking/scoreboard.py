from turtle import Turtle

ALIGNMENT = "center"
FONT_TYPE = ('Courier', 20, 'normal')




class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.score = 0
        self.read_highscore()
        self.hideturtle()
        self.penup()
        self.goto(x=0, y=260)
        self.speed("fastest")
        self.color("white")
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High score {self.highscore}", move=False, align=ALIGNMENT, font=FONT_TYPE)
        
    def point_gained(self):
        self.score +=1 
        self.update_scoreboard()
        
    def reset(self):
        if self.score > self.highscore:
           self.highscore = self.score
           self.write_highscore()
        self.score = 0
        self.update_scoreboard()
        
    def read_highscore(self):
        with open(r"sec_024_local_os_system\snake_game_update_score_tracking\data.txt", mode="r") as file:
            HIGHSCORE = int(file.read())
        self.highscore = HIGHSCORE
    
    def write_highscore(self):
        with open(r"sec_024_local_os_system\snake_game_update_score_tracking\data.txt", mode="w") as file:
            file.write(str(self.highscore))
        
        
            
                
    # def game_over(self):
    #     self.goto(x=0, y=0)
    #     self.color("red")
    #     self.write(f"Game over!", move=False, align=ALIGNMENT, font=FONT_TYPE)
        