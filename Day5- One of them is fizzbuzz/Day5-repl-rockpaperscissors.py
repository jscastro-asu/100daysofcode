'''Instructions
Make a rock, paper, scissors game.

Inside the top100movies.py file, you'll find the ASCII art for the hand signals already saved to a corresponding variable: rock, paper, and scissors. This will make it easy to print them out to the console.

Start the game by asking the player:

"What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."

From there you will need to figure out:

How you will store the user's input.
How you will generate a random choice for the computer.
How you will compare the user's and the computer's choice to determine the winner (or a draw).
And also how you will give feedback to the player.0
'''
import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

bets = [rock,paper,scissors]

my_bet = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
if my_bet == 0:
  print(bets[0], "\n ROCK \n")
elif my_bet == 1:
  print(bets[1], "\n PAPER \n")
elif my_bet == 2:
  print(bets[2], "\n SCISSORS \n")


print("COMPUTER CHOICE: ")
comp_bet = random.randint(0,2)
if comp_bet == 0:
  print(bets[0], "\n ROCK \n")
elif comp_bet == 1:
  print(bets[1], "\n PAPER \n")
elif comp_bet == 2:
  print(bets[2], "\n SCISSORS \n")


print("RESULT:\n")
if my_bet == comp_bet:
  print("TIE")
elif my_bet == 0:
  if comp_bet == 1:
    print("YOU LOSE")
  else:
    print("YOU WON")
elif my_bet == 1:
  if comp_bet == 2:
    print("YOU LOSE")
  else:
    print("YOU WON")
elif my_bet == 2:
  if comp_bet == 0:
    print("YOU LOSE")
  else:
    print("YOU WON")



