from flask import Flask, render_template
import requests

blog_url = "https://api.npoint.io/88c2c1f644ef334058be"
response = requests.get(blog_url)
posts = response.json()

app = Flask(__name__)


@app.route("/")
@app.route("/index.html")
def get_all_posts():
    return render_template("index.html", all_posts=posts)


@app.route("/about.html")
def go_to_about_page():
    return render_template("about.html")


@app.route("/contact.html")
def go_to_contact_page():
    return render_template("contact.html")


@app.route("/post/<int:post_id>")
def view_post(post_id):
    requested_post = None
    for post in posts:
        if post["id"] == post_id:
            requested_post = post
    return render_template("post.html", post=requested_post)


if __name__ == "__main__":
    app.run(debug=True)
