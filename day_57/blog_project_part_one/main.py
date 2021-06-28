from flask import Flask, render_template
import requests


app = Flask(__name__)


@app.route("/")
def home():
    blog_url = "https://api.npoint.io/ed99320662742443cc5b"
    response = requests.get(blog_url)
    all_posts = response.json()
    return render_template("index.html", posts=all_posts)


#
@app.route("/post/<int:post_id>")
def get_post(post_id):
    blog_url = "https://api.npoint.io/ed99320662742443cc5b"
    response = requests.get(blog_url)
    all_posts = response.json()
    return render_template("post.html", posts=all_posts, post_id=post_id)


if __name__ == "__main__":
    app.run(debug=True)
