import random

def play_again():
  while play_again == input("Play blackjack?") == "y":
    deal_card(play_again)
    
def deal_card(play_again):

  cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    
  #get first card for dealer
  rdm_dealer = [random.choice(list(cards)) for y in range(2)]
  print(f"Dealer's first card: {[rdm_dealer[0]]}")
  return rdm_dealer

  #get new cards for user
  rdm_user = [random.choice(list(cards)) for x in range(2)]
  sum_usercards = sum(rdm_user)
  print(f"Your cards {rdm_user} = {sum_usercards}")
  if sum_usercards == 21:
    print("21! BLACKJACK")
    play_again = input("Play again?")
    
  #generate new card for user
  new_card = random.choice(list(cards))
  total = sum(rdm_user)

  #generate new card for dealer
  new_dcard = random.choice(list(cards))
  d_total = sum(rdm_dealer)
  

  end_game = False
  while not end_game:

    get_card = input("Hit? Type 'y' OR Pass? Type 'n': ").lower()

    if get_card == "y":
      rdm_user.append(new_card)
      new_total = sum(rdm_user)

      print(f"Your new set: {rdm_user}: Current score: {new_total}")
      print(f"Dealer's cards: {rdm_dealer}")

    if total == 21:
      print("You Won! Blackjack!")

    if total > 21 and total < d_total:
      print(f"BUST: Dealer won with {d_total}. You went over 21. :( ")


    if get_card == "n":
      print(f"Your cards: {rdm_user} VS Dealer's cards: {rdm_dealer}.")
      if total > d_total and total < 21:
        print("You won.")
        play_again()
      elif total > 21:
        print("Dealer won.")
        end_game = True

    if get_card == "n" and d_total != 17:
      rdm_dealer.append(new_dcard)
      d_total = sum(rdm_dealer)


        
play_again()
deal_card(play_again)


#incomplete
    