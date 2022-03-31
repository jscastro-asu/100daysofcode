
import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("US - GUESS THE STATES GAME")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
turtle.penup()
turtle.stamp()

# will keep asking for states until 50/50
game_over = False
data = pd.read_csv("50_states.csv")
states_list = data["state"].to_list()

while not game_over:
    list_ans = []
    max_ans = 50
    while len(list_ans) < max_ans:
        ans = screen.textinput(title = f"SCORE: {len(list_ans)}/50", prompt = "Type a state: ").title()

        if ans in states_list:
            #cannot accept duplicate input and won't add in score
            list_ans.append(ans) if ans not in list_ans else None
            t = turtle.Turtle()
            t.speed(0)
            t.penup()
            t.hideturtle()
            #this writes the input on the correct x,y coordinates of the state given
            mystate = data[data.state == ans] 
            t.goto(int(mystate.x), int(mystate.y))
            t.write(ans,move=False, font=("Arial", 8, "normal"))
        # if you give up, you type Exit, it will generate a csv of states you missed
        if ans == "Exit":
            df1 = pd.DataFrame(list_ans)
            df2 = pd.DataFrame(states_list)
            dfdiff = pd.concat([df1,df2]).drop_duplicates(keep=False)
            diff_csv = dfdiff.to_csv('remaininglist.csv')
            exit()




turtle.mainloop()

