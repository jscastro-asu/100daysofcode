from turtle import *
import turtle as turtle_module
turtle = Turtle()

turtle.pen(fillcolor="black", pencolor="red", pensize=2)
for i in range(50):
    turtle.forward(5)
    turtle.penup()
    turtle.forward(5)
    turtle.pendown()



screen = turtle_module.Screen()
screen.exitonclick()