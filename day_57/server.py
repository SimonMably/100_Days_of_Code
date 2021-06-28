import random
import datetime
import requests
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    random_number = random.randint(1, 10)
    now = datetime.datetime.now()
    current_year = now.strftime("%Y")
    # current_year = datetime.datetime.now().year()
    return render_template("index.html", num=random_number, year=current_year)


@app.route("/guess/<name>")
def guess(name):
    agify_response = requests.get(f"https://api.agify.io/?name={name}")
    age = agify_response.json()["age"]

    genderize_response = requests.get(f"https://api.genderize.io/?name={name}")
    gender = genderize_response.json()["gender"]

    return render_template("guess.html", name=name.title(), age=age, gender=gender)


@app.route("/blog/<num>")
def get_blog(num):
    print(num)  # To prove that this works
    blog_url = "https://api.npoint.io/ed99320662742443cc5b"
    response = requests.get(blog_url)
    all_posts = response.json()
    return render_template("blog.html", posts=all_posts)


if __name__ == "__main__":
    app.run(debug=True)
