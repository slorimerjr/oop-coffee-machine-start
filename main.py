from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

is_on = True
coffee_maker = CoffeeMaker()

while is_on:
    choice = input("What would you like? (espresso/latte/cappuccinno) ").lower()
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee_maker.report()
    else:
        ### drink = MENU[choice]###