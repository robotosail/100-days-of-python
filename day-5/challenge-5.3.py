#----------Adds all even numbers from 1 to 100------------------#
total = 0
# using range to get the numbers between 1 and 101 by incrementing by 2
for number in range(2, 101, 2):
    total += number
print(total)

# another way
total2 = 0
for number in range(1, 101):
    # for every number that is cleanly divisible by two add that number with the total
    if number % 2 == 0:
        total2 += number
print(total2)
