from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
import random

# See main.py in 'notes' folder to see notes on stuff.

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
        """Turns each database entry (form Cafe database) into a dictionary."""
        dictionary = {}

        for column in self.__table__.columns:
            dictionary[column.name] = getattr(self, column.name)
        return dictionary
        # return {column.name: getattr(self, column.name) for column in self.__table__.columns}


@app.route("/")
def home():
    return render_template("index.html")
    

# HTTP GET - Read Record
@app.route("/random")
def get_random_cafe():
    """"""
    cafes = db.session.query(Cafe).all()
    random_cafe = random.choice(cafes)
    # Simply convert the random_cafe data record to a dictionary of key-value pairs.
    return jsonify(cafe=random_cafe.to_dict())


@app.route("/all")
def all_cafes():
    """"""
    cafes = db.session.query(Cafe).all()
    return jsonify(cafes=[cafe.to_dict() for cafe in cafes])


@app.route("/search")
def search_cafes_by_location():
    """"""
    search_location = request.args.get("location").title()
    matching_cafes = db.session.query(Cafe).filter_by(location=search_location).all()
    if matching_cafes:
        return jsonify(cafes=[cafe.to_dict() for cafe in matching_cafes])
    return jsonify(error={"Cafes Not Found": "There are no cafes in that area. Search again."})


# HTTP POST - Create Record
@app.route("/add", methods=["GET", "POST"])
def add_cafe():
    """"""
    new_cafe = Cafe(
        name=request.form.get("name"),
        map_url=request.form.get("map_url"),
        img_url=request.form.get("img_url"),
        location=request.form.get("location"),
        seats=request.form.get("seats"),
        has_toilet=bool(request.form.get("has_toilets")),
        has_wifi=bool(request.form.get("has_wifi")),
        has_sockets=bool(request.form.get("has_sockets")),
        can_take_calls=bool(request.form.get("can_take_calls")),
        coffee_price=request.form.get("coffee_price"),
    )
    db.session.add(new_cafe)
    db.session.commit()
    return jsonify(response={"success": "Successfully added the new cafe."})


# HTTP PUT/PATCH - Update Record
@app.route("/update-price/<int:cafe_id>", methods=["GET", "PATCH"])
def update_coffee_price(cafe_id):
    """"""
    # TODO: Perhaps expand on this to be able to update other bits of info besides the price
    new_price = request.args.get("new_price")
    cafe = db.session.query(Cafe).get(cafe_id)
    if cafe:
        cafe.coffee_price = new_price
        db.session.commit()
        return jsonify(response={"success": "Successfully updated the price."}), 200
    else:
        return jsonify(response={"Not Found": "The cafe with that ID was not found."}), 400


# HTTP DELETE - Delete Record
@app.route("/report-closed/<int:cafe_id>", methods=["GET", "DELETE"])
def delete_cafe_from_database(cafe_id):
    """"""
    api_key = request.args.get("api_key")
    cafe = db.session.query(Cafe).get(cafe_id)
    if api_key == "TopSecretAPIKey":
        if cafe:
            db.session.delete(cafe)
            db.session.commit()
            return jsonify(response={"Success": "The cafe has been successfully deleted."}), 200
        else:
            return jsonify(error={"Not Found": "That cafe was not found in the database."}), 400
    else:
        return jsonify(error={"Forbidden": "Sorry, that's not allowed. Please use the correct API key."}), 403


if __name__ == '__main__':
    app.run(debug=True)
