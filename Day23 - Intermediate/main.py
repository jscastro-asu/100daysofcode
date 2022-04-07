# move turtle up with keypress
# create cars and move them
# detect collision to cars
# detect when turtle reaches the other side
# create scoreboard

import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.title("TURTLE CROSSING")
screen.bgcolor("darkgrey")


player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()



screen.listen()
screen.onkey(player.go_up, "Up")       


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    
    car_manager.new_car()
    car_manager.move_cars()
    
    # when turtle moves to the end top it goes back down, with next level speeds up
    player.move()
    if player.ycor() > 280:
        player.start_pos()
        car_manager.level_up()
        scoreboard.incr_score()
        
    # detect collision to car
    for c in car_manager.all_cars:
        if c.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()
            

        
        
    

    
    
screen.mainloop()