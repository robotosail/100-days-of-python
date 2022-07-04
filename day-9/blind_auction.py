#-----------------Blind auction----------------#
import os
from art import logo
# creating a dictionary to hold the bids and the names of the bidders
bids = {}
bidding = True

# creating a function to push the values to the bids dictionary
def autctioneer(record):
    highest_bid = 0
    name = ""
    # looping through the key in the bids dictionary
    for key in record:
        # setting the value of the key to a variable: for easier access
        bid = record[key]
        # if the value of the key is greater then the variable highest
        if bid > highest_bid:
            # set the highest to the value of that key
            highest_bid = bid
            # set the name of the person to the
            name = key
    # printing the winner
    print(f"The winner is {name} with a bid of ${highest_bid}")

# while bidding is true run 
while bidding == True:
    # getting user input
    print(logo)
    name = input("What is your name: ")
    bid = int(input("How much are you bidding: $"))
    again = input(
        "Are there any other bidders: 'Y' for yes or 'N' for no: ").lower()
    # pushing the input to the bids
    bids[name] = bid
    # checking if there is any bidders left.
    if "n" in again:
        bidding = False
        # calling function to check the highest bid
        autctioneer(bids)
    else:
        # clears the terminal
        os.system("cls")