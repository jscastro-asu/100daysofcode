from turtle import Turtle, Screen

t = Turtle()
s = Screen()
s.setup(width=600, height=600)
s.title("ETCH-A-SKETCH")
t.setheading(0)

def fw_w():
    t.fd(10)

def bw_s():
    t.back(10)
 


def left_a():
    t.left(10)



def right_d():
    t.right(10)


def clear_c():
    t.clear()
    t.penup()
    t.home()


s.listen()
s.onkey(fw_w, "w")
s.onkey(bw_s, "s")
s.onkey(left_a, "a")
s.onkey(right_d, "d")
s.onkey(clear_c, "c")
s.exitonclick()