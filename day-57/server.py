import requests
from flask import Flask, render_template
import random
from datetime import datetime as dt

app = Flask(__name__)


@app.route("/")
def home():
    random_number = random.randint(1, 10)
    date = dt.now()

    # sending the random_ number variable to the index.html so it can be used:
    # any thing put after the comma will be sent over it must be in the right format for it to be accessible
    #  the format is (name=value)
    return render_template("index.html", num=random_number, year=date.year)


@app.route("/guess/<name>")
def guess(name):
    # request for the api genderize.io
    gender_response = requests.get(
        "https://api.genderize.io")

    # getting the gender from the json data
    gender = gender_response.json()["gender"]

    # requesting for agify api
    age_response = requests.get(
        f"https://api.agify.io?name={name}")
    age = age_response.json()["age"]

    return render_template("guess.html", name=name, gender=gender, age=age)


# new route called blog


@app.route("/blog/<num>")
def get_blog(num):
    print(num)
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(blog_url)
    all_post = response.json()
    # print(all_post)
    return render_template("blog.html", posts=all_post)


if __name__ == "__main__":
    app.run(debug=True)
