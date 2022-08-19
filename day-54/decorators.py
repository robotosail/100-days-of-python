import time

# FUnctions are first class objects, and can be passed around as arguments


# functions can be nested inside each other
def msg():
    print('Hi')

    def message():
        print('Hello how are you')
    return message  # returning this functions and allowing it to be called later


mse = msg()
mse()

# Functions can be returned from other functions


def add(n1, n2):
    return n1 + n2


def calculate(function, n1, n2):
    return function(n1, n2)


# Python decorator - they are meant to modify or delay other functions
def decorator_function(function):
    def wrapper_function():
        time.sleep(2)
        function()
    return wrapper_function


@decorator_function  # - it is called syntax sugar it must be untop inorder to work
def say_hello():
    print("Hello")


# this is similar to the decorator function
decorator_function(say_hello)()


def loggining(function):
    name = function.__name__
    print(f"You called {name} {function(1, 2, 4)}")


@loggining
def calling(*args):
    answer = 0
    for i in args:
        answer += i + answer
    print(answer)
