from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("chocolate1","black")
        self.setheading(90)
        self.penup()
        self.start_pos()
        

    def start_pos(self):
        self.goto(STARTING_POSITION) 
        # self.move_speed = 0.1
        
    def go_up(self):
        y = self.ycor() + 20
        self.goto(self.xcor(), y)
        
    def move(self):
        new_x = self.xcor() 
        new_y = self.ycor() 
        self.goto(new_x,new_y)

