from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user
import os

app = Flask(__name__)

app.config['SECRET_KEY'] = 'Flask_Secret_Key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)


# CREATE TABLE IN DB
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))


@login_manager.user_loader
def load_user(user_id):
    """"""
    return User.query.get(int(user_id))


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/register', methods=["GET", "POST"])
def register():
    """"""
    if request.method == "POST":

        # hash_and_salted_password = generate_password_hash(
        #     password=request.form.get("password"),
        #     method="pbkdf2:sha256",
        #     salt_length=8
        # )

        new_user = User()
        new_user.name = request.form["name"].title()
        new_user.email = request.form["email"]
        new_user.password = generate_password_hash(password=request.form["password"],
                                                   method="pbkdf2:sha256",
                                                   salt_length=8)

        db.session.add(new_user)
        db.session.commit()

        login_user(new_user)

        return render_template("secrets.html", user=new_user)
    return render_template("register.html")


@app.route('/login', methods=["GET", "POST"])
def login():
    """"""

    if request.method == "POST":
        user_email = request.form.get("email")
        user_password = request.form.get("password")

        user = User.query.filter_by(email=user_email).first()

        if not user:
            flash("That email doesn't exist. Please try again.")
            return redirect(url_for("login"))
        elif not check_password_hash(user.password, user_password):
            flash("Password incorrect. Please try again.")
            return redirect(url_for("login"))
        else:
            login_user(user)
            return redirect(url_for("secrets"))



        # if user_password != matched_password:
        #     error = "Invalid Password."
        # else:
        #     flash("You were successfully logged in.")
        #     return redirect(url_for("secrets"))

    return render_template("login.html")


@app.route('/secrets')
@login_required
def secrets():
    """"""
    print(current_user.name)
    return render_template("secrets.html")


@app.route('/logout')
def logout():
    """"""
    logout_user()
    return redirect(url_for("home"))


@app.route("/download")
@login_required
def download():
    """"""
    return send_from_directory(directory=app.static_folder, path="files/cheat_sheet.pdf")


@app.route("/delete/<int:user_id>")
def delete(user_id):
    """"""
    user_to_delete = User.query.get(user_id)
    db.session.delete(user_to_delete)
    db.session.commit()
    return redirect(url_for("home"))


if __name__ == "__main__":
    if not os.path.isfile("users.db"):
        db.create_all()
    app.run(debug=True)
