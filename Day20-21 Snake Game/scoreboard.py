from turtle import Turtle
import datetime
from os import path


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open('highscore.txt', 'r') as data:
            self.high_score = int(data.read())
        self.color("yellow")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.upd_score()
       

    def upd_score(self):
        self.clear()
        self.write(f"SCORE: {self.score} | HIGH SCORE: {self.high_score}",align = "center", font = ("Courier",24,"bold"))

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open('highscore.txt', 'w') as data:
                data.write(f"{self.high_score}")
            self.score = 0
            self.upd_score()
    
    def incr_score(self):
        self.score += 1
        self.upd_score()
 

        