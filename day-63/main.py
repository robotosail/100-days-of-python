from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///book-collection.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# instanciating the database
db = SQLAlchemy(app)

# all_books = []
id = 0


# creating a class to add a new book to the data
class AddBook(db.Model):
    # creating the column called id, title, author, rating
    id = db.Column(db.Integer, primary_key=True, nullable=False, unique=True)
    title = db.Column(db.String, unique=True, nullable=False)
    author = db.Column(db.String, nullable=False)
    rating = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return "<Book %r>" % self.title


@app.route('/')
def home():
    # checking the database
    all_books = db.session.query(AddBook).all()
    # sending the data over to the html
    return render_template("index.html", books=all_books)


@app.route("/add", methods=["GET", "POST"])
def add():
    global id
    if request.method == "POST":
        # increasing the id
        id += 1
        # getting the data from the html form
        book_title = request.form["Title"]
        book_Author = request.form["Author"]
        book_Rating = request.form["Rating"]
        # creating a new book based on the data field from the html
        new_book = AddBook(id=id, title=book_title,
                           author=book_Author, rating=book_Rating)
        # adding the new data to the database
        db.session.add(new_book)
        db.session.commit()
        # redirecting back to the home page
        return redirect(url_for("home"))
    return render_template("add.html")


@app.route("/edit", methods=["GET", "POST"])
def edit():
    if request.method == "POST":
        # getting the title of the book you want to change the rating to
        bookid = request.form["title"]
        updated_book_rating = AddBook.query.filter_by(title=bookid).first()
        updated_book_rating.rating = request.form["rating"]
        # commiting the changes to the database
        db.session.commit()
    # getting the parameter id from the url get method
    bookid = request.args.get("id")
    # using the id then get the book info and send it to the html
    requestedBook = AddBook.query.get(bookid)
    return render_template("edit.html", book=requestedBook)


@app.route("/delete", methods=["GET"])
def delete():
    bookid = request.args.get("id")
    delete_book = AddBook.query.get(bookid)
    db.session.delete(delete_book)
    db.session.commit()
    return redirect(url_for("home"))


if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)
