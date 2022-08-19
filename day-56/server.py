from unicodedata import name
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    #  rendering an html file - html file must be in a folder called template
    # and every other files like css and images must be in a folder called static
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
