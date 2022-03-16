from turtle import *
draw_square = Turtle()

for x in range(4):
    draw_square.fd(100)
    draw_square.left(90)


screen = Screen()
screen.exitonclick()