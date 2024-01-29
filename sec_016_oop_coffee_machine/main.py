from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_menu = Menu()
coffee_machine = CoffeeMaker()
money_machine = MoneyMachine()

turn_on = True
while turn_on:
    options = coffee_menu.get_items()
    user_choice = input(f"What would you like? {options}: ")
    if user_choice == "off":
        turn_on = False
    elif user_choice == "report":
        coffee_machine.report()
        money_machine.report()
    else:
        drink = coffee_menu.find_drink(user_choice)
        if drink != None:
            if coffee_machine.is_resource_sufficient(drink):
                if money_machine.process_coins(drink.cost):
                    coffee_machine.make_coffee(drink)
