from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time
import shelve

s = Screen()
s.setup(width=600, height=600)
s.bgcolor("black")
s.title("JEN SNAKE GAME")
s.tracer(0)

# create snake by calling from class
snake = Snake()
food = Food()
scoreboard = Scoreboard()

# control snake
s.listen()
s.onkey(snake.up, "Up")
s.onkey(snake.down, "Down")
s.onkey(snake.left, "Left")
s.onkey(snake.right, "Right")

# move snake
game_on = True
while game_on:
    s.update() 
    time.sleep(0.10)
    snake.move_snake()

    # detect food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.incr_score()

    # detect wall collision
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        snake.reset_snake()
        scoreboard.reset()
       
    # detect collision with tail , slicing
    for seg in snake.segment:
        if seg == snake.head:
            pass
        elif snake.head.distance(seg) < 10:
            snake.reset_snake()
            scoreboard.reset()

            


    



s.exitonclick()