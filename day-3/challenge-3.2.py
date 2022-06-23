#---------- BMI CALCULATOR 2.0 -------------#
print("WELCOME TO BMI CALCULATOR")
height = float(input("Enter your height in meters: "))
weight = float(input("Enter your weight in kilograms: "))

bmi = round(weight / (height ** 2))

print(f"your BMI is {bmi}")

# if the bmi is less than 18.5
if bmi < 18.5:
    print("You are underweight. You need to eat more.")
# if the bmi is greater than 18.5 but less than 25
elif bmi < 25:
    print("You're weight is normal good job.")
elif bmi < 30:
    print("You are overweight! HIT THE GYM!")
elif bmi < 35:
    print("YOU HAVE OBESITY! START GOING ON DIETS.")
else:
    print("YOU ARE CLINICALLY OBESE! START GOING ON DIETS AND HIT THE GYM BEFORE YOU DIE")
