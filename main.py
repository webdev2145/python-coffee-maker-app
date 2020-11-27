from art import logo
import time
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
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0.0
}

def prompt():
    print(logo)
    idx = 1
    for coffee_type in MENU:
        print(f'{coffee_type:<10}: ${MENU[coffee_type]["cost"]:<2.2f}')
        idx += 1

def print_report():
    heading = '''
=====================
 Resources Available
=====================
    '''
    print(heading)
    pre = ''
    suf = ''
    for res in resources:
        if res == 'money':
            pre = '$'
            suf = ''
        elif res == 'water' or res == 'milk':
            suf = 'ml'
        elif res == 'coffee':
            suf = 'g'
        else:
            suf = ''
            pre = ''
        print(f'{res.title():<6}: {pre}{resources[res]}{suf}')

def is_resource_available(drink_type):
    global resources
    drink_resources = MENU[drink_type]["ingredients"]
    for val in drink_resources:
        if drink_resources[val] < resources[val]:
            go_ahead = True
        else:
            go_ahead = False
    return go_ahead

def reduce_resources(drink_type):
    global resources
    drink_data = MENU[drink_type]['ingredients']
    for ingredient in drink_data:
        resources[ingredient] -= drink_data[ingredient]

def increase_resources():
    global resources
    res_type = input("What resource do you want to add? :")
    if res_type == 'water':

def insert_coins(drink_type):
    global resources
    drink_cost = MENU[drink_type]["cost"]
    print(f"Your drink costs: ${drink_cost:,.2f}")
    print("Please insert coins ...")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))
    total_payment = (quarters * 0.25) + (dimes * 0.1) + (nickles * 0.05) + (pennies * 0.01)
    customer_change = total_payment - drink_cost
    if customer_change < 0:
        print("You did not provide enough money. Your payment was refunded")
        return
    else:
        print(f"Here is your change: ${customer_change:,.2f}")
        print(f"Here is your {drink_type} Enjoy!")
        reduce_resources(drink_type)
        resources["money"] += drink_cost

def make_drink(coffee_type):
    if coffee_type == 'espresso' or option == 'latte' or option == 'cappuccino':
        if is_resource_available(coffee_type):
           insert_coins(coffee_type)
        else:
           print("Not enough resource available")
    else:
       print("Invalid Option")

#Program starts here
prompt()

option = input("What would you like?: ").lower()

while option != 'off':
    if option == 'report':
        print_report()
    elif option == 'inventory':
        increase_resources()
    else:
        make_drink(option)


    option = input("What would you like?: ").lower()

print("Powering down....")
time.sleep(4)

