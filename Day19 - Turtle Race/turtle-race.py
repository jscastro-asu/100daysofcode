
from turtle import Turtle, Screen
import random
import time


s = Screen()
s.setup(width=500, height=400)
s.title("TURTLE RACE")


start_race = False
player_bet = s.textinput(title="What's your bet?", prompt="Pick a turtle color: \nYour options: \norange \nblue \npink \nred \nviolet \nyellow \ncyan")


colors = ["orange", "blue", "pink", "red", "violet","yellow","cyan"]
start_point = [150, 100, 50, 0, -50, -100, -150]
racers = []

track = Turtle()
track.penup()
track.goto(200, 250)


track.pensize(10)
track.pencolor("black")
track.right(90)
for tracking in range(20): #finish line track
    track.forward(20)
    track.penup()
    track.forward(20)
    track.pendown()


for r in range(0,7):
#placing turtle in the start point
    t = Turtle(shape="turtle")
    t.speed("fastest")
    t.color(colors[r])
    t.penup() 
    t.goto(x=-220, y=start_point[r])
    t.pendown()
    t.fd(10)
    racers.append(t)


# once player placed bet, race is on
if player_bet:
    start_race = True

while start_race:
    for racer in racers:

        if racer.xcor() > 200: # this is the finish line if a racer got it to over 200 then that turtle color wins
            winner = racer.pencolor()
            t.hideturtle()
            t.color("black")
            t.penup()
            t.goto(0, 0)
            
            start_race = False
            t.clear()
            t.write(f"The winner is {winner}!", align = "center", font = ("Impact",16,"bold"))
            
            # winner printscreen
            if winner == player_bet:
                print(f"Your {player_bet} turtle won.")
            else:
                print(f"{winner} turtle won.")


        #random turtle speed/distance
        dist = random.randint(0,20)
        racer.fd(dist)



s.mainloop()


