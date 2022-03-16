import random
import turtle as x
from turtle import Screen

x.colormode(255)
t = x.Turtle()
t.pensize(5)
t.speed(5)


def rdmcolor():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rdmcolor = (r, g, b)
    return rdmcolor


def make_random_walk(step_size, step_number):
    dir = [0, 90, 180, 270]
    for _ in range(step_number):
        t.setheading(random.choice(dir))
        t.forward(step_size)
        t.color(rdmcolor())


make_random_walk(20,1000)
screen = Screen()
screen.exitonclick()
