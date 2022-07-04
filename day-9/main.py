# dictionaries
programming_dictionary = {"Bug": "An error in a program that prevents the program from running as expected.",
                          "Function": "A piece of code that you can easily call over and over again."}

print(programming_dictionary["Bug"])

# adding new items to dictionary
programming_dictionary["Loop"] = "The action of doing something"

print(programming_dictionary)

# create an empty dictionary.
# it also wipes the dictionary
# empty_dictionary = {}

# edit an item in a dictionary
# programming_dictionary["Bug"] = "A moth in your computer"

# # Looping through a dictionary
# for key in programming_dictionary:
#     print(key)
#     # prints the value of the key
#     print(programming_dictionary[key])

# Nesting DIctionary in a Dictionary
travel_log = {
    "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "Total_Visits": 12},
    "Germany": {"cities_visited":["Berlin", "Hamburg", "Stuttgart"], "total_visits": 5}
    }

travel_log = [
    "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "Total_Visits": 12},
    "Germany": {"cities_visited": ["Berlin", "Hamburg", "Stuttgart"], "total_visits": 5}
]
 