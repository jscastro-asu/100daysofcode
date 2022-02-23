from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

coffee_on = True

# check resources sufficient
while coffee_on:
  # print report
  options = menu.get_items()
  choice = input(f"What do you want? {options}")

  if choice == "report":
    money_machine.report()
    coffee_maker.report()
  elif choice == "off":
    coffee_on = False
  else:
    drink = menu.find_drink(choice)
    # process coins and check transaction if successful
    if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
        #make the coffee
        coffee_maker.make_coffee(drink)





