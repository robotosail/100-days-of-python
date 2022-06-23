# ------------------- EVEN OR ODD ------------------#
# getting the user data
number = int(input("Which number do you want to check? "))

# checking if there is a remainder when the number is divided by 2
if number % 2 == 0:
    print(f"The number {number} is an even number.")
else:
    print(f"The number {number} is an odd number.")

# the % sign divides two numbers together and returns the remainder
