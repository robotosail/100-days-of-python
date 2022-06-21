age = input("What is your current age? ")

age_as_int = int(age)

years_remaining = 90 - age_as_int
days_remaining = years_remaining * 365
weeks_remaining = years_remaining * 52
months_remaining = years_remaining * 12

print(f"You have {years_remaining} years remaining, {months_remaining} months remaining, {weeks_remaining} weeks remaining, and {days_remaining} days remaining")