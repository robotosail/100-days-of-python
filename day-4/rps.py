# |------------Rock / Paper / Scissors----------------|
import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
# putting the images in a list for easy access
choices = [rock, paper, scissors]
choices_string = ["rock", "paper", "scissors"]
# getting user data
player_choice = int(input(
    "What do you choose? Type 0 for Rock, 1 for Paper and 2 for Scissors: "))
# picking a random number between the length of the choice list
computer_choice = random.randint(0, len(choices) - 1)
lose = "You Lose!"
won = "You Won!"

# check if the user choice is valid
if player_choice >= 3 or player_choice < 0:
    print("that is not an option")
else:
    # making the win and lose condition
    print(
        f"You chose {choices_string[player_choice]}\n{choices[player_choice]}")
    print(
        f"The computer chose {choices_string[computer_choice]}\n{choices[computer_choice]}")
    if player_choice == 0 and computer_choice == 2:
        print(won)
    elif player_choice == 2 and computer_choice == 0:
        print(lose)
    elif player_choice == 1 and computer_choice == 2:
        print(lose)
    elif player_choice == 2 and computer_choice == 1:
        print(won)
    elif player_choice == 0 and computer_choice == 1:
        print(lose)
    elif player_choice == 1 and computer_choice == 0:
        print(won)
    elif player_choice == computer_choice:
        print("it is a tie")
