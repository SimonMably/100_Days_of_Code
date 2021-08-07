from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
import requests
import random

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
        # METHOD 1:
        # dictionary = {}
        # # Looping through each column in the dats record
        # for column in self.__table__.columns:
        #     # Create a new dictionary entry;
        #     # where the key is the name of the column
        #     # and the value is the value of the column
        #     dictionary[column.name] = getattr(self, column.name)
        # return dictionary

        # METHOD 2:
        # This return statement does the same as the above for loop and return statement
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}


@app.route("/")
def home():
    return render_template("index.html")
    

# HTTP GET - Read Record
# @app.route("/random")
# def get_random_cafe():
#     """"""
#     random_cafe = random.choice(Cafe.query.all())  # Works
#     # cafes = db.session.query(Cafe).all()
#     # random_cafe = random.choice(cafe)
#
#     return jsonify(cafe={
#         # "id": random_cafe.id,
#         "name": random_cafe.name,
#         "map_url": random_cafe.map_url,
#         "img_url": random_cafe.img_url,
#         "cafe_location": random_cafe.location,
#         "amenities": {
#             "sockets_available": random_cafe.has_sockets,
#             "toilets_available": random_cafe.has_toilet,
#             "wifi": random_cafe.has_wifi,
#             "can_take_calls": random_cafe.can_take_calls,
#             "amount_of_seats": random_cafe.seats,
#             "coffee_price": random_cafe.coffee_price,
#         }
#         }
#     )
# Notes:
# In most cases, might just want to return all the data in particular record and not
# want to write all that code for every route (like the above 'get_random_cafe()'.
# Instead, we can serialise a database row Object to JSON by first converting it to a
# dictionary (see the 'to_dict()' function above) and then using 'jsonify() to
# converting that dictionary to a JSON (in the '/random' route/'get_random_cafe()'
# function below.
@app.route("/random")
def get_random_cafe():
    cafes = db.session.query(Cafe).all()
    random_cafe = random.choice(cafes)
    # Simply convert the random_cafe data record to a dictionary of key-value pairs.
    return jsonify(cafe=random_cafe.to_dict())

# HTTP POST - Create Record

# HTTP PUT/PATCH - Update Record

# HTTP DELETE - Delete Record


if __name__ == '__main__':
    app.run(debug=True)
