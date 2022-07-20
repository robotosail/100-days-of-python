# list comprehension

# numbers = [1, 2, 3, 4]
# # short hand version of for loop
# # new_list = [print(item) for item in list]
# new_list = [number + 1 for number in numbers]

# print(new_list)
# range_list = [n * 2 for n in range(1, 5)]
# print(range_list)

# # conditional list comprehentions

#     # it only adds the item if the test returns true
#     # new_list = [item for item in list if test]
#     names = ["Alex", "Beth", "Freddy", "Dave", "Caroline"]
#     # if the length fo the name is less than 5 add it to the new list
#     short_names = [name for name in names if len(name) < 5]
#     print(short_names)

#     cap_names = [name.upper() for name in names if len(name) < 5]
#     print(cap_names)


#     with open("file1.txt") as file1:
#         file1_data = file1.readlines()

#     with open("file2.txt") as file2:
#         file2_data = file2.readlines()

#     result = [int(num)
#               for num in file1_data if num in file2_data]

#     print(result)
import random
# Dictionary comprehension
names = ["Alex", "Beth", "Freddy", "Dave", "Caroline"]
students_scores = {student: random.randint(19, 100) for student in names}

passed_students = {student: score for (
    student, score) in students_scores.items() if score >= 60}
print(passed_students)
# passed_students = {key: value for (key, value) in dictionary.items()}
