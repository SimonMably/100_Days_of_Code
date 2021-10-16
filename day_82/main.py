from flask import Flask, render_template, redirect, url_for, flash, request, \
    abort
from flask_bootstrap import Bootstrap
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_login import login_user, LoginManager, login_required, current_user,\
    logout_user
from functools import wraps
import os
from datetime import datetime as dt
import models
from forms import CreateAdminForm, AdminLoginForm, AddProjectForm, \
    DeleteProjectForm

app = Flask(__name__)
app.config["SECRET_KEY"] = "SECRET_KEY"
Bootstrap(app)

# app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("DATABASE_URL", "sqlite:///blog.db")
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///portfolio.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)


@app.context_processor
def inject_now():
    """"""
    return {"now": dt.now()}


def admin_only(f):
    """"""
    @wraps(f)
    def func(*args, **kwargs):
        if not current_user.is_authenticated or current_user.id != 1:
            return abort(403)
        return f(*args, **kwargs)
    return func


@login_manager.user_loader
def load_user(user_id: int):
    """"""
    return models.Admin.query.get(int(user_id))


@app.route("/")
def homepage():
    """"""
    return render_template("index.html")


@app.route("/register-admin", methods=["GET", "POST"])
def register_admin():
    """Creates an Administrative user. There will only be 1 admin user."""
    register_admin_form = CreateAdminForm()

    if register_admin_form.validate_on_submit():
        hash_and_salted_password = generate_password_hash(
            password=request.form["password"],
            method="pbkdf2:sha256",
            salt_length=8
        )

        create_admin = models.Admin()
        create_admin.username = request.form["username"]

        # Checks the Admin table in database for existing user via username
        existing_user = models.Admin.query.filter_by(
            username=create_admin.username).first()
        if existing_user:
            flash("That username is already the admin. Login instead.")
            return redirect(url_for("login_admin"))

        create_admin.password = hash_and_salted_password

        db.session.add(create_admin)
        db.session.commit()

        login_user(create_admin)
        return redirect(url_for("homepage"))
    return render_template("admin.html", form=register_admin_form)


@app.route("/login-admin", methods=["GET", "POST"])
def login_admin():
    """"""
    login_admin_form = AdminLoginForm()

    if login_admin_form.validate_on_submit():
        admin_username = request.form["username"]
        admin_password = request.form["password"]

        admin = models.Admin.query.filter_by(username=admin_username).first()

        if not admin:
            flash("That username doesn't exist. Please try again.")
            return redirect(url_for("login_admin"))
        elif not check_password_hash(admin.password, admin_password):
            flash("You entered the wrong password. Please try again.")
            return redirect(url_for("login_admin"))
        else:
            login_user(admin)
            # TODO: Printing for testing purposes. Get rid when all complete.
            print(current_user.username)
            return redirect(url_for("homepage"))
    return render_template("admin.html", form=login_admin_form)


@app.route("/logout")
def logout_admin():
    """"""
    logout_user()
    return redirect(url_for("homepage"))


@app.route("/add-project", methods=["GET", "POST"])
@login_required
@admin_only
def add_project_to_database():
    """"""
    add_project_form = AddProjectForm()

    if add_project_form.validate_on_submit():
        new_project = models.Portfolio(
            project_name=add_project_form.project_name.data,
            project_description=add_project_form.project_description.data,
            project_url=add_project_form.project_url.data,
            img_url=add_project_form.img_url.data
        )

        db.session.add(new_project)
        db.session.commit()
        return redirect(url_for("homepage"))
    return render_template("admin.html", form=add_project_form,
                           current_user=current_user)


@app.route("/delete-project", methods=["GET", "POST"])
@login_required
@admin_only
def delete_project_from_database():
    """"""
    delete_project_form = DeleteProjectForm()

    if delete_project_form.validate_on_submit():
        project_to_delete = models.Portfolio.query.filter_by(
            project_name=delete_project_form.project_name.data).first_or_404(
            description=f"There is no project with the name "
                        f"{delete_project_form.project_name.data}")

        db.session.delete(project_to_delete)
        db.session.commit()


if __name__ == "__main__":
    # Creates portfolio database if it doesn't exist in expected directory
    models.create_db()

    app.run(debug=True)
