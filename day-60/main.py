from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")

# login path

# use the method post to get the data from the html


@app.route("/login", methods=["post"])
def recieve_data():
    # to request the data sent from the form in the html use the request method
    name = request.form["username"]
    password = request.form["password"]
    return f"<h1>Name: {name} Password: {password}</h1>"


if __name__ == "__main__":
    app.run(debug=True)
