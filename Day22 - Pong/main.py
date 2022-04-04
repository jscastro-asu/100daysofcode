from turtle import Screen, Turtle
from paddle import Paddle
#from ball import Ball

s = Screen()
s.setup(width=800, height=600)
s.bgcolor("palegreen4")
s.title("JEN PONG GAME")
s.tracer(0)

r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))

#move paddle
s.listen()
s.onkey(r_paddle.scroll_up, "Up")
s.onkey(l_paddle.scroll_down, "Down")
s.onkey(r_paddle.scroll_up, "w")
s.onkey(l_paddle.scroll_down, "s")

end_game = False
while not end_game:
    s.update

s.exitonclick()