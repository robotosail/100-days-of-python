#-------------PRIME NUmber Checker------------#
n = int(input("Check this number: "))

# creating function
def prime_checker(number):
    # setting variable 
    is_prime = True
    # looping through the each number from 2 to the number
    for num in range(2, number):
        # if the number is cleanly divisible the num then it is not a prime number
        if number % num == 0:
            is_prime = False
    if is_prime:
        print("it is a prime number")
    else:
        print("it is not a prime number")

prime_checker(number=n)