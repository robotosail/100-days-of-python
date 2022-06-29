#------------HANGMAN-------------#
import random
from hangman_art import logo, stages
import word_list

gameOver = False
# creating the word list
# word_list = ["ardvark", "baboon", "camel"]
# using choice function in random module to randomly pick a word in the word list
random_word = random.choice(word_list.word_list)
# creating a list to hold the blank spaces used for guessing
list = []
prev_guess = []
# the lives
live = 6

print("Welcome to HANGMAN")
print(logo)

# setting the list to be the length of the random word
for letter in random_word:
    list += "_"
print(f"The word is {random_word}")
# using while loop to make it ask you continously
while gameOver == False:
    # getting user input and making it lowercase
    guess = input("Guess a letter: ").lower()
    # looping through the length of the random word,
    # checking to see if the guessed letter matches any of the letters in the random word by using its index.
    if guess in prev_guess:
        print(f"You've already Guessed {guess}")
        # for debugging
        # print(prev_guess)
    else:
        # every time a guess is made store it.
        prev_guess.append(guess)

        for index in range(len(random_word)):
            # if the guess letter matches any letter in the random word
            # get the index position of the letter in the random word array and use it to replace the word with the guessed letter

            if guess == random_word[index]:
                # replacing the blank spaces with the guessed letter by using the index
                list[index] = guess

        # checking if the guessed letter is not in the random_word
        if guess not in random_word:
            # if the guessed letter is not correct, reduce the lives by 1
            live -= 1
            print(f"The letter \"{guess}\" is not in the word.")

            # if there is no more lives game over, End this loop
            if live == 0:
                gameOver = True
                print("You lose!")
                print(f"The word was {random_word}")

        # shows the player how many more lives they have left
        print(stages[live])
        # combines the list into a string
        print(f"{''.join(list)}")
        # checking if there is still blanks in the list. if not the game is over they won
        if "_" not in list:
            gameOver = True
            print("You Win!")
