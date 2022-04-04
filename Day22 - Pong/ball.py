from turtle import Turtle

class Ball():
    
    def __init__(self, position):
        super().__init__()
        self.shape("circle")
        self.color("yellow")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(0,0)
      
    