# to use any module in python you need to import it
# import random
# # import my_module

# random_integer = random.randint(1, 10)
# print(random_integer)

# random_float = random.random() * 5
# print(random_float)

"""
# Data Structure 
    # lists:- Holds groups of multiple values
    .append() //appends to a list
    .extend() //extends a lists it can take multiple characters
    .split() //splits characters from each other and turns it into a list
    .len() // can also be used to get the length of a list
"""
states_of_america = ["Deleware", "Pennsylvania", "New Jersey"]

states_of_america[1] = "Pencilvania"  # changes the value of index
states_of_america.append("Daveland")  # appends to the end of the list
states_of_america.extend(["Daveland"])

print(states_of_america[0])

# dirty_dozen = ["Strawberries", "Spinach", "Kale", "Nectarines", "Apples",
#    "Grapes", "Peaches", "Cherries", "Pears", "Tomatoes", "Celery", "Potatoes"]

fruits = ["Strawberries", "Nectarines", "Apples",
          "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

dirty_dozen = [fruits, vegetables]
print(dirty_dozen)
# ---modules:
# a complex amount of code split up into groups
# you can create your own module by importing the name of the file
