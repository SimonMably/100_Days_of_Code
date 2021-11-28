from flask import Flask, render_template, redirect, url_for, flash, request, \
    abort
from flask_bootstrap import Bootstrap
from sqlalchemy.orm import query
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_ckeditor import CKEditor
from flask_login import UserMixin, login_user, LoginManager, login_required, \
    current_user, logout_user
from functools import wraps
from datetime import datetime as dt
import os
from forms import CreateAdminForm, AdminLoginForm, AddProjectForm

app = Flask(__name__)
app.config["SECRET_KEY"] = "SECRET_KEY"
Bootstrap(app)
ckeditor = CKEditor(app)

# app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("DATABASE_URL", "sqlite:///blog.db")
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///portfolio.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# Database
class Admin(UserMixin, db.Model):
    __tablename__ = "admin"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    # projects = relationship("Portfolio", back_populates="project_author")


class Portfolio(db.Model):
    __tablename__ = "portfolio"
    id = db.Column(db.Integer, primary_key=True)
    # author_id = db.Column(db.Integer, db.ForeignKey("admin.id"))
    # project_author = relationship("Admin", back_populates="projects")
    project_name = db.Column(db.String(100), unique=True, nullable=False)
    project_description = db.Column(db.String(500), nullable=False)
    project_url = db.Column(db.String(300), nullable=False)
    img_name = db.Column(db.String(300), nullable=False)
    made_with = db.Column(db.String(300), nullable=False)

    def __repr__(self) -> str:
        return f"{self.project_name}"


login_manager = LoginManager()
login_manager.init_app(app)


@app.context_processor
def inject_now():
    """Allows the placing of the current date in to associated web pages."""
    return {"now": dt.now()}


def admin_only(f):
    """Decorator: Gives user with id of 1 admin status to perform certain
    actions / access certain features."""
    @wraps(f)
    def func(*args, **kwargs):
        if not current_user.is_authenticated or current_user.id != 1:
            return abort(403)
        return f(*args, **kwargs)
    return func


@login_manager.user_loader
def load_user(user_id: int):
    """Uses user_loader decorator from LoginManager(). Loads user, when signing 
    in via the retrieval of users ID from Admin table of database."""
    return Admin.query.get(int(user_id))


@app.route("/")
def homepage():
    """Route responsible for the sites homepage. """
    projects = Portfolio.query.all()
    
    # Used to count amount of users in admin tablr of database, to hide 'Register'
    # button after one person registers as a user/admin
    user_count = db.session.execute("select count(id) as c from admin").scalar()
    
    return render_template("index.html", all_projects=projects, 
                            user_count=user_count)


@app.route("/register-admin", methods=["GET", "POST"])
def register_admin():
    """Creates an Administrative user. Admin is the only intended user of site. 
    This route renders CreateAdminForm(), 1 of 3 forms on the admin page. 
    The username and password inputted into this form will be stored in the 
    Admin table of the portfolio database. Passwords are hashed and salted.
    Link to route will be hidden / taken off from drop-down list of navbar when
    admin user has registered."""
    register_admin_form = CreateAdminForm()
    
    # Stops users from registering as admin/users if 1 admin user already exists.
    user_count = db.session.execute("select count(id) as c from admin").scalar()
    if user_count == 1:
        flash("We're sorry, but you're not applicable to register.")
        return redirect(url_for("homepage"))

    # Registration Form
    if register_admin_form.validate_on_submit():
        hash_and_salted_password = generate_password_hash(
            password=request.form["password"],
            method="pbkdf2:sha256",
            salt_length=8
        )

        create_admin = Admin()
        create_admin.username = request.form["username"]

        # Checks the Admin table in database for existing user via username
        existing_user = Admin.query.filter_by(username=create_admin.username).first()
        if existing_user:
            flash("That username is already the admin. Login instead.")
            return redirect(url_for("login_admin"))
        
        create_admin.password = hash_and_salted_password

        db.session.add(create_admin)
        db.session.commit()

        login_user(create_admin)
        return redirect(url_for("homepage"))
    return render_template("admin.html", form=register_admin_form, title="Register as Admin")


@app.route("/login-admin", methods=["GET", "POST"])
def login_admin():
    """Route allows the admin user to log in to site. Renders AdminLoginForm(), 
    1 of 3 forms on the admin page. ."""
    login_admin_form = AdminLoginForm()

    if login_admin_form.validate_on_submit():
        admin_username = request.form["username"]
        admin_password = request.form["password"]

        # Searches for admin user
        admin = Admin.query.filter_by(username=admin_username).first()

        if not admin:
            flash("That username doesn't exist. Please try again.")
            return redirect(url_for("login_admin"))
        elif not check_password_hash(admin.password, admin_password):
            flash("You entered the wrong password. Please try again.")
            return redirect(url_for("login_admin"))
        else:
            login_user(admin) 
            return redirect(url_for("homepage"))
    return render_template("admin.html", form=login_admin_form, title="Admin Login")


@app.route("/logout")
def logout_admin():
    """"""
    logout_user()
    return redirect(url_for("homepage"))


@app.route("/add-project", methods=["GET", "POST"])
@login_required
@admin_only
def add_project_to_database():
    """Adds new project to Portfolio table of database. Renders AddProjectForm, 
    1 of 3 forms, on to the admin page. """
    add_project_form = AddProjectForm()

    if add_project_form.validate_on_submit():
        new_project = Portfolio(
            project_name=add_project_form.project_name.data,
            project_description=add_project_form.body.data,
            project_url=add_project_form.project_url.data,
            img_name=add_project_form.img_name.data,
            made_with=add_project_form.made_with.data
        )

        db.session.add(new_project)
        db.session.commit()
        return redirect(url_for("add_project_to_database"))
    return render_template("admin.html", form=add_project_form,
                           current_user=current_user, title="Add Project to Database")


@app.route("/delete-project/<int:project_id>")
@admin_only
def delete_project(project_id: int):
    """Deletes project from Portfolio table of database."""
    project_to_delete = Portfolio.query.get(project_id)

    db.session.delete(project_to_delete)
    db.session.commit()

    return redirect(url_for("homepage"))


if __name__ == "__main__":
    # Creates portfolio database if it doesn't exist in expected directory
    if not os.path.isfile("portfolio.db"):
        db.create_all()
    app.run(debug=True)
