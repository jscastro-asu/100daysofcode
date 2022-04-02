from turtle import Turtle
import random

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("darkseagreen")
        self.penup()
        self.shapesize(stretch_len=1,stretch_wid=1)
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        rdm_x =random.randint(-290,290)
        rdm_y =random.randint(-290,290)
        self.goto(rdm_x, rdm_y)