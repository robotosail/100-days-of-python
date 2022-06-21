# adding two digit numbers together
two_digit_number = input("Type a two digit number: ")

# separating the two digits by using subscript
first_digit = two_digit_number[0]
second_digit = two_digit_number[1]

# converting the first and second digits, then adding them together
result = int(first_digit) + int(second_digit)

# printing out result
print(result)