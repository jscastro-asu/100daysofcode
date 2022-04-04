from turtle import Screen, Turtle
from paddle import Paddle


s = Screen()
s.setup(width=800, height=600)
s.bgcolor("palegreen4")
s.title("JEN PONG GAME")
s.tracer(0)


r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))

w_paddle = Paddle((350,0))
s_paddle = Paddle((-350,0))


#move paddle
s.onkey(r_paddle,"Up")
s.onkey(l_paddle,"Down")
s.onkey(w_paddle,"Up")
s.onkey(s_paddle,"Down")
s.listen()

end_game = False
while not end_game:
    s.update

# ball
# net
# bat

# pong score = player a vs player b
# when player a miss the ball, player b scores
# vice versa

s.exitonclick()