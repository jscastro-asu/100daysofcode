from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("yellow")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.upd_score()

    def upd_score(self):
        self.write(f"SCORE: {self.score}",align = "center", font = ("Courier",24,"bold"))

    def game_over(self):
        self.color("red")
        self.goto(0, 0)
        self.write("* GAME OVER *", align = "center", font = ("Courier",24,"bold"))
        
    def incr_score(self):
        self.score += 1
        self.clear()
        self.upd_score()
        