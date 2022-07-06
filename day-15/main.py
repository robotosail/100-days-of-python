MENU = {
    "expresso": {
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

money = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

# check if the ingredients are enough


def enough_res(ingredients):
    """Checks if the ingredients are enough. Returns True or False"""
    # looping through the items in the ingredients
    for item in ingredients:
        if ingredients[item] > resources[item]:
            print(f"Sorry, there is not enough {item}")
            return False
    return True


def coins():
    """Returns the total value from the coins inserted"""
    print("Please insert coins")
    total = int(input("How many quarters: ")) * 0.25
    total += int(input("How many dimes: ")) * 0.10
    total += int(input("How many nickels: ")) * 0.5
    total += int(input("How many pennies: ")) * 0.1
    return total


def check_payment(money_rec, cost):
    """Returns True or False if money was accepted"""
    if money_rec >= cost:
        change = round(money_rec - cost, 2)
        print(f"Here is your change ${change}")
        global money
        money += cost
        return True
    else:
        print("Sorry that not enough money given. Refunded")
        return False


def make_coffee(drink, ingredients):
    """Deduct the required ingredents from the resources"""
    # looping through the ingredients
    for item in ingredients:
        # subtracting each item from the ingredients
        resources[item] -= ingredients[item]
    print(f"Here is your {drink} 🍵")


on = True
while on:
    choice = input(
        "What would you like? (expresso/latte/cappuccino): ").lower()
    # allowing admin access
    if choice == "off":
        on = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"milk: {resources['milk']}ml")
        print(f"Coffe: {resources['coffee']}g")
        print(f"Money: ${money}")
    else:
        # getting the desired coffee from the menu
        drink = MENU[choice]
        # calling the function to check if the ingredients are enough
        if (drink["ingredients"]):
            payment = coins()
            if check_payment(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])
                # print(drink)
