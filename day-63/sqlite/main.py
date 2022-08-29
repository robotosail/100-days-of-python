# import sqlite3
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# connecting to a new database(if it doesn't exist it will be created by default)
# db = sqlite3.connect("books-collection.db")
# # creating a cursor to use to add rows
# cursor = db.cursor()
# # tells the cursor to execute an action(Most actions are a form of sql (Structured query language) commands)
# # CREATE TABLE- creates a new table in the database and the name of the table comes after.
# # The part in the parenthesis are the fields or the column headings
# # The first field is id with a data type of Primary key,
# #  this is because it is one piece of data that uniquely identifies each data in the table
# # The second field is Title and it has a maximum length of 250 characters.
# # The third is Author
# # The last is Rating
# # varchar: the maximum length of the value
# # NOT NULL: its value must not be empty
# # UNIQUE: No two piece of data can have the same value
# # FLOAT: a field that accepts float numbers as a datatype
# cursor.execute(
#     "CREATE TABLE books(id INTEGER PRIMARY KEY, Title varchar(250) NOT NULL UNIQUE, Author varchar(250) NOT NULL, Rating FLOAT NOT NULL)")

# # adding data to table
# cursor.execute(
#     "INSERT INTO books VALUES(1, 'Harry Potter', 'J.k', 'Rowling', '9.3'")

# # commiting changes to database
# db.commit()
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///new-books-collection.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), unique=True, nullable=False)
    author = db.Column(db.String(120), nullable=False)
    rating = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return '<Book %r>' % self.title


db.create_all()

# only run this once
# it creates a new record
# new_book = Book(id=1, title="Harry Potter", author="J. K. Rowling", rating=9.3)
# db.session.add(new_book)
# db.session.commit()

# # to read all records
# all_books = db.session.query(Book).all()
# print(all_books)

# # read a particular record by query
# book = Book.query.filter_by(title="Harry Potter").first()
# print(book)

# update a particular record
# book_to_update = Book.query.filter_by(title="Harry Potter").first()
# book_to_update.title = "This is a test"
# db.session.commit()

# # update by primary key
# book_id = 2
# book_to_update = Book.query.get(book_id)
# book_to_update.title = "This is a test"
# db.session.commit()

# # delete record by key
# book_id = 4
# book_to_delete = Book.query.get(book_id)
# db.session.delete(book_to_delete)
# db.session.commit()

# # deletes a table
# User.__table__.drop(db.engine)
# db.session.commit()
