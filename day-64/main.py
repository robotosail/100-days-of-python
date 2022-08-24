# Movie library

from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField
from wtforms.validators import DataRequired
import requests

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///movie.collection.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Bootstrap(app)

movieid = 1
url = "https://api.themoviedb.org/3/search/movie/"
key = "your api key"


class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False, unique=True)
    title = db.Column(db.String, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String, nullable=False)
    rating = db.Column(db.String, nullable=False)
    ranking = db.Column(db.String, nullable=False)
    review = db.Column(db.String, nullable=False)
    img_url = db.Column(db.String, nullable=False)

    def __repr__(self):
        return "<Movie %r>" % self.title


class EditForm(FlaskForm):
    rating = StringField("Your rating out of 10", validators=[
        DataRequired(message="This field is required")], name="rating")
    review = StringField("Your review", validators=[
                         DataRequired(message="This field is required")], name="review")
    submit = SubmitField("Done")


class AddForm(FlaskForm):
    movie_title = StringField("Movie Title", validators=[DataRequired(
        message="You need a movie title")], name="title")
    submit = SubmitField("Add Movie")


db.create_all()

# new_movie = Movie(id=1,
#                   title="Phone Booth",
#                   year=2002,
#                   description="Publicist Stuart Shepard finds himself trapped in a phone booth, pinned down by an extortionist's sniper rifle. Unable to leave or receive outside help, Stuart's negotiation with the caller leads to a jaw-dropping climax.",
#                   rating=7.3,
#                   ranking=10,
#                   review="My favourite character was the caller.",
#                   img_url="https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg"
#                   )
# db.session.add(new_movie)
# db.session.commit()


@ app.route("/")
def home():
    # creates a list of all movies sorted by their rating
    all_movies = Movie.query.order_by(Movie.rating).all()

    # # loop through all the movies
    for i in range(len(all_movies)):
        # reverse the order the movies  ranking
        all_movies[i].ranking = len(all_movies) - i
    db.session.commit()
    return render_template("index.html", movies=all_movies)


@app.route("/edit", methods=["POST", "GET"])
def edit():
    form = EditForm()
    # checking if the forms validation was successful
    if form.validate_on_submit():
        # getting the id from the html
        movieid = request.args.get("id")
        edited_movie = Movie.query.get(movieid)
        edited_movie.rating = form.rating.data
        edited_movie.review = form.review.data
        db.session.commit()
        return redirect(url_for("home"))

    return render_template("edit.html", form=form)


@app.route("/delete")
def delete():
    # getting the id of the movie that is to be deleted
    movieid = request.args.get("id")
    # using that id get it from the database and delete it
    removed_movie = Movie.query.get(movieid)
    db.session.delete(removed_movie)
    db.session.commit()
    return redirect(url_for("home"))


@app.route("/add", methods=["GET", "POST"])
def add():
    form = AddForm()

    if form.validate_on_submit():
        movie_title = form.movie_title.data
        data = requests.get(
            url, params={"api_key": key, "query": movie_title}).json()["results"]
        print(data)
        return render_template("select.html", options=data)

    return render_template("add.html", form=form)


@app.route("/find", methods=["GET", "POST"])
def find_movie():
    global movieid
    movie_api_id = request.args.get("id")
    if movie_api_id:
        new_url = f"https://api.themoviedb.org/3/movie/{movie_api_id}"
        movieid += 1
        response = requests.get(
            new_url, params={"api_key": key, "language": "en-US"})
        data = response.json()

        new_movie = Movie(
            id=movieid,
            title=data["title"],
            year=data["release_date"].split('-')[0],
            description=data["overview"],
            ranking="None",
            review="None",
            rating="None",
            img_url=f'https://image.tmdb.org/t/p/w600_and_h900_bestv2{data["poster_path"]}',
        )
        db.session.add(new_movie)
        db.session.commit()
    return redirect(url_for("edit", id=movieid))


if __name__ == '__main__':
    app.run(debug=True)
