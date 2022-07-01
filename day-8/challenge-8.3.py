#-----------CEASER CIPHER------------#
import art
# creating a list of all the alphabet
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y",
            "z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

print(art.logo)
# creating a function to encrypt and decrypt user input
def ceasar(start_text, shift_amount, direction):
    end_text = ""
    # checking if the direction is to decode
    if direction == "decode":
        # multiply the shift amount by -1
        shift_amount *= -1
    # looping through each letter in the the start text
    for char in start_text:
        # checking if the character is in the alphabet list
        if char in alphabet:
            # getting the indexed position of the char from the alphabet then adding it with the shift amount
            # 5 * -1 = -5
            new_position = alphabet.index(char) + shift_amount
            # getting the new letter from the alphabet using the new index
            # adding the new letter to the cipher text
            end_text += alphabet[new_position]
            # printing out the cipher text
        # else just add the character to the end text
        else:
            end_text += char
    print(f"The {direction}d text is {end_text}")


# getting user input
Continue = True
while Continue == True:
    direction = input("Type \"encode\" to encrypt, or \"decode\" to decrypt: ").lower()
    text = input("Type your message: ").lower()
    shift = int(input("Type the shift number: "))
    # dividing the shift number by 26 until there is no remainder
    shift = shift % 26
    ceasar(start_text=text, shift_amount=shift, direction=direction)
    ask = input("Do you want to go again? 'Y' for yes or 'N' for no: ").lower()

    if ask == "n":
        Continue = False
        print("GoodBye!")
