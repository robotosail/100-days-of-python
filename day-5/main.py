# Loops:-
#   For loops:-
#       looks through a list and assigns each value to a variable
#
#   For loops with range:-
#       it gets hold of numbers between the two specified; doesn't get the last number
#       it can take up to 3 values, the start, end and the number it should increment by
#       for number in range(a, b):
#           print(number)
#       for number in range(a, b, 3):
#           print(number)

# fruits = ["Apple", "Peach", "Pear"]

# # loops throught the fruits list and prints out the fruit
# for fruit in fruits:
#     print(fruit)
#     print(fruit + " Pie")

# # for loop gets hold of the numbers between 1 and 10
# for number in range(1, 10):
#     print(number)

total = 0
for number in range(1, 101):
    total += number
print(total)
