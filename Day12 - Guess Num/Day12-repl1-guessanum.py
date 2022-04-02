from art import logo
print(logo)
import random

def game():
  print("Welcome! You will guess the number I picked from 1 - 100.")
  num = random.randint(1, 100)
  print(f"===Testing: {num}====")
  return num

def check(num):

  diff = input("Choose difficulty level: Type 'easy' or 'hard': ")

  if diff == "easy":
    turns = 5

    while turns >= 1:
      guess = int(input("Guess? "))
      turns -= 1
      
      if guess < num and turns !=0:
        print(f"Too low. {turns} turn/s left: ")
      elif guess > num and turns != 0:
        print(f"Too high. {turns} turn/s left: ")
      elif guess == num:
        print("You got it.")
        break
      
    if turns == 0:
      print("You reached the limit.")
      exit()
  
  elif diff == "hard":
    turns = 10

    while turns >= 1:
      guess = int(input("Guess? "))
      turns -= 1
      
      if guess < num and turns !=0:
        print(f"Too low. {turns} turn/s left: ")
      elif guess > num and turns != 0:
        print(f"Too high. {turns} turn/s left: ")
      elif guess == num:
        print("You got it.")
        break
      
    if turns == 0:
      print("You reached the limit.")
      exit()



    

num = game()
check(num)