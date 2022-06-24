print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
age = int(input("How old are you? "))
bill = 0

# regular if and else condition
# if height >= 120:
#     print("You can ride the rollercoaster!")
# else:
#     print("Sorry, you have to grow taller before you can ride.")

# # nested if else condition
# if height >= 120:
#     print("You can ride the rollercoaster!")
#     if age >= 18:
#         print("You need to pay $12 dollars")
#     else:
#         print("You only need to pay $7")
# else:
#     print("Sorry, you have to grow taller before you can ride.")

# elif statement
if height >= 120:
    print("You can ride the rollercoaster!")
    if age < 12:
        bill = 5
        print("Child tickets are $5.")
    elif age <= 18:
        bill = 7
        print("YOuth tickets are $7")
    elif age >= 45 and age <= 55:
        print("Everything is going to be ok. Have a free ride. It is on us")
    else:
        bill = 12
        print("Adult tickets are $12.")
    photo = input("Do you want a photo taken? Y for yes or N for no. ")
    if photo == "Y":
        # Add $3 to their bill
        bill += 3
    print(f"Your total bill is {bill}")

else:
    print("Sorry, you have to grow taller before you can ride.")


'''
# Comparison Operators

    Operators       Meaning
    ---------       --------
        >           Greater than
        <           Less than
        >=          Greater than or equal to
        <=          Less than or equal to
        ==          Equal to
        !=          Not equal to
        %           Divdes a number by another number and gives you the remainder
    
* Remeber that one equal sign means that you are assigning to a variable, while two means you are checking.

# LOGICAL OPERATORS
    and
    or
    not
'''
