from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

s = Screen()
s.setup(width=600, height=600)
s.bgcolor("black")
s.title("JEN SNAKE GAME")
s.tracer(0)

#create snake by calling from class
snake = Snake()
food = Food()
scoreboard = Scoreboard()

#control snake
s.listen()
s.onkey(snake.up, "Up")
s.onkey(snake.down, "Down")
s.onkey(snake.left, "Left")
s.onkey(snake.right, "Right")

#move snake
end_game = False
while not end_game:
    s.update() 
    time.sleep(0.10)
    snake.move_snake()

    #detect food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.incr_score()
        

    #detect wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        end_game = True
        scoreboard.game_over()

    #detect collision with tail , slicing
    for seg in snake.segment[1:]:
        if snake.head.distance(seg) < 10:
            end_game = True
            scoreboard.game_over()


    



s.exitonclick()