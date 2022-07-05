#---------------- Guessing Game ---------------#
# importing random module
import random
import art

# setting amount of tries based on difficulty lvl.
def set_difficulty():
    # asking for difficulty level
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

    if(difficulty == "easy"):
        return 10
    elif(difficulty == "hard"):
        return 5
    # Failsafe
    else:
        print("not an option")

# Checking if the number is low or high
def check(guess, answer, tries):
    """Checks if the users guess is high or low. Returns tries remaining"""
    if guess > answer:
        print("Too high")
        return tries - 1
    elif guess < answer:
        print("Too low")
        return tries - 1
    # Fail Safe
    else:
       print(f"You got it! the answer was {answer}")

# while loop: Make continous
def game():
    print(art.logo[random.randint(0, 1)])
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    # randomly picking a number between 1 and a 100
    chosen_num = random.randint(1, 100)
    # setting tries to equal the number gotten back fromt the function
    tries = set_difficulty()
    guess = 0
    while guess != chosen_num:
        # printing amount of lives
        print(f"You have {tries} attempts remaining.")
        guess = int(input("Guess: "))
        # set tries to the value gotten from check function
        tries = check(guess, chosen_num, tries=tries)

        # checks if the there is no more lives
        if tries == 0:
            print("You lose!")
            print(f"The number was {chosen_num}")
            return # exits the function
        elif guess != chosen_num:
            print("Guess again.")
game()