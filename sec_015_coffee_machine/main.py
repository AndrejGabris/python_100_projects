from replit import clear

clear()

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


all_types_of_coffe = list(MENU.keys())
machine_functions = all_types_of_coffe + ['off', 'report']


def report():
    print(f"""
Water: {resources["water"]}ml
Milk: {resources["milk"]}ml
Coffee: {resources["coffee"]}g
Money: ${profit}
""")

print(MENU["espresso"]["ingredients"])

def coffee_sufficient(type_of_coffee):
    for ingredient in MENU[type_of_coffee]["ingredients"]:
        ingredient_level = resources[ingredient] - MENU[type_of_coffee]["ingredients"][ingredient]
        if ingredient_level < 0:
            return f"Sorry there is not enough {ingredient}"
        
def pay_amount():
    print("Please insert money:")
    quaters = int(input("How many quaters ($0.25): "))
    dimes = int(input("How many dimes ($0.10): "))
    nickles = int(input("How many nickles ($0.05): "))
    pennies = int(input("How many nickles ($0.01): "))
    amount_inserted = quaters*0.25 + dimes*0.10 + nickles*0.05 + pennies*0.01
    return amount_inserted

def resources_changer(type_of_coffee):
    for ingredient in MENU[type_of_coffee]["ingredients"]:
        resources[ingredient] -= MENU[type_of_coffee]["ingredients"][ingredient]  
    print(f"Here is your {type_of_coffee} ☕️. Enjoy!") 



is_off = False
while is_off == False:
    user_choice = input("What type of coffee would you like? (espresso/latte/cappuccino): ")
    while user_choice not in machine_functions:
        user_choice = input("What type of coffee would you like? (espresso/latte/cappuccino): ")
    if user_choice == 'off':
        is_off = True
    elif user_choice == "report":
        report()
    else:
        not_enough_ingredients = coffee_sufficient(user_choice)
        if not_enough_ingredients == None:
            money_status = pay_amount()
            if money_status < MENU[user_choice]["cost"]:
                print("Sorry that's not enought money. Money refunded.")
            elif money_status > MENU[user_choice]["cost"]:
                profit += MENU[user_choice]["cost"]
                amount_of_returned_money = money_status - MENU[user_choice]["cost"]
                print(f"Here is ${amount_of_returned_money} in change.")
                resources_changer(user_choice)
            else:
                profit += MENU[user_choice]["cost"]
                resources_changer(user_choice)
        else:    
            print(not_enough_ingredients)