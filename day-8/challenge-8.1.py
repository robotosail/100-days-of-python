#------------Surface area calculator-----------#
import math

# getting user data
test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
# setting the coverage to 5
coverage = 5

# defining a function called paint_calc: with the parameters height, width, and cover
def paint_calc(height, width, cover):
    # multiplying the height and width to get the area then dividing by the coverage
    # using math.ceil to round up
    number_of_cans = math.ceil((height * width) / cover)
    print(f"You need {number_of_cans} cans of paint.")


paint_calc(height=test_h, width=test_w, cover=coverage)
