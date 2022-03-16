import random
import turtle as t
from turtle import Screen

tt = t.Turtle()
tt.speed(10)
tt.pensize(2)
t.colormode(255)


def rdmcolor():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rdmcolor = (r, g, b)
    return rdmcolor

for x in range(1,100):
    tt.color(rdmcolor())
    tt.circle(150,360)
    tt.left(50)




screen = Screen()
screen.exitonclick()