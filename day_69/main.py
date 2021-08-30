from flask import Flask, render_template, redirect, url_for, flash, request, \
    abort
from flask_bootstrap import Bootstrap
from flask_ckeditor import CKEditor
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
from flask_login import UserMixin, login_user, LoginManager, login_required, \
    current_user, logout_user
from flask_gravatar import Gravatar
from forms import CreatePostForm, RegisterUserForm, LoginUserForm, CommentForm
from functools import wraps
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
ckeditor = CKEditor(app)
Bootstrap(app)
gravatar = Gravatar(app,
                    size=100,
                    rating='g',
                    default='retro',
                    force_default=False,
                    force_lower=False,
                    use_ssl=False,
                    base_url=None)

# CONNECT TO DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)


# CONFIGURE TABLES

class User(UserMixin, db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100))
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    comments = relationship("Comment", back_populates="author")

    # Acts like a List of BlogPost objects attached to each User.
    # The "author" refers to the author property in the BlogPost class.
    posts = relationship("BlogPost", back_populates="author")


class BlogPost(db.Model):
    __tablename__ = "blog_posts"
    id = db.Column(db.Integer, primary_key=True)

    # ForeignKey, "users.id" users refers to the __tablename__ of User
    author_id = db.Column(db.Integer, db.ForeignKey("users.id"))

    # author = db.Column(db.String(250), nullable=False)
    # author used to be above, now below
    author = relationship("User", back_populates="posts")
    title = db.Column(db.String(250), unique=True, nullable=False)
    subtitle = db.Column(db.String(250), nullable=False)
    date = db.Column(db.String(250), nullable=False)
    body = db.Column(db.Text, nullable=False)
    img_url = db.Column(db.String(250), nullable=False)
    comments = relationship("Comment", back_populates="parent_post")


class Comment(db.Model):
    __tablename__ = "comments"
    id = db.Column(db.Integer, primary_key=True)
    post_id = db.Column(db.Integer, db.ForeignKey("blog_posts.id"))
    author_id = db.Column(db.Integer, db.ForeignKey("users.id"))

    # "author" refers to the comments property in the Users class (the user
    # who made the comment)
    author = relationship("User", back_populates="comments")
    parent_post = relationship("BlogPost", back_populates="comments")
    text = db.Column(db.String(500), nullable=False)
    date = db.Column(db.String(250), nullable=False)


def admin_only(f):
    """
    Decorator that allows only admin level status users to perform certain
    actions.
    """
    @wraps(f)
    def func(*args, **kwargs):
        if not current_user.is_authenticated or current_user.id != 1:
            return abort(403)
        return f(*args, **kwargs)
    return func


@login_manager.user_loader
def load_user(user_id: int):
    """"""
    return User.query.get(int(user_id))


@app.route('/')
def get_all_posts():
    """
    Homepage. Retrieves blog posts and displays 5 post per page via pagination.
    """
    page = request.args.get("page", 1, type=int)
    posts = BlogPost.query.order_by(BlogPost.date.desc()).paginate(page=page,
                                                                   per_page=5)
    return render_template("index.html", all_posts=posts)


@app.route('/register', methods=["GET", "POST"])
def register():
    """Register page. Registers new users."""
    register_form = RegisterUserForm()

    if register_form.validate_on_submit():
        hash_and_salted_password = generate_password_hash(
            password=request.form["password"],
            method="pbkdf2:sha256",
            salt_length=8
        )

        new_user = User()
        new_user.username = request.form["username"]
        new_user.email = request.form["email"]

        # Checks User table in database for existing users via stored emails
        existing_user = User.query.filter_by(email=new_user.email).first()
        if existing_user:
            flash("E-mail address already signed up, login instead")
            return redirect(url_for("login"))

        new_user.password = hash_and_salted_password

        db.session.add(new_user)
        db.session.commit()

        login_user(new_user)
        return redirect(url_for("get_all_posts"))
    return render_template("register.html", form=register_form)


@app.route('/login', methods=["GET", "POST"])
def login():
    """Login Page. Allows existing users to login to blog site."""
    login_form = LoginUserForm()

    if login_form.validate_on_submit():
        user_email = request.form["email"]
        user_password = request.form["password"]

        user = User.query.filter_by(email=user_email).first()

        if not user:
            flash("That email doesn't exist. Please try again.")
            return redirect(url_for("login"))
        elif not check_password_hash(user.password, user_password):
            flash("You entered the wrong password. Please try again.")
            return redirect(url_for("login"))
        else:
            login_user(user)
            print(current_user.username)
            return redirect(url_for("get_all_posts"))
    return render_template("login.html", form=login_form)


@app.route('/logout')
def logout():
    """Logout route allows existing users to logout of blog site."""
    logout_user()
    return redirect(url_for('get_all_posts'))


@app.route("/post/<int:post_id>", methods=["GET", "POST"])
def show_post(post_id: int):
    """
    Post Page/Route. Displays a selected post along with comments for selected
    post. Allows users to submit comments to post. Comments are stored in
    database.
    """
    requested_post = BlogPost.query.get(post_id)
    # IDEA: Paginate comments
    comments = Comment.query.order_by(Comment.date.desc()).all()

    # IDEA: Find a way for users to submit comments as replies to other comments
    comment_form = CommentForm()
    if comment_form.validate_on_submit():
        if not current_user.is_authenticated:
            flash("Please login or register to post comments.")
            return redirect(url_for("login"))

        new_comment = Comment(
            text=comment_form.comment_field.data,
            author=current_user,
            parent_post=requested_post,
            date=datetime.now().strftime("%H:%M%p %d %B, %Y")
        )

        db.session.add(new_comment)
        db.session.commit()

        # Leaves the text field blank after the comment has been submitted
        comment_form.comment_field.data = ""

    return render_template("post.html", post=requested_post, form=comment_form,
                           current_user=current_user)


@app.route("/about")
def about():
    """Displays the About Page."""
    return render_template("about.html", current_user=current_user)


@app.route("/contact")
def contact():
    """Displays contact page."""
    return render_template("contact.html", current_user=current_user)


@app.route("/new-post", methods=["GET", "POST"])
@admin_only
def add_new_post():
    """
    Allows admin level users to create and submit new blog posts. Post is
    stored in database.
    """
    create_post_form = CreatePostForm()

    if create_post_form.validate_on_submit():
        new_post = BlogPost(
            title=create_post_form.title.data,
            subtitle=create_post_form.subtitle.data,
            body=create_post_form.body.data,
            img_url=create_post_form.img_url.data,
            author=current_user,
            date=datetime.now().strftime("%H:%M%p %d %B, %Y")
        )

        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for("get_all_posts"))

    return render_template("make-post.html", form=create_post_form,
                           current_user=current_user)


@app.route("/edit-post/<int:post_id>", methods=["GET", "POST"])
@admin_only
def edit_post(post_id: int):
    """Allows admin level user to edit posts."""
    post = BlogPost.query.get(post_id)
    edit_form = CreatePostForm(
        title=post.title,
        subtitle=post.subtitle,
        img_url=post.img_url,
        author=post.author,
        body=post.body
    )
    if edit_form.validate_on_submit():
        post.title = edit_form.title.data
        post.subtitle = edit_form.subtitle.data
        post.img_url = edit_form.img_url.data
        post.body = edit_form.body.data
        db.session.commit()
        return redirect(url_for("show_post", post_id=post.id))
    return render_template("make-post.html", form=edit_form)


@app.route("/delete-post/<int:post_id>")
@admin_only
def delete_post(post_id: int):
    """Allows admin to delete blog posts and comments from blog and database."""
    # Deletes comments in blog post
    delete_all_comments(post_id)

    # Deletes the blog post itself
    post_to_delete = BlogPost.query.get(post_id)
    db.session.delete(post_to_delete)
    db.session.commit()

    return redirect(url_for("get_all_posts"))


@app.route("/delete-comment/<int:post_id>/<int:comment_id>", methods=["GET",
                                                                      "POST"])
@login_required
def delete_comment(post_id: int, comment_id: int):
    """Allows users to delete there own comments. Admin level user allowed to
    delete all users comments.
    """
    comment_to_delete = Comment.query.get(comment_id)
    db.session.delete(comment_to_delete)
    db.session.commit()
    return redirect(url_for("show_post", post_id=post_id))


@app.route("/delete-comments/<int:post_id>", methods=["GET", "POST"])
@admin_only
def delete_all_comments(post_id: int):
    """
    Deletes all comments. Used in conjunction with delete_post(). Used by admin
    level user.
    """
    comments_to_delete = Comment.query.filter_by(post_id=post_id).all()
    for comment in comments_to_delete:
        db.session.delete(comment)
        db.session.commit()

    return redirect(url_for("get_all_posts", post=post_id))


if __name__ == "__main__":
    if not os.path.isfile("blog.db"):
        db.create_all()
    app.run(debug=True)
