print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is crushes name? \n")

concatinate_name = (name1 + name2).lower()

t = concatinate_name.count("t")
r = concatinate_name.count("r")
u = concatinate_name.count("u")
e = concatinate_name.count("e")
l = concatinate_name.count("l")
o = concatinate_name.count("o")
v = concatinate_name.count("v")
e2 = concatinate_name.count("e")

True_Score = t+r+u+e
Love = l+o+v+e
# Lower function
# .lower() reduces the letters in a string to lowercase
# count function
# gives you the number of time a letter occures in a string, it is case sensitive
