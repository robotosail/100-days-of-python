from flask import Flask

# the name of a module in the flask module to be run
app = Flask(__name__)

# the url the user must go to inorder to view the file


@app.route("/")
def Hello_world():
    return "<h1>Hi world</h1>"


# runs the code automatically if the name is main - allows you to run the code normally instead of flask run
if __name__ == "__main__":
    app.run()
