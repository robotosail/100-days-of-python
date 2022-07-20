# weather_c = {
#     "Monday": 12,
#     "Tuesday": 14,
#     "Wednesday": 15,
#     "Thursday": 14,
#     "Friday": 21,
#     "Saturday": 22,
#     "Sunday": 24,
# }
# # 🚨 Don't change code above 👆

# weather_f = {day: (temp*9/5)+35 for (day, temp) in weather_c.items()}
# # Write your code 👇 below:


# print(weather_f)

import pandas
student_dict = {
    "student": ["Angela", "kim", "rob"],
    "Score": [56, 76, 98]
}

# # looping through dictionaries
# for (key, value) in student_dict.items():
#     print(value)
student_df = pandas.DataFrame(student_dict)

# for (key, value) in student_df.items():
#     print(key)
#     print(value)

# loop through rows of data frame
for (index, row) in student_df.iterrows():
    print(index)
    print(row)
    print(row.student)
