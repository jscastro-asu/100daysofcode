from turtle import *
import random
s = Turtle()
s.shape()
s.speed(10)
colors = ["red", "orange", "yellow", "green", "blue", "purple", "black","pink"]

def shape(sides):
    for x in range(sides):
        s.fd(100)
        s.left(360.0/sides)



for y in range(3,11):
    s.color(random.choice(colors))
    shape(y)