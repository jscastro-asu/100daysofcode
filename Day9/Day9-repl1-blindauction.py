from replit import clear #i'm using replit

#HINT: You can call clear() to clear the output in the console.

from art import logo
print(logo)

bidder_d = {}
end_auction = False

def get_highest_bidder(bid_info):
  winning_bid = 0
  winner = ""


  for bidder in bid_info: #loops in key not value

    bid_amt = bid_info[bidder]
    if bid_amt > winning_bid:
      winning_bid = bid_amt
      winner = bidder

  print(f"The winner is {winner} with bid of ${winning_bid}.")

while not end_auction:

  bidder_name= input("What is your name?: ")

  bidder_value= int(input("What's your bid?: $"))
  bidder_d[bidder_name] = bidder_value

  add_bidder = input("Are there any other bidders? Type 'yes' or 'no': ")
  
  if add_bidder == "yes":
    clear()

  elif add_bidder == "no":
    get_highest_bidder(bidder_d)
    end_auction = True






