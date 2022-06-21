#-----------BMI Calculator------------
# getting the data
height = input("What is your height in meters: ")
weight = input("What is your weight in kilograms: ")

# turning the data into a float and doing the required calculations
result = float(weight) / float(height)**2

# converting the results in to an integer and printing it out
print(int(result))