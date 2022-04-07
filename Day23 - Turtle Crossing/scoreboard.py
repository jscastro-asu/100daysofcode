from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("black")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.upd_score()

    def upd_score(self):
        self.write(f"SCORE: {self.score}",align = "center", font = (FONT))

    def game_over(self):
        self.color("red")
        self.goto(0, 0)
        self.write("* GAME OVER *", align = "center", font = (FONT))
        
    def incr_score(self):
        self.score += 1
        self.clear()
        self.upd_score()
        
