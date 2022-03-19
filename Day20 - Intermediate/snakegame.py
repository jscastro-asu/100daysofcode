from turtle import Turtle, Screen

t = Turtle()
t.speed(5)
t.pensize(5)


def snake_body():
    for i in range(3):
        t.shape("square")
        t.setpos(0,0)
        t.color("white")
        t.fd(20)
snake_body()

        


#incomplete
#screen
s = Screen()
s.setup(width=600, height=600)
s.bgcolor("black")
s.title("SNAKE GAME")
s.exitonclick()