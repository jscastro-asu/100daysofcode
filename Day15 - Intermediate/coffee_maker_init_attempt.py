from menu import MENU
from menu import resources
import math
print("COFFEE MACHINE")

def select_coffee():
   selection = input("What would you like? espresso | latte | cappuccino: " )
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


def payment(price):
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
   elif ans < price:
      print("Insufficient amount, refunded.")
   elif ans > price:
      chg = float( ans - price )
      print("You coffee is brewing...☕. Enjoy!")
      print(f"Your change: ${chg}")




price = select_coffee()
ans = payment(price)
cx_change(ans, price)