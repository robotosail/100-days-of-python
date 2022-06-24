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

true = str(t+r+u+e)
Love = str(l+o+v+e)

love_score = int(true + Love)

if (love_score < 10) or (love_score > 90):
    print(
        f"your love score is {love_score}, you go together like coke and mentos.")
elif (love_score >= 40) and (love_score <= 50):
    print(f"your love score is {love_score}, you are fine together")
else:
    print(f"your love score is {love_score}")

# Lower function
# .lower() reduces the letters in a string to lowercase
# count function
# gives you the number of time a letter occures in a string, it is case sensitive
