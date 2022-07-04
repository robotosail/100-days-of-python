import art
from os import system
# creating the neccessary functions


def add(a, b):
    """Adds the first value with the second value"""
    return a + b


def subtract(a, b):
    """Subtracts the first value from the second value"""
    return a - b


def multiply(a, b):
    """Multiplys the first value with the second value"""
    return a * b


def divide(a, b):
    """Divides the first value with the second value"""
    return a / b


# creating a dictionary that has operations and the operations hold the functions
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

# creating a function to calculate


def calculate(first, second, operation):
    # getting the operation
    result = operations[operation]
    # since the operation is a function pass in the values needed
    result = result(first, second)

    return result

def calculator():
    print(art.logo)
    calculating = True
    num1 = float(input("What is the first number: "))
    # looping through the operations dictionary
    for symbol in operations:
        print(symbol)

    while calculating:
        # getting input
        operation = input("Pick an operation: ")
        num2 = float(input("What is the second number: "))
        # calling the calculate function
        answer = calculate(first=num1, operation=operation, second=num2)
        print(f"{num1} {operation} {num2} = {answer}")

        if input("Do you want to continue calculating? 'Y' for yes or 'N' for no: ").lower() == "y":
            num1 = answer
        else:
            calculating = False
            system("clear")
            calculator()
calculator()