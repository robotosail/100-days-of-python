# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

# the names of the files
# increment = 1
# # getting the contents of the starting letter file
# with open("Input/Letters/starting_letter.txt") as file:
#     # saving the contents into a variable
#     contents = file.read()

# # getting the list of names
# with open("Input/Names/invited_names.txt") as name:
#     # storing it to a variable then removing whitespaces and \n
#     names = name.read()
#     # turn the names into a list after removing the whitespaces and \n
#     names = names.split()

# for name in names:
#     with open(f"Output/ReadyToSend/{name}'s invitation.txt", mode="w") as output:
#         # loop through the list of names
#         # replacing the the string name with the name and assigning it to a variable so it doesn't overwrite
#         new_contents = contents.replace("[name]", name)
#         # writing in to the newly created file
#         output.write(f"{new_contents}")
#         increment += 1

# or
# getting the list of names
with open("Input/Names/invited_names.txt") as name:
    # storing the names into a list
    names = name.readlines()
# getting the contents of the starting letter file
with open("Input/Letters/starting_letter.txt") as file:
    # saving the contents into a variable
    contents = file.read()

# loop through the list of names
    for name in names:
        # removing the whitespaces from the names
        stripped_name = name.strip()
        # replacing the the placeholder name with the name and assigning it to a variable so it doesn't overwrite
        new_contents = contents.replace("[name]", stripped_name)
        print(new_contents)

        with open(f"Output/ReadyToSend/letter_for_{stripped_name}.txt", mode="w") as output:
            # writing in to the newly created file
            output.write(f"{new_contents}")
