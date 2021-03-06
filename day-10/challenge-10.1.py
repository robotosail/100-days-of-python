def is_leap_year(year):
    # if the year is cleanly divisible by 4 move on else it is not a leap year
    if year % 4 == 0:
        # if the year is cleanly divisible by 100 move on else it is a leap year
        if year % 100 == 0:
            # if the year is cleanly divisible by 400 then it is a leap year else it is not
            if year % 400 == 0:
                return True
            else:
               return False
        else:
           return True
    else:
       return False

# checks how many days are in a month
def days_in_months(year, month):
    # if the month is greater than 12 or less than 1: it is an invalid month
    if month > 12 or month < 1:
        return "Invalid input"
    # an array that holds the amount of days in each month
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_leap_year(year) and month == 2:
        return 29
    return month_days[month - 1]


year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_months(year, month)
print(days)
