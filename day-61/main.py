from flask import Flask, render_template
# importing bootstrap so it can be used
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
# importing the string field
from wtforms import StringField, PasswordField, SubmitField
# importing the form validator
from wtforms.validators import DataRequired, Email

app = Flask(__name__)
app.secret_key = "Hello"
# passing in the app to the Bootstrap class
Bootstrap(app)


# creating a login class
class Login_Form(FlaskForm):
    # creating the email input field using the email and data requried validators
    email = StringField(label="Email", validators=[DataRequired(
        message="This filed is required"), Email(message="Invalid Email given")])
    # creating a password field using the data required validator
    password = PasswordField(label="Password", validators=[DataRequired(
        message="This field is required")])
    submit = SubmitField(label="login")


# initializing the home or the base route of the site
@app.route("/")
def home():
    return render_template('index.html')


# creating a login route
@app.route("/login", methods=["POST", "GET"])
def login():
    # initialize the form
    form = Login_Form()
    # validating the form when its submitted
    if form.validate_on_submit():
        # getting the data from the email input
        email_data = form.email.data
        # getting the data from the password input
        pwd_data = form.password.data
        # check if the data matches the one specified
        if email_data == "admin@gmail.com" and pwd_data == "12345678":
            # if it does matches then render the success.html on the same route
            return render_template("success.html")
        else:
            return render_template("denied.html")
    # send the form data over to the html
    return render_template("login.html", form=form)


if __name__ == '__main__':
    app.run(debug=True)
