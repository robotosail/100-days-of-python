# with open("weather_data.csv") as info:
#     # readlines turns each line into a list
#     data = info.readlines()
#     print(data)

# importing csv library
# import csv

# with open("Weather_data.csv") as data_file:
#     # creates a csv reader object that can be looped through
#     data = csv.reader(data_file)
#     # looping through the data
#     temperatures = []

#     for row in data:
#         if row[1] != "temp":
#             # getting the temperatures from the row
#             temperatures.append(int(row[1]))
#             # print(row)
#     print(temperatures)

import pandas

# data = pandas.read_csv("Weather_data.csv")
# # getting a specific column
# data["temp"]
# # turining the data into a dictionary
# temp_dict = data["temp"].to_dict()
# print(temp_dict)
# # turining the data into a list
# temp_list = data["temp"].to_list()
# print(len(temp_list))

# # getting average
# average = sum(temp_list) / len(temp_list)
# print(average)
# you can also do this much simplar
# print(data["temp"].mean())
# print(data["temp"].max())

# # Get Data in Columns
# print(data["condition"])
# print(data.condition)  # the line above is the same as this one

# get data in rows
# get the column you want to check
# print(data[data["day"] == "Monday"])
# print(data[data.temp == data.temp.max()])
# print(data[data["day"]])

# monday = data[data.day == "Monday"]
# monday_temp = int(monday.temp)

# print((monday_temp * 9/5) + 32)

# creating a data frame from scratch
# data_dict = {
#     "Students": ["Amy", "George", "Juan"],
#     "Scores": [76, 90, 10]
# }
# data = pandas.DataFrame(data_dict)
# # print(data)
# data.to_csv("newdata.csv")

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

grey_squirels = len(data[data["Primary Fur Color"] == "Gray"])
black_squirels = len(data[data["Primary Fur Color"] == "Black"])
cinnamon_squirels = len(data[data["Primary Fur Color"] == "Cinnamon"])

print(grey_squirels)
print(black_squirels)
print(cinnamon_squirels)

data_dict = {
    "Fur Color": ["Gray", "cinnamon", "Black"],
    "Count": [grey_squirels, black_squirels, cinnamon_squirels]
}

# print(data_dict)
df = pandas.DataFrame(data_dict)
df.to_csv("new_squirrel.csv")
