from flask import Flask, render_template, redirect, url_for, flash, request
from flask_bootstrap import Bootstrap
from flask_ckeditor import CKEditor
from datetime import date
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.engine import Engine
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user
from forms import CreatePostForm, RegisterForm, LoginForm, CommentForm
from flask_gravatar import Gravatar

# INITIALIZING
app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
ckeditor = CKEditor(app)
Bootstrap(app)
Base = declarative_base()

# CONNECT TO DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# LOGIN
login_manager = LoginManager(app)
logged_in = False
display_btn = False

# using gravatar for profile pic
# :param app: Your Flask app instance
# :param size: Default size for avatar
# :param rating: Default rating
# :param default: Default type for unregistred emails
# :param force_default: Build only default avatars
# :param force_lower: Make email.lower() before build link
# :param use_ssl: Use https rather than http
# :param base_url: Use custom base url for build link
gravatar = Gravatar(app, size=100, rating="pg-13", default="retro", force_default=False,
                    force_lower=False, use_ssl=False, base_url=None)


# CONFIGURE TABLES
class User(UserMixin, db.Model, Base):
    __tablename__ = "User"
    id = db.Column(db.Integer, primary_key=True, unique=True)
    email = db.Column(db.String, nullable=False, unique=True)
    name = db.Column(db.String, nullable=False, unique=False)
    password = db.Column(db.String, nullable=False, unique=False)

    # creates a reference to the author in blog post
    posts = relationship("BlogPost", back_populates="author")
    comments = relationship("Comment", back_populates="comment_author")


class BlogPost(db.Model, Base):
    __tablename__ = "blog_posts"
    id = db.Column(db.Integer, primary_key=True)

    # Create Foreign Key, "users.id" the users refers to the tablename of User.
    # it gets the id of the author from the User table
    author_id = db.Column(db.Integer, db.ForeignKey("User.id"))
    # Create reference to the User object, the "posts" refers to the posts property in the User class.
    # the author now become a user object and has all the things of a regular user.
    author = relationship("User", back_populates="posts")

    title = db.Column(db.String(250), unique=True, nullable=False)
    subtitle = db.Column(db.String(250), nullable=False, unique=False)
    date = db.Column(db.String(250), nullable=False, unique=False)
    body = db.Column(db.Text, nullable=False, unique=False)
    img_url = db.Column(db.String(250), nullable=False, unique=False)

    # --------- Child Relationship --------#
    comments = relationship("Comment", back_populates="parent_post")


class Comment(db.Model, Base):
    __tablename__ = "comments"
    id = db.Column(db.Integer, primary_key=True, unique=True)
    author_id = db.Column(db.Integer, db.ForeignKey("User.id"))
    comment_author = relationship("User", back_populates="comments")
    # --------- Child Relationship --------#
    blog_id = db.Column(db.Integer, db.ForeignKey("blog_posts.id"))
    parent_post = relationship("BlogPost", back_populates="comments")
    text = db.Column(db.String, nullable=False, unique=False)


# db.create_all()


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


@app.route('/')
def get_all_posts():
    # users = User.query.all()
    # for user in users:
    #     db.session.delete(user)
    #     db.session.commit()
    posts = BlogPost.query.all()
    return render_template("index.html", all_posts=posts, current_user=current_user, display_btn=display_btn)


@app.route('/register', methods=["GET", "POST"])
def register():
    global logged_in

    form = RegisterForm()
    if request.method == "POST":
        if form.validate_on_submit():
            # getting the data sent from the form
            name = request.form["name"]
            email = request.form["email"]
            password = request.form["password"]
            # getting the email inputed email from the db
            check_email = User.query.filter_by(email=email).first()
            # check if user object exists
            if check_email:
                # checking if there is already a user with that email
                if check_email.email == email:
                    flash(
                        "An account with that email has already been used. Try logging instead.", "Error")
                    return redirect(url_for("login"))
            else:
                # creating new user
                new_user = User(
                    email=email,
                    name=name,
                    password=generate_password_hash(password=password, method="pbkdf2:sha3-512", salt_length=10))
                logged_in = True

                # adding the new user to db
                db.session.add(new_user)
                db.session.commit()
                login_user(new_user)

                return redirect(url_for("get_all_posts"))
    return render_template("register.html", form=form)


@app.route('/login', methods=["GET", "POST"])
def login():
    global logged_in, display_btn
    form = LoginForm()

    # validating the form on a post request
    if request.method == "POST" and form.validate_on_submit():
        # getting the form data
        email = request.form["email"]
        password = request.form["password"]
        # check if user exist in db
        user = User.query.filter_by(email=email).first()
        if user:
            display_btn = False
            # check password
            if check_password_hash(user.password, password):
                # loggining the user
                login_user(user)
                logged_in = True
                return redirect(url_for("get_all_posts"))
            else:
                flash("password incorrect!", "Error")
                return redirect(url_for("login"))

        else:
            flash(
                "That email doesn't exist, make sure your are registered first", "Error")
            return redirect(url_for("login"))

    return render_template("login.html", form=form)


@app.route('/logout')
def logout():
    global logged_in
    logout_user()
    logged_in = False
    return redirect(url_for('get_all_posts'))


@app.route("/post/<int:post_id>", methods=["GET", "POST"])
def show_post(post_id):
    requested_post = BlogPost.query.get(post_id)
    commentForm = CommentForm()

    if request.method == "POST":
        if current_user.is_authenticated:
            if commentForm.validate_on_submit():
                # adding the new comment to the database
                new_comment = Comment(
                    text=commentForm.comment.data, comment_author=current_user, parent_post=requested_post)
                db.session.add(new_comment)
                db.session.commit()

        else:
            flash("Login to comment", "Error")
            return redirect(url_for("get_all_posts"))
    all_comments = db.session.query(Comment).all()
    return render_template("post.html", post=requested_post, form=commentForm, comments=all_comments)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/new-post", methods=["GET", "POST"])
def add_new_post():
    form = CreatePostForm()
    if form.validate_on_submit():
        new_post = BlogPost(
            title=form.title.data,
            subtitle=form.subtitle.data,
            body=form.body.data,
            img_url=form.img_url.data,
            author_id=current_user.id,
            date=date.today().strftime("%B %d, %Y")
        )
        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for("get_all_posts"))
    return render_template("make-post.html", form=form)


@app.route("/edit-post/<int:post_id>", methods=["GET", "POST"])
def edit_post(post_id):
    post = BlogPost.query.get(post_id)
    edit_form = CreatePostForm(
        title=post.title,
        subtitle=post.subtitle,
        img_url=post.img_url,
        body=post.body
    )
    if edit_form.validate_on_submit():
        post.title = edit_form.title.data
        post.subtitle = edit_form.subtitle.data
        post.img_url = edit_form.img_url.data
        post.author = post.author
        post.body = edit_form.body.data
        db.session.commit()
        return redirect(url_for("show_post", post_id=post.id))

    return render_template("make-post.html", form=edit_form)


@app.route("/delete/<int:post_id>")
def delete_post(post_id):
    post_to_delete = BlogPost.query.get(post_id)
    db.session.delete(post_to_delete)
    db.session.commit()
    return redirect(url_for('get_all_posts'))


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
