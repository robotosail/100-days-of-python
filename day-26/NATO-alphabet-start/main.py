import pandas


data = pandas.read_csv("nato_phonetic_alphabet.csv")
# Loop through rows of a data frame
for (index, row) in data.iterrows():
    # Access index and row
    # Access row.student or row.score
    pass

phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}

word = input("Enter a word: ").upper()
output_list = [phonetic_dict[letter] for letter in word]
print(output_list)

# TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}
