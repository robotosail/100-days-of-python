#-------------Treasure Map----------------#
from tkinter import HORIZONTAL


row1 = ["▢ ", "▢ ", "▢ "]
row2 = ["▢ ", "▢ ", "▢ "]
row3 = ["▢ ", "▢ ", "▢ "]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure: ")

# getting the first and second value of the user input then turning it into an integer, then assigning it to a variable
horizontal = int(position[0])
vertical = int(position[1])
# print(horizontal)
# getting the position from the list
map[vertical - 1][horizontal - 1] = "x"
print(f"{row1}\n{row2}\n{row3}")
