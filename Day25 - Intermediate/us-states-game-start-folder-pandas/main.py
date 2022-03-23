import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("US - GUESS THE STATES GAME")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
turtle.penup()
turtle.stamp()

# keep asking until 50/50
game_over = True
while game_over:
    ans = screen.textinput(title = "SCORE: ", prompt = "Type a state: ")
    data = pd.read_csv("50_states.csv")
    states_list = data["state"].to_list()


    # writes the input state at the exact coordinate
    mystate = data[data.state == ans]
    getx = int(mystate.x)
    gety = int(mystate.y)
    turtle.speed(0)
    turtle.penup()
    turtle.hideturtle()
    turtle.setpos(getx, gety)
    turtle.write(ans,move=False, align='left', font='Calibri')

# if all states are added total of 50, end the game

# record score, record highest score, add timer






turtle.mainloop()

