from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# getting access to the classes
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()
# items = MenuItem()


on = True
while on:
    options = menu.get_items()
    choice = input(f"What do you want? ({options}): ")
    if choice == "off":
        on = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        # finding the drink from the menu class
        drink = menu.find_drink(choice)
        # checking if there are enough resources to make the drink
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            # making the coffee
            coffee_maker.make_coffee(drink)

            # print(drink)
