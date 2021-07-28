from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from os.path import isfile

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///books-collection.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)


class Books(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f"<Books {self.title}>"
        # return "<Title %r>" % self.id

if not isfile("books-collection.db"):
    db.create_all()


@app.route('/')
def home():
    """Homepage. Displays list of entries from Books Collection database."""
    all_books = db.session.query(Books).all()
    return render_template("index.html", books=all_books)


@app.route("/add", methods=["GET", "POST"])
def add():
    """Adds new book (title & author) along with a rating to Books Collection database."""
    if request.method == "POST":
        new_book_title = request.form["title"]
        new_book_author = request.form["author"]
        new_book_rating = request.form["rating"]

        new_book = Books(title=new_book_title, 
                         author=new_book_author, 
                         rating=new_book_rating)
        
        db.session.add(new_book)
        db.session.commit()

        return redirect(url_for("home"))

    return render_template("add.html")


@app.route("/edit", methods=["GET", "POST"])
def edit():
    """Edits rating for selected book from Books Collection database."""
    if request.method == "POST":
        book_id = request.form["id"]
        book_to_update = Books.query.get(book_id)
        book_to_update.rating = request.form["rating"]
        db.session.commit()
        return redirect(url_for("home"))
    
    book_id = request.args.get("id")
    book_selected = Books.query.get(book_id)
    return render_template("edit.html", book=book_selected)

# My Attempt - it works
# @app.route("/delete/<int:id>")
# def delete(id):
#     book_to_delete = Books.query.get(id)
#     db.session.delete(book_to_delete)
#     db.session.commit()
#     return redirect(url_for("home"))

@app.route("/delete")
def delete():
    book_id = request.args.get("id")

    book_to_delete = Books.query.get(book_id)
    db.session.delete(book_to_delete)
    db.session.commit()
    return redirect(url_for("home"))

 

if __name__ == "__main__":
    app.run(debug=True)
