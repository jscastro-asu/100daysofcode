from turtle import Turtle

class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.color("purple")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_score()
        
        
    def update_score(self):
        self.clear()
        self.goto(-200, 200)
        self.write(f"Score A: {self.l_score}", align="center", font=("Calibri",30,"normal")) 
        self.goto(200, 200)
        self.write(f"Score B: {self.r_score}", align="center", font=("Calibri",30,"normal")) 
        
    def l_point(self):
        self.l_score += 1
        self.update_score()
        
    def r_point(self):
        self.r_score += 1
        self.update_score()