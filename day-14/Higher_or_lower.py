#----------------Higher or lower-------------#

#           __  ___       __
#          / / / (_)___ _ / /_  ___  _____
#         / /_/ / / __ `/ __ \/ _ \/ ___/
#        / __  / / /_/ / / / /  __/ /
#       /_/ ///_/\__, /_/ /_/\___/_/
#      / /  /____/_      _____  _____
#     / /   / __ \ | /| / / _ \/ ___/
#    / /___/ /_/ / |/ |/ /  __/ /
#   /_____/\____/|__/|__/\___/_/

import random
from art import logo, vs
from data import data
from os import system

# function to format the data


def format_data(account):
    """Returns the formatted version of the account dataformats the data gotten """
    # format the data
    # getting the account name from the dictionary
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_descr}, from {account_country}"

# function to check which account has more followers


def check(account1, account2, guess):
    """returns the account with the most followers"""
    count1 = account1["follower_count"]
    count2 = account2["follower_count"]
    if count1 < count2:
        return guess == "b"
    else:
        return guess == "a"


def game():
    # Generate a random account from the game data.
    account_b = random.choice(data)
    gameOver = False
    score = 0
    while not gameOver:

        # changing a to b
        account_a = account_b
        account_b = random.choice(data)
        # checking that the accounts are different from each other
        while account_a == account_b:
            account_b = random.choice(data)

        # printing the data to compare to
        print(f"Compare A: {format_data(account_a)}.")
        print(vs)
        print(f"Compare B: {format_data(account_b)}.")
        # ask user for guess
        guess = input("Who has the most followers? Type A or B: ").lower()
        correct_answer = check(account_a, account_b, guess)
        system("cls")
        # display art
        print(logo)
        # check if user is correct.
        if correct_answer:
            score += 1
            print(f"Correct! Your score is {score}")
        else:
            print(f"Wrong")
            print(f"Your score was: {score}")
            gameOver = True


game()
# track score
