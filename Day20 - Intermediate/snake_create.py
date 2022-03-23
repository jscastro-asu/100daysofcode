from turtle import Turtle

# by default the beginning is already at (0,0)
starting_position = [(-20, 0), (-40, 0)]

class Snake:

    # init the snake
    def __init__(self):
        my_snake = Turtle("circle")
        my_snake.color("darkseagreen4")

        self.segment = [my_snake] # a list (of object) where the snake head is at
        self.head = self.segment[0]
        self.create_snake() # function call out

    #create snake
    def create_snake(self):
        for start in starting_position: # will loop to the coordinates to create the baby snake
            snake_body = Turtle("square")
            snake_body.color("darkseagreen1")
            snake_body.penup() # pause the turtle from moving when creating snake segments
            snake_body.goto(start) # starting coordinates
            self.segment.append(snake_body) # append the body to the snake head

    # moving snake to previous location of the succeeding segments
    def move_snake(self):
        # note start-stop-step; this is head to tail 
        for seg in range(len(self.segment) -1, 0, -1):
            #go to 
            x = self.segment[seg-1].xcor()
            y = self.segment[seg-1].ycor()
            self.segment[seg].goto(x,y)
        self.segment[0].penup() # so there is no tail line
        self.segment[0].forward(20)

    # control snake

    # collision tail, wall

    # keep score

    
