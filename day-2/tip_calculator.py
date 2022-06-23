#------------ Tip Calculator ----------------------#
print("Welcome to the tip calculator.")

# getting user input for the bill, tip and amount of people
bill = input("How much is the total bill? $")
tip = input("What percantage of tip would you like to give: 10, 12, or 15? ")
people = input("How many people are splitting the bill? ")

# dividing the tip by 100
tip = int(tip) / 100
# multiplying the tip with the bill to get the amount of tip to pay then adding it to the bill and dividing by the number of people.
result = (float(bill) + float(bill) * tip) / int(people)
# rounding the result to the second decimail place.
result = round(result, 2)
# printing the result.
print(f"Each person should pay: ${result}")