# to allow multiple inputs use the add one *and a names so it would look like
# this- *args
# args come in as a tuple
# *args allows there to be infinite amount of values
# it doesn't have to be named args
# values can be accessed by index
# it is for positional arguments

def add(*args):
    print(args[0])
    sum = 0
    for number in args:
        sum += number
    return sum


print(add(2, 4, 5))

# turns into a dictionary
# stands for keyword arguments


def calculate(n, **kwargs):
    print(kwargs)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    n /= kwargs["divide"]
    n -= kwargs["subtract"]


print(calculate(3, add=3))


class Car:
    def __init__(self, **kw):
        # using the .get makes sure no error is returned
        self.make = kw.get("make")
        self.model = kw.get("model")
