from turtle import Turtle, Screen
import random

class Ball(Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("yellow")
        self.penup()
        self.x_move = 10
        self.y_move = 10
  

    def move(self):

        ball_x = self.xcor() + self.x_move
        ball_y = self.ycor() + self.y_move
        self.goto(ball_x,ball_y)
        
    def bounce_y(self):
        self.y_move *= -1 #moves opposite direction
        
    def bounce_x(self):
         self.x_move *= -1
        

      
    