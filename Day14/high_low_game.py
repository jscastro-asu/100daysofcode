import random
from art import logo
from art import versus
from game_data import data


print(logo)
def high_low():

  my_val = random.choice(list(data))

  for k, v in my_val.items():
    if type(v) is str:
      x = my_val[k]
      print(x, end=" ", flush=True)
  return x

def follower_diff(a,b):

  your_guess = input("===> YOUR PICK? A vs B, Type 'A' or 'B': ")
  print(your_guess)

  if your_guess == "A" and a > b:
    print("Score!")
  elif your_guess == "A" and a < b:
    print("You lose.")
  elif your_guess == "B" and a < b:
    print("Score!")
  elif your_guess == "B" and a > b:
    print("You lose.")




print("SAMPLE A: ")
a = high_low()
print(versus)
print("SAMPLE B: ")
b = high_low()
follower_diff(a, b)

