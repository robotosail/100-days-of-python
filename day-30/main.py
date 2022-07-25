# Catching and Handling Errors

# Catching generic Errors
# try:
#     file = open("a_file.txt")
# except:
#     file = open("a_file.txt", "w")
#     print("There was an error")

# Catching specific Errors
# *You can have multiple except
# try:
#     file = open("a_file.txt")
#     a_dictionary = {"key": "value"}
#     print(a_dictionary["something"])
# except FileNotFoundError:
#     file = open("a_file.txt", "W")
#     file.write("Something")
# except KeyError:
#     print("That key doesn't exist")

# Catching and getting hold of the error message
# try:
#     file = open("a_file.txt")
#     a_dictionary = {"key": "value"}
#     print(a_dictionary["l;fdsak"])
# except FileNotFoundError:
#     file = open("a_file.txt", "w")
#     file.write("Something")
# except KeyError as error:
#     print(f"The key {error} doesn't exist")

# Errors with Else
# try:
#     file = open("a_file.txt")
#     a_dictionary = {"key": "value"}
#     print(a_dictionary["key"])
# except FileNotFoundError:
#     file = open("a_file.txt", "w")
#     file.write("Something")
# except KeyError as error:
#     print(f"The key {error} doesn't exist")
# # happens if everything was successful
# else:
#     content = file.read()
#     print(content)
#     print("Successfully")
# # happens no matter what
# finally:
#     file.close()
#     print("file was closed")


# # Generating Your own Exceptions
# try:
#     file = open("a_file.txt")
#     a_dictionary = {"key": "value"}
#     print(a_dictionary["key"])
# except FileNotFoundError:
#     file = open("a_file.txt", "w")
#     file.write("Something")
# except KeyError as error:
#     print(f"The key {error} doesn't exist")
# # happens if everything was successful
# else:
#     content = file.read()
#     print(content)
#     print("Successfully")
# # happens no matter what
# finally:
#     file.close()
#     print("file was closed")
#     raise NameError("This is a made up error")

# fruits = ["Apple", "Pear", "Orange"]

# # TODO: Catch the exception and make sure the code runs without crashing.


# def make_pie(index):
#     try:
#         fruit = fruits[index]
#     except IndexError:
#         print("fruit" + " pie")
#     else:
#         print(fruit + " pie")


# make_pie(4)

facebook_posts = [
    {'Likes': 21, 'Comments': 2},
    {'Likes': 13, 'Comments': 2, 'Shares': 1},
    {'Likes': 33, 'Comments': 8, 'Shares': 3},
    {'Comments': 4, 'Shares': 2},
    {'Comments': 1, 'Shares': 1},
    {'Likes': 19, 'Comments': 3}
]

total_likes = 0

for post in facebook_posts:
    try:
        total_likes = total_likes + post['Likes']
    except KeyError:
        print("This person has no likes")
    else:
        print(total_likes)
