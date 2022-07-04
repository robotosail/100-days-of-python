#---------------Black Jack--------------#
from os import system
from art import logo
import random

# function that deals cards randomly


def Deal_card():
    """Returns a random card from the cards list using the random.choice function"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

# function to calculate the score


def calc_score(cards):
    """calculates the score and returns the value"""
    # checking if the hand has a score of 21 and the length of the cards is 2
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    # if the hand is greater than 21 and there is an 11 change it to a 1
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


def compare(user_score, computer_score):
    if user_score == computer_score:
        return "Draw"
    elif computer_score == 0:
        return "You lose!\nComputer had a Blackjack"
    elif user_score == 0:
        return "You Win!"
    elif user_score > 21:
        return "You lose, your score was more than 21"
    elif computer_score > 21:
        return "You Win, computer score was more than 21"
    elif user_score > computer_score:
        return "You win"
    else:
        return "You lose"

def Game():
    print(logo)
    user_cards = []
    computer_cards = []

    # creating a loop to run twice
    for n in range(2):
        # appending the new cards to the user card
        user_cards.append(Deal_card())
        # appending the new cards to the computer card
        computer_cards.append(Deal_card())

    gameOver = False
    while not gameOver:
        # getting hold of the user and the computers score
        user_score = calc_score(user_cards)
        computer_score = calc_score(computer_cards)

        print(f"Your cards are: {user_cards};\nYour score is {user_score}")
        print(f"Computer's first card is: {computer_cards[0]}")
        if user_score == 0 or computer_score == 0 or user_score > 21:
            gameOver = True
        else:
            ask = input(
                "Do you want to get another card? 'Y' for yes or 'n' for no: ").lower()
            if ask == "y":
                user_cards.append(Deal_card())
            else:
                gameOver = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(Deal_card())
        computer_score = calc_score(computer_cards)

    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(
        f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score=user_score, computer_score=computer_score))

# asking user if they want to play again
while input("Do you want to play a game of Blackjack? 'Y' for yes or 'N' for no: ") == "y":
    Game()
    # clears the screen
    system("clear")