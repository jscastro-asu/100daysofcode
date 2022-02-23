from menu import MENU
from menu import resources
import math
print("COFFEE MACHINE")

def select_coffee():
   selection = input("What would you like? espresso | latte | cappuccino: " )
   return selection

def coffee_price(selection):
   if selection == "espresso":

      for k, v in MENU.items():
         if "espresso" in k:
            price = float(v['cost'])
            print(f"Cost is ${price}. ")
            return price

   elif selection == "latte":

      for k, v in MENU.items():
         if "latte" in k:
            price = float(v['cost'])
            print(f"Cost is ${price}. ")

            return price

   elif selection == "cappuccino":

      for k,v in MENU.items():
         if "cappuccino" in k:
            price = float(v['cost'])
            print(f"Cost is ${price}. ")
            return price

   elif selection == "report":

      print()

def payment():
   quarter = float(input(" = How much quarters? "))
   q_val = 0.25
   q = q_val * quarter

   dime = float(input(" = How much dime? "))
   d_val = 0.10
   d = d_val * dime

   nickel = float(input(" = How much nickel? "))
   n_val = 0.05
   n = n_val * nickel

   penny = float(input(" = How much penny?"))
   p_val = 0.01
   p = p_val * penny

   ans = float((q + d + n + p))
   print(f"You paid: ${ans}")
   return ans

def cx_change(ans, price):
   if ans == price:
      print("You coffee is brewing...☕. Enjoy!")

   elif ans > price:
      chg = float(round( ans - price ))
      print("You coffee is brewing...☕. Enjoy!")
      print(f"Your change: ${chg}")

   elif ans < price:
      print("Insufficient amount, refunded.")

def coffee_ingredients(selection):

   w = resources.get("water")
   c = resources.get("coffee")
   m = resources.get("milk")

   water_left = int()
   coffee_left = int()
   milk_left = int()

   for k, v in MENU.items():
      if "espresso" in k:
         e_water = v["ingredients"]["water"]
         e_coffee = v["ingredients"]["coffee"]
         water_left = w - e_water
         coffee_left = c - e_coffee

      elif "latte" in k:
         l_water = v["ingredients"]["water"]
         l_coffee = v["ingredients"]["coffee"]
         l_milk = v["ingredients"]["milk"]
         water_left = w - l_water
         coffee_left = c - l_coffee
         milk_left = m = m - l_milk

      elif "cappuccino" in k:
         c_water = v["ingredients"]["water"]
         c_coffee = v["ingredients"]["coffee"]
         c_milk = v["ingredients"]["milk"]
         water_left = w - c_water
         coffee_left = c - c_coffee
         milk_left = m - c_milk

      elif water_left <= 0:
         print("Ran out of water, sorry.")
      elif coffee_left <= 0:
         print("No more stash.")
      elif milk_left <= 0:
         print("The cow went to the market.")


  def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")






selection = select_coffee()
price = coffee_price(selection)
ans = payment()
cx_change(ans, price)
coffee_ingredients(selection)

# print(MENU['espresso']['ingredients'])
# print(resources['water'])
# esp = (MENU['espresso']['ingredients'])