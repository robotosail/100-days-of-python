from datetime import datetime
from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, URLField, TimeField, SelectField
from wtforms.validators import DataRequired, URL
import csv

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)

year = datetime.now().year
month = datetime.now().month
day = datetime.now().day
d = datetime(year, month, day, hour=8, minute=0, second=0)
msg = "Please fill out this field."


class CafeForm(FlaskForm):
    # input field for cafe name
    Cafe_Name = StringField('Cafe Name', validators=[DataRequired(msg)])
    # input field for cafe location url
    Cafe_Location = URLField('Cafe Location on Google Maps',
                             validators=[DataRequired(msg), URL()])
    # time field for opening an closing time
    Cafe_OpeningTime = TimeField(
        'Opening Time eg. 8am', validators=[DataRequired(msg)], default=d)

    Cafe_ClosingTime = TimeField('Closing Time', validators=[
                                 DataRequired(msg)], default=d)

    # Select Field for picking the ratings
    Cafe_CoffeeRating = SelectField(
        'Coffee Rating', validators=[DataRequired(msg)], choices=["☕️", "☕️☕️", "☕️☕️☕️", "☕️☕️☕️☕️", "☕️☕️☕️☕️☕️"])

    Cafe_WifiRating = SelectField('Wifi Rating', validators=[
        DataRequired(msg)], choices=["select", "💪", "💪💪", "💪💪💪", "💪💪💪💪", "💪💪💪💪💪"])

    Cafe_PowerAvailabilty = SelectField(
        'Power Availability', validators=[DataRequired(msg)], choices=["select", "🔌", "🔌🔌", "🔌🔌🔌", "🔌🔌🔌🔌", "🔌🔌🔌🔌🔌"])

    # submit button
    submit = SubmitField('Submit')

# Exercise:
# add: Location URL, open time, closing time, coffee rating, wifi rating, power outlet rating fields
# make coffee/wifi/power a select element with choice of 0 to 5.
# e.g. You could use emojis ☕️/💪/✘/🔌
# make all fields required except submit
# use a validator to check that the URL field has a URL entered.
# ---------------------------------------------------------------------------


# all Flask routes below
@ app.route("/")
def home():
    return render_template("index.html")


@ app.route('/add', methods=["GET", "POST"])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        # writing the new cafe into the csv file
        with open("cafe-data.csv", mode="a", encoding="utf8") as file:
            file.write(
                f"\n{form.Cafe_Name.data}, {form.Cafe_Location.data}, {form.Cafe_OpeningTime.data}, {form.Cafe_ClosingTime.data}, {form.Cafe_CoffeeRating.data}, {form.Cafe_WifiRating.data}, {form.Cafe_PowerAvailabilty.data}")
    return render_template('add.html', form=form)


@ app.route('/cafes',)
def cafes():
    # getting the cafes info from the csv data
    with open('cafe-data.csv', newline='', encoding="utf-8") as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        # looping through the data and adding it to the list
        for row in csv_data:
            list_of_rows.append(row)
    # sending the list to the html
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)
