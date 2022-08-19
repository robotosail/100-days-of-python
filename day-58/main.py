import os
import smtplib
from flask import Flask, render_template, request
import requests

# data = requests.get("https://api.npoint.io/0efb6deb54a7e17a1679").json()
data = [
    {
        "id": 1,
        "title": "The Life of Cactus",
        "subtitle": "Who knew that cacti lived such interesting lives.",
        "body": "Nori grape silver beet broccoli kombu beet greens fava bean potato quandong celery. Bunya nuts black-eyed pea prairie turnip leek lentil turnip greens parsnip. Sea lettuce lettuce water chestnut eggplant winter purslane fennel azuki bean earthnut pea sierra leone bologi leek soko chicory celtuce parsley jícama salsify."
    },
    {
        "id": 2,
        "title": "Top 15 Things to do When You are Bored",
        "subtitle": "Are you bored? Don't know what to do? Try these top 15 activities.",
        "body": "Chase ball of string eat plants, meow, and throw up because I ate plants going to catch the red dot today going to catch the red dot today. I could pee on this if I had the energy. Chew iPad power cord steal the warm chair right after you get up for purr for no reason leave hair everywhere, decide to want nothing to do with my owner today."
    },
    {
        "id": 3,
        "title": "Introduction to Intermittent Fasting",
        "subtitle": "Learn about the newest health craze.",
        "body": "Cupcake ipsum dolor. Sit amet marshmallow topping cheesecake muffin. Halvah croissant candy canes bonbon candy. Apple pie jelly beans topping carrot cake danish tart cake cheesecake. Muffin danish chocolate soufflé pastry icing bonbon oat cake. Powder cake jujubes oat cake. Lemon drops tootsie roll marshmallow halvah carrot cake."
    }
]


app = Flask(__name__)


@app.route("/")
def home():
    # app.url_for('static', filename='css/style.css')
    return render_template("index.html", data=data)


# about page
@app.route("/about")
def about():
    return render_template("about.html")


# contact page
@app.route("/contact", methods=["post", "get"])
def contact():
    print(request.method)
    # checking if the method was a post or a get request
    if request.method == "POST":
        # if so get from the form tag get the element with a name username, email, and phone
        username = request.form["username"]
        email = request.form["email"]
        phone = request.form["phone"]
        message = request.form["message"]
        print(username, email, phone)
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(os.getenv("USR"), os.getenv("PWD"))
            connection.sendmail(os.getenv("USR"), os.getenv(
                "USR"), msg=f"Subject: New User from {app.url_for('home', _external=True)}\n\nName: {username}\nEmail: {email}\nPhone: {phone}\nMessage: {message}")
            return "Successfully submitted"
    else:
        # if not just render the html page
        return render_template("contact.html")


@app.route("/post/<int:postid>")
def get_post(postid):
    for blog in data:
        if blog["id"] == postid:
            return render_template("post.html", post=blog)
    return "Sorry this post is not found"


if __name__ == "__main__":
    app.run(debug=True)
