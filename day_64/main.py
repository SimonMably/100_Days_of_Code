from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests
import os
from os.path import isfile
from dotenv import load_dotenv
from pprint import pprint

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///movie-list.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)
Bootstrap(app)
load_dotenv()
movie_db_api_key = os.getenv("MOVIE_DB_API")
movie_db_search_url = "https://api.themoviedb.org/3/search/movie/"


class AddMovieForm(FlaskForm):
    movie_title = StringField(label="Movie Title", validators=[DataRequired()])
    submit = SubmitField("Add Movie")


class RateMovieForm(FlaskForm):
    new_rating = StringField(label="Your rating out of 10, e.g. 7.3")
    new_review = StringField(label="Your Review")
    submit = SubmitField("Submit")


class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(500), nullable=True)
    rating = db.Column(db.Float, nullable=True)
    ranking = db.Column(db.Integer, nullable=True)
    review = db.Column(db.String(250), nullable=True)
    img_url = db.Column(db.String(250), nullable=False)

    def __repr__(self):
        return f"<Movie {self.title}>"


if not isfile("movie-list.db"):
    db.create_all()


@app.route("/")
def home():
    """Home page / index.html | Displays films (movie poster along with movie information
    and user rating & review. The information and user review/rating for each movie is stored
    in the SQLite database."""
    all_movies = db.session.query(Movie).order_by(Movie.rating.desc()).all()

    movie_order = 1
    for movie in all_movies:
        movie.ranking = movie_order
        movie_order += 1
    db.session.commit()

    return render_template("index.html", movies=all_movies)


@app.route("/edit", methods=["GET", "POST"])
def edit_review():
    """Edit page / edit.html | User can edit a review and/or rating for a movie that
    already stored in the database."""
    rate_form = RateMovieForm()
    movie_id = request.args.get("id")
    selected_movie = Movie.query.get(movie_id)

    if rate_form.validate_on_submit():
        selected_movie.rating = float(rate_form.new_rating.data)
        selected_movie.review = rate_form.new_review.data
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("edit.html", movie=selected_movie, form=rate_form, id=movie_id)


@app.route("/add", methods=["GET", "POST"])
def add_movie():
    """Add page / add.html | Retrieves information (in the form of JSON) of a user
    inputted film. Returns relevant data for multiple films with inputted movie name
    in the movies title in on-screen list form containing film names/movie release date.
    All are links that user can click to select correct movie."""
    add_form = AddMovieForm()

    if add_form.validate_on_submit():
        searched_movie = add_form.movie_title.data
        params = {
            "api_key": movie_db_api_key,
            "query": searched_movie,
        }

        response = requests.get(movie_db_search_url, params=params)
        data = response.json()["results"]

        return render_template("select.html", options=data)
    return render_template("add.html", form=add_form)


@app.route("/delete")
def delete_movie():
    """Deletes a specified movie entry from the Movie database."""
    movie_id = request.args.get("id")
    movie_to_delete = Movie.query.get(movie_id)
    db.session.delete(movie_to_delete)
    db.session.commit()
    return redirect(url_for("home"))


@app.route("/find")
def find_film():
    """Finds user selected film from select.html and retrieves relevant data
    from The Movie Database via API, then adds film to Movie database. Redirects
    to edit page for user to input review and rating."""
    movie_db_info_url = "https://api.themoviedb.org/3/movie"
    movie_api_id = request.args.get("id")
    if movie_api_id:

        params = {
            "api_key": movie_db_api_key,
            "language": "en-US",
        }

        response = requests.get(f"{movie_db_info_url}/{movie_api_id}", params=params)
        data = response.json()

        new_movie = Movie(
            title=data["title"],
            year=data["release_date"].split("-")[0],
            img_url=f"https://image.tmdb.org/t/p/w500{data['poster_path']}",
            description=data["overview"],
            rating=data["vote_average"],
            review="Great"
        )
        db.session.add(new_movie)
        db.session.commit()

        return redirect(url_for("edit_review", id=new_movie.id))


if __name__ == '__main__':
    app.run(debug=True)
