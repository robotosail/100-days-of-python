import pandas


data = pandas.read_csv("nato_phonetic_alphabet.csv")
# Loop through rows of a data frame
for (index, row) in data.iterrows():
    # Access index and row
    # Access row.student or row.score
    pass

phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}


def gen_phonetic():
    word = input("Enter a word: ").upper()
    try:
        output_list = [phonetic_dict[letter] for letter in word]
    except KeyError:
        print("Please, only type letters")
        gen_phonetic()
    else:
        print(output_list)


gen_phonetic()
# TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}
