#------------- LEAP YEAR CALCULATOR---------------#
year = int(input("Which year do you want to check? "))

# if the year is cleanly divisible by 4 move on else it is not a leap year
if year % 4 == 0:
    # if the year is cleanly divisible by 100 move on else it is a leap year
    if year % 100 == 0:
        # if the year is cleanly divisible by 400 then it is a leap year else it is not
        if year % 400 == 0:
            print(f"The year {year} is a Leap Year.")
        else:
            print(f"The year {year} is not a Leap Year.")
    else:
        print(f"The year {year} is a Leap Year.")
else:
    print(f"The year {year} is not a Leap Year.")
