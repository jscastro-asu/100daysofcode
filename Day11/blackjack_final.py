import random
import os
clear = os.system("clear")

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
user_sum = int()
dealer_sum = int()
# to pick random cards for player and dealer
def deal_card(cards):
  random_card = random.choice(cards)
  return random_card

# this is the summation section of the cards. In case 11 was drawn and it the sum is over 21 then it replaces it to 1
def score(cards):
  if sum(cards) == 21 and len(cards) == 2:
    return 21
  if 11 in cards and sum(cards) > 21:
    cards.remove(11)
    cards.append(1)
  return sum(cards)

# this is comparing values, win or lose
def get_sum(user_sum,dealer_sum):

  if user_sum == dealer_sum:
    return "=Draw="
  elif user_sum == 21:
    return "Blackjack!!"
  elif dealer_sum == 21:
    return "Dealer Blackjack, you lose :("
  elif user_sum < 21:
    return "**You won!**."
  elif user_sum > 21:
    return "You're over 21, you lose. :("
  elif user_sum > dealer_sum:
    return "**You won!**."
  elif dealer_sum < 21 and user_sum < dealer_sum:
    return "Dealer won. =("

# this is the play section
def get_card():
    user_card = []
    dealer_card = []
    end_game = False

    for x in range(2):
      user_card.append(deal_card(cards))
      dealer_card.append(deal_card(cards))

    print(f"Your first cards: {user_card}")
    print(f"Dealer's card: {dealer_card[0]}")

    while not end_game:
      user_sum = score(user_card)
      dealer_sum = score(dealer_card)

      if user_sum == 21 or dealer_sum == 21 or user_sum > 21:
        end_game = True
      else:
        get_card = input("Hit? Type 'y' OR Pass? Type 'n': ").lower()

        if get_card == 'y':
          user_card.append(deal_card(cards))
          user_sum = score(user_card)
          print(f"Your new set: {user_card}: Current score: {user_sum}")
          print(f"Dealer's cards: {dealer_card}")

        else:
          end_game = True

    while dealer_sum != 21 and dealer_sum < 17:
        dealer_card.append(deal_card(cards))
        dealer_sum = score(dealer_card)
    print(f"Your score: {user_sum} vs Dealer's score: {dealer_sum}")
    print(get_sum(user_sum, dealer_sum))

def try_again():
  ask = input("Play blackjack? 'y' or 'n': ") 
  while ask == 'y':
    get_card()
  if ask == 'n':
    print("Thanks for playing.")
    



random_card = deal_card(cards)
score(cards)

get_card()
get_sum(user_sum, dealer_sum)
try_again()
