from flask import Flask, render_template, request
import requests
import smtplib
from dotenv import load_dotenv
import os

load_dotenv()
email_address = os.getenv("EMAIL")
password = os.getenv("PASSWORD")

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


@app.route("/contact", methods=["GET", "POST"])
def go_to_contact_page():
    # Receives data from contact form in 'contact.html' page
    if request.method == "GET":
        return render_template("contact.html")
    elif request.method == "POST":
        form_data = request.form
        send_email(form_data["name"], form_data["email"], form_data["phone"], form_data["message"])
        return render_template("contact.html")


# Email: My Code
# def send_message():
#     """Sends message via email from form in contact.html page when the 'SEND' button is clicked."""
#     load_dotenv()
#     email_address = os.getenv("EMAIL")
#     password = os.getenv("PASSWORD")
#
#     form_data = request.form
#     name = form_data["name"]
#     email = form_data["email"]
#     phone = form_data["phone"]
#     message = request.form["message"]
#
#     details = f"Name: {name}\n" \
#               f"Email: {email}\n" \
#               f"Phone Number: {phone}\n" \
#               f"Message: {message}"
#
#     with smtplib.SMTP("smtp.gmail.com") as connection:
#         connection.starttls()
#         connection.login(email_address, password)  # Causing a 'smtplib.SMTPServerDisconnected' exception
#         connection.sendmail(from_addr=email_address, to_addrs=email_address, msg=f"Subject:Blog Contact\n\n{details}")


# Email: Course solution
def send_email(name, email, phone, message):
    email_message = f"Subject:New Message\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage:{message}"
    with smtplib.SMTP("smtp.mail.yahoo.com", timeout=120) as connection:
        connection.starttls()
        connection.login(email_address, password)  # Causing a 'smtplib.SMTPServerDisconnected' exception
        connection.sendmail(email_address, email_address, email_message)


@app.route("/post/<int:post_id>")
def view_post(post_id):
    requested_post = None
    for post in posts:
        if post["id"] == post_id:
            requested_post = post
    return render_template("post.html", post=requested_post)


if __name__ == "__main__":
    app.run(debug=True)

