import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

s = Screen()
s.setup(width=800, height=600)
s.bgcolor("palegreen4")
s.title("PONG GAME")
s.tracer(0)

 
r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))

ball = Ball()
scoreboard = Scoreboard()


#move paddle
s.onkey(r_paddle.scroll_up, "Up")
s.onkey(r_paddle.scroll_down, "Down")
s.onkey(l_paddle.scroll_up, "w")
s.onkey(l_paddle.scroll_down, "s")
s.listen()


end_game = False
while not end_game:
    time.sleep(ball.move_speed)
    s.update()
    ball.move()


    # wall collision
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
        
    # ball to paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
    
    # right paddle misses the ball
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point
       
    # left paddle misses the ball 
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point


s.exitonclick()
