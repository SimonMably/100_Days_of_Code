import sqlite3
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# ------------------------------------------------------------------------------
# db = sqlite3.connect("books-collection.db")
# cursor = db.cursor()

# cursor.execute("CREATE TABLE books (id INTEGER PRIMARY KEY, title varchar(250) NOT NULL UNIQUE, author varchar(250) NOT NULL, rating FLOAT NOT NULL)")

# cursor.execute("INSERT INTO books VALUES(1, 'Harry Potter', 'J. K. Rowling', '9.3')")
# db.commit()
# ------------------------------------------------------------------------------

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///new-books-collection.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Books(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)

    # def __init__(self, title, author, rating):
    #     self.title = title
    #     self.author = author
    #     self.rating = rating

    def __repr__(self):
        return f"<Books {self.title}>"


# db.create_all()

new_book = Books(id=1, title="Harry Potter", author="J.K. Rowling", rating=9.3)
db.session.add(new_book)
db.session.commit()



