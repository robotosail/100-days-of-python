# FUNCTIONS WITH INPUTS

# Simple Function
# def Greet():
#     print("Hello")
#     print("How are you today")
#     print("Welcome to day 8 of 100 days of python")

# Greet()

# Function that allows for input


# def Greet_With_name(name):
#     print(f"Hello {name}")
#     print(f"How are you today {name}")
#     print(f"{name}Welcome to day 8 of 100 days of python")

# Greet_With_name("David")

# Functions with more than one inputs
def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location} ?")

# positional arguments - data can only be put in a specific order.
# greet_with("David", "Google")
# keyword arguments - data can only be put in a specific order.
greet_with(location="US", name="David")
