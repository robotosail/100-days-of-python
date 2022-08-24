import random
from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)

    def to_dict(self):
        # Method 1.
        dictionary = {}
        # Loop through each column in the data record
        for column in self.__table__.columns:
            # Create a new dictionary entry;
            # where the key is the name of each column in the database
            # and the value is the value in each of the column in the database
            dictionary[column.name] = getattr(self, column.name)
        return dictionary

        # Method 2. Altenatively use Dictionary Comprehension to do the same thing.
        # return {column.name: getattr(self, column.name) for column in self.__table__.columns}


@app.route("/")
def home():
    return render_template("index.html")


# HTTP GET - Read Record

# listening for a fetch or get request
@app.route("/random", methods=["GET"])
def random_cafe():
    # all_cafe = db.session.query(Cafe).all()
    # same as line above
    all_cafe = Cafe.query.all()
    chosen_cafe = random.choice(all_cafe)

    # using jsonify from flask we are
    # returning a json format of the randomly chosen cafe's information
    # return jsonify(id=chosen_cafe.id,
    #                name=chosen_cafe.name,
    #                map_url=chosen_cafe.map_url,
    #                img_url=chosen_cafe.img_url,
    #                location=chosen_cafe.location,
    #                seats=chosen_cafe.seats,
    #                has_toilet=chosen_cafe.has_toilet,
    #                has_wifi=chosen_cafe.has_wifi,
    #                has_sockets=chosen_cafe.has_sockets,
    #                can_take_calls=chosen_cafe.can_take_calls,
    #                coffee_price=chosen_cafe.coffee_price
    #                )

    return jsonify(cafe=chosen_cafe.to_dict())


@app.route("/all", methods=["GET"])
def all():
    # getting all the cafes in the database
    all_cafe = Cafe.query.all()
    # creating a list to hold all the cafes
    cafes = []
    # looping through the list of all the cafes
    for cafe in all_cafe:
        # converting the cafe to a dictionary
        # adding the cafe to the cafes list
        cafes.append(cafe.to_dict())
        # turning the cafes list into a dictionary.
    return jsonify(all_cafe=cafes)


# creating a search route to search a specific location
@app.route("/search", methods=["GET"])
def search():
    info = request.args.get("location")
    all_cafes = Cafe.query.all()
    cafes_in_location = []
    for cafe in all_cafes:
        # check if the cafes location matches the location typed into the address bar
        if cafe.location.lower() == info.lower():
            # add the cafe into the list
            cafes_in_location.append(cafe.to_dict())
            # return the json formato fo the cafe
            return jsonify(cafes=cafes_in_location)
        else:
            return jsonify(error="Sorry we don't have a cafe in that location")


# HTTP POST - Create Record
@app.route("/add", methods=["POST"])
def add():
    new_cafe = Cafe(
        name=request.form.get("name"),
        map_url=request.form.get("map_url"),
        img_url=request.form.get("img_url"),
        location=request.form.get("loc"),
        has_sockets=bool(request.form.get("sockets")),
        has_toilet=bool(request.form.get("toilet")),
        has_wifi=bool(request.form.get("wifi")),
        can_take_calls=bool(request.form.get("calls")),
        seats=request.form.get("seats"),
        coffee_price=request.form.get("coffee_price"),
    )
    db.session.add(new_cafe)
    db.session.commit()
    return jsonify(response={"success": "Successfully added the new cafe."})


# HTTP PUT/PATCH - Update Record
@app.route("/update-price/<cafeid>", methods=["PATCH"])
def update(cafeid):
    # get the id of the cafe using the id passed in
    item_id = db.session.query(Cafe).get(cafeid)
    # check if the id exist
    if id:
        # get the value of the new price
        new_price = request.args.get("new_price")
        # changing the corresponding values
        item_id.coffee_price = new_price
        # commiting the changes
        db.session.commit()
        # returning with a success message
        return jsonify(success=f"Successfully updated the coffee price from the shop {item_id.name}")
    # if the id doesn't exist return the not found error
    else:
        return jsonify(error={"Not Found": "The cafe with that id was not found. Try again"})


# HTTP DELETE - Delete Record
@app.route("/report-closed/<cafeid>", methods=["DELETE"])
def delete(cafeid):
    key = request.args.get("api-key")
    if key == "TOP_SECRET_KEY":
        id = Cafe.query.get(cafeid)
        if id:
            db.session.delete(id)
            db.session.commit()
            return jsonify(success="Successfully deleted")
        else:
            return jsonify(error={"Not found": "Sorry that cafe was not found "})
    else:
        return jsonify(error={"Unauthorized": "You are not authorized"})


if __name__ == '__main__':
    app.run(debug=True)
