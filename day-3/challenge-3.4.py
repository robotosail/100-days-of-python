print("Welcome to Python Pizza Deliveries!")

# getting user data
size = input(
    "What size pizza do you want? S for small, M for medium, L for large: ")
pepperoni = input("Do you want pepperoni? Y for yes or N for no: ")
cheese = input("Do you want extra cheese? Y for yes or N for no: ")
price = 0

# if user wants large pizza set price to 25
if size == "L":
    price = 25
    # if user wants pepperoni add 3 to the price.
    if pepperoni == "Y":
        price += 3

# if user wants medium pizza set price to 20
elif size == "M":
    price = 20
    # if user wants pepperoni add 3 to the price.
    if pepperoni == "Y":
        price += 3

# if user wants small pizza set price to 15
elif size == "S":
    price = 15
    # if user wants pepperoni add 3 to the price.
    if pepperoni == "Y":
        price += 2

if cheese == "Y":
    price += 1
print(f"Your final bill is ${price}")
