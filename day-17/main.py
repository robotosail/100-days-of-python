# creating a class
class User:
    # self refers to the object being created
    def __init__(self, user_id, username):
        # creating attributes - a variable associated with a class
        self.id = user_id
        # setting a default value
        self.username = username
        self.followers = 0
        self.following = 0
        print("new user created")
    # # it passes like you pass your turn
    # pass
    # creating a method: all methods must have a self attribute. The difference from a method and a function is that a method is inside a class

    def follow(self, user):
        # for each follow increase the number of the
        user.followers += 1
        self.following += 1


# creating a new object with the User class
user_1 = User("001", "David")
user_2 = User("002", "Egg")

user_1.follow(user_2)
print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)
