from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user

app = Flask(__name__)

# for the session
app.config['SECRET_KEY'] = 'This-my-secret'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
logged_in = False

# LOGIN MANAGER
login_manager = LoginManager(app)


# CREATE TABLE IN DB
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))
# Line below only required once, when creating DB.
# db.create_all()


# this gets all the users in the database and stores it so it can be ready to use
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@app.route('/')
def home():
    # # deletes all the users for testing purposes
    # users = User.query.all()
    # for user in users:
    #     db.session.delete(user)
    #     db.session.commit()
    return render_template("index.html")


@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        password = request.form["password"]

        if User.query.filter_by(email=email).first().email == email:
            flash(
                "An account with that email already exist. Try logging in instead", "Error")
            return redirect(url_for("login"))
        else:
            # hashing the password
            password = generate_password_hash(
                password=password, method="pbkdf2:sha3-512", salt_length=20)
            # adding the newly registered user
            new_user = User(email=email, name=name, password=password)
            db.session.add(new_user)
            db.session.commit()
            return redirect(url_for("secrets"))
    return render_template("register.html")


@app.route('/login', methods=["GET", "POST"])
def login():
    global logged_in
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]
        # getting the user by email.
        user = db.session.query(User).filter_by(email=email).first()
        # check if the user exist
        if user:
            # checking the password is correct
            if check_password_hash(user.password, password):
                # logining in the user
                login_user(user)
                # telling the user they successfully logged in
                flash(message="Successfully logged in", category="Success")
                # redirecting to the secrets page when user logs in
                return redirect(url_for("secrets"))

            else:
                flash(message="Invalid password", category="Error")
        else:
            flash(message="Invalid email", category="Error")
    return render_template("login.html")


@app.route('/secrets')
# making sure the user is logged in order to view the url : by calling the decorator function
@login_required
def secrets():
    print(current_user.name)
    return render_template("secrets.html", name=current_user.name, logged_in=logged_in)


@app.route('/logout')
def logout():
    # logs out the user
    logout_user()
    return redirect(url_for("home"))


@app.route('/download')
@login_required
def download():
    # sending the cheatsheat using send_from_directory.
    return send_from_directory("static/files/", "cheat_sheet.pdf")


if __name__ == "__main__":
    app.run(debug=True)
