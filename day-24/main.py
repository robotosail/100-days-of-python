# opens a file
# it takes the file to be opened, the mode to open it in like r to read or w to write,
# file = open("test.txt", "w")
# contents = file.read()
# print(contents)
# file.close()

# much better just incase you forget to close the file
# another method of reading a file
# with open("test.txt") as file:
#     contents = file.read()
#     print(contents)

# writing into a file by deleting the previous contents of the file
# with open("test.txt", mode="w") as file:
#     file.write("new texts.")
# adds the writing to the file
with open("test.txt", mode="a") as file:
    file.write("\nnew texts.")

with open("newfile.txt", mode="w") as file:
    file.write("\nnew texts.")
