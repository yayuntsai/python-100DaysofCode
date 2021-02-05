from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
menu_items = menu.get_items()
#print(menu_items)

latte = MenuItem('latte', '20', '30', '20', '70')
espresso = MenuItem('espresso', '10', '30', '20', '40')
cappuccino = MenuItem('cappuccino', '20', '20', '10', '50')
#print(espresso.ingredients)
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

is_on = True
while is_on:
  option = menu.get_items()
  choice = input(f"What do you want? ({option})?")
  if choice == 'off':
    is_on = False
  elif choice == 'report':
    coffee_report = coffee_maker.report()
    money_report = money_machine.report()
  else:
    print(menu.find_drink(choice))