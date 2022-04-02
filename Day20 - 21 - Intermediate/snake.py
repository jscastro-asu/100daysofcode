from turtle import Turtle, Screen

START_POS = [(0,0), (-20, 0), (-40, 0)]
MOVE_DIST = 20

class Snake:

    #init the snake
    def __init__(self):
        self.segment = [] # a list (of object) where the snake head is at
        self.create_snake() # function call out
        self.head = self.segment[0]
    
    #create snake (baby snake with 3 segments)
    def create_snake(self):
        for start in START_POS: 
            self.add_seg(start)
            
    def add_seg(self, start):
        new_seg = Turtle("square")
        new_seg.color("orange")
        new_seg.penup()
        new_seg.goto(start) 
        self.segment.append(new_seg) 

    def extend(self):
        #this is a turtle state which return the turtle’s current location (x,y)
        self.add_seg(self.segment[-1].position()) 


    #move snake to previous location of the succeeding segments
    def move_snake(self):
        # note start-stop-step; so tail follows the head whichever it goes
        for seg in range(len(self.segment) -1, 0, -1):
            x = self.segment[seg-1].xcor()
            y = self.segment[seg-1].ycor()
            self.segment[seg].goto(x,y)
        self.segment[0].penup() # remove tail line
        self.head.forward(MOVE_DIST)
    

    #control snake
    def up(self):
        if self.head.heading() != 270: 
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)
        
    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

