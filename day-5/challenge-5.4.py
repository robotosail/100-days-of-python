#--------------FIZZ BUZZ--------------------#
# getting the numbers from 1 to  == 100
for number in range(1, 101):
    # checking if the number is divisible by 5 and 3
    if number % 3 == 0 and number % 5 == 0:
        # if it is print fizzbuzz
        print("FizzBuzz")
    # if it is not check if the number is divisible by only 3
    elif number % 3 == 0:
        # if so print fizz
        print("Fizz")
    # else if the number is divisible by 5 print buzz
    elif number % 5 == 0:
        print("Buzz")
    # if it is not divisible by anything just print the number
    else:
        print(number)
