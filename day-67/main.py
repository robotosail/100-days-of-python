from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditor, CKEditorField
from datetime import datetime as dt

# Delete this code:
# import requests
# posts = requests.get("https://api.npoint.io/43644ec4f0013682fc0d").json()

app = Flask(__name__)
Bootstrap(app)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
ckeditor = CKEditor(app)

# CONNECT TO DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# DATE TIME MODULE
date = dt.now()

# CONFIGURE TABLE


class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    subtitle = db.Column(db.String(250), nullable=False)
    date = db.Column(db.String(250), nullable=False)
    body = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    img_url = db.Column(db.String(250), nullable=False)


# WTForm
class CreatePostForm(FlaskForm):
    title = StringField("Blog Post Title", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    author = StringField("Your Name", validators=[DataRequired()])
    img_url = StringField("Blog Image URL", validators=[DataRequired(), URL()])
    # use ckeditorfield instead
    body = CKEditorField("Blog Content", validators=[DataRequired()])
    submit = SubmitField("Submit Post")


@app.route('/')
def get_all_posts():
    posts = db.session.query(BlogPost).all()
    return render_template("index.html", all_posts=posts)


@app.route("/post/<int:index>")
def show_post(index):
    posts = db.session.query(BlogPost).get(index)
    return render_template("post.html", post=posts)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/new-post", methods=["GET", "POST"])
def new_post():
    form = CreatePostForm()
    if request.method == "POST":
        if form.validate_on_submit():
            # gets the full name of the month
            new_date = date.now().strftime("%B %d, %Y")

            # creating a new post using the sent data
            new_post = BlogPost(
                title=form.title.data,
                subtitle=form.subtitle.data,
                author=form.author.data,
                body=form.body.data,
                img_url=form.img_url.data,
                date=new_date
            )
            # adding it to the database
            db.session.add(new_post)
            db.session.commit()

    return render_template("make-post.html", form=form)


@app.route("/edit/<post_id>", methods=["GET", "POST"])
def edit_post(post_id):
    postid = BlogPost.query.get(post_id)
    # automatically fill the form
    edit_form = CreatePostForm(
        title=postid.title,
        subtitle=postid.subtitle,
        author=postid.author,
        body=postid.body,
        img_url=postid.img_url

    )
    # FORM VALIDATION
    if edit_form.validate_on_submit():
        postid.title = edit_form.title.data
        postid.subtitle = edit_form.subtitle.data
        postid.author = edit_form.author.data
        postid.body = edit_form.body.data
        postid.img_url = edit_form.img_url.data
        # postid.date = date.now().strftime("%B %d, %Y")
        # updating the database
        db.session.commit()
        return redirect(url_for("show_post", index=postid.id))
    return render_template("make-post.html", form=edit_form, is_edit=True)


@app.route("/delete/<post_id>", methods=["GET"])
def delete(post_id):
    post_to_delete = BlogPost().query.get(post_id)
    db.session.delete(post_to_delete)
    db.session.commit()
    return redirect(url_for("get_all_posts"))


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=500, debug=True)
