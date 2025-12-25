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
    "money": 0,
}
# Necessary Functions
def sufficient_resources(drink):
    global resources

    for item in MENU[drink]["ingredients"]:
        if resources[item] < MENU[drink]["ingredients"][item]:
            print(f"Sorry, there is not enough {item}")
            return False

    for item in MENU[drink]["ingredients"]:
        resources[item] -= MENU[drink]["ingredients"][item]
    return True

def coin_handler(drink):
    global resources
    num_quarters = int(input("How many quarters?: "))
    num_dimes = int(input("How many dimes?: "))
    num_nickels = int(input("How many nickels?: "))
    num_pennies = int(input("How many pennies?: "))

    change = round((num_quarters*0.25 + num_dimes*0.1 + num_nickels*0.05 + num_pennies*0.01) - MENU[drink]["cost"], 2)

    if change >= 0:
        print(f"Here is ${change} in change")
        resources["money"] += MENU[drink]["cost"]
    else:
        print("Sorry that's not enough money. Money refunded.")
def response(choice):
    if choice in MENU:
        if sufficient_resources(choice):
            coin_handler(choice)

# Main Code:

while True:
    user_choice = input("What would you like? (espresso/latte/cappuccino): ")

    # First check for special commands and act upon them:
    if user_choice == "off":
        break
    elif user_choice == "report":
        print(f"Water: {resources["water"]}\nMilk: {resources["milk"]}\nCoffee: {resources["coffee"]}\nMoney: ${resources["money"]}")

    response(user_choice) # Checks for general commands and acts upon them
