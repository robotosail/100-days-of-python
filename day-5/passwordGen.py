#---------Password Gen----------#
import random
letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",
           "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
number = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
symbols = ["!", "@", "#", "$", "%", "&", "(", ")", "*", "+", ]

print("Welcome to the Python Password Generator")

number_of_letters = int(
    input("How many letters would you like in your password: "))

number_of_numbers = int(
    input("How many numbers would you like in your password: "))

number_of_char = int(
    input("How many special characters would you like in your password: "))

# Eazy -- it doesn't shuffle the password
# password = ""

# # looping through the number of letters the user wants in the password
# for letter in range(1, number_of_letters + 1):
#     # using random function to randomly choice a letter from the letters list
#     # setting the password to the the random letter
#     password += random.choice(letters)

# for num in range(1, number_of_numbers + 1):
#     # using random function to randomly choice a number from the numbers list
#     # setting the password to the the random number
#     password += random.choice(number)

# for char in range(1, number_of_char + 1):
#     # using random function to randomly choice a letter from the letters list
#     # setting the password to the the random letter
#     password += random.choice(symbols)
# print(password)

# Hard level
password_list = []
# looping through the number of letters the user wants in the password
for letter in range(1, number_of_letters + 1):
    # using random function to randomly choice a letter from the letters list
    # setting the password to the the random letter
    password_list += random.choice(letters)

for num in range(1, number_of_numbers + 1):
    # using random function to randomly choice a number from the numbers list
    # setting the password to the the random number
    password_list += random.choice(number)

for char in range(1, number_of_char + 1):
    # using random function to randomly choice a letter from the letters list
    # setting the password to the the random letter
    password_list += random.choice(symbols)

# shuffles the password so it appears random
random.shuffle(password_list)
print(password_list)

password = ""
# using for loop to turn the list into a string
for char in password_list:
    password += char
print(f"Your password is {password}")
