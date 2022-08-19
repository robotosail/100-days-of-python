from venv import create


class User:
    def __init__(self, name):
        self.name = name
        self.is_logged_in = False


def is_authenticated(function):
    # giving args and kwargs so the it can have access to the is_logged_in attribute
    def wrapper(*args, **kwargs):
        # getting
        if args[0].is_logged_in == True:
            function(args[0])
    return wrapper


@is_authenticated
def create_blog_post(user):
    print(f"This is {user.name}'s new post")


new_user = User("David")
new_user.is_logged_in = True
create_blog_post(new_user)
