#-------------BILL PAYER----------#

# importing the random module
import random

# getting user input
names_string = input("Give me everybody's names, seperated by a comma: ")
# seperating the names into a list and removing the commas and spaces
names = names_string.split(", ")
# getting the length of the list by using len
names_length = len(names)
# using the random integer generator to get the index
random_person = random.randint(0, names_length - 1)

# printing the person who is buying the meal
print(f"The person to pay the bill is {names[random_person]}")
