from flask import Flask

app = Flask(__name__)


def makebold(text):
    def bold():
        return f"<b>{text()}</b>"
    return bold


@app.route("/")
@makebold
def main():
    return "hello"


# any thing in the <> becomes a variable and parameter for the function greet
# @app.route("/<name>")
# this gets the name variable and every thing after it
# @app.route("/<path:name>")

# you can specify the data type of the variables - <int:nubmer>- int is the datatype and number is the variable
@app.route("/username/<name>/"
           "<int:number>")
def greet(name, number):
    return f"Hello {name}, you are {number} years old"


if __name__ == "__main__":
    # allowing it to run on debug mode so that it reloads the server on every change
    app.run(debug=True)
