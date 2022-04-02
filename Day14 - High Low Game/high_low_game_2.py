import random
from art import logo
from art import versus
from game_data import data
print(logo)

def high_low():

  random_val = random.randrange(len(data))

  val= (f"{data[random_val]['name']} {data[random_val]['description']} from {data[random_val]['country']}")
  print(val)
  return val

def follower_diff(a, b):

  if a != b:
    your_guess = input("===> YOUR PICK? A vs B, Type 'A' or 'B': ")
    print(your_guess)

    score = 0
    if (your_guess == "A" and a > b) or (your_guess == "B" and a < b):
      print("Score!")
      score += 1
      return score

    elif (your_guess == "A" and a < b) or (your_guess == "B" and a > b):
      print("Game Over.")

end_game = False
while not end_game:
  print("==SAMPLE A:== ")
  a = high_low()
  print(versus)
  print("== SAMPLE B:== ")
  b = high_low()
  score = follower_diff(a, b)
  if not score:
    end_game = True














