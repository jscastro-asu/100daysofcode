from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE
        
    def new_car(self):
        # makes the road less crowded,
        rdm_occur = random.randint(1, 6)
        if rdm_occur == 1:
            car = Turtle("square")
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.penup()
            car.color(random.choice(COLORS))
            rdm_y = random.randint(-250, 250)
            car.goto(300,rdm_y)
            self.all_cars.append(car)
        
    def move_cars(self):
        # cars left to write
        for c in self.all_cars:
            c.backward(self.car_speed)
            
    def level_up(self):
        self.car_speed += MOVE_INCREMENT
        
        
        
        

