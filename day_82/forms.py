from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditorField


class CreateAdminForm(FlaskForm):
    username = StringField("Admin Name", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Register as Admin")


class AdminLoginForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Login")


class AddProjectForm(FlaskForm):
    project_name = StringField("Project Name", validators=[DataRequired()])
    body = CKEditorField("Project Description", validators=[DataRequired()])
    project_url = StringField("Project URL", validators=[DataRequired(), URL()])
    img_name = StringField("Project Image Name", validators=[DataRequired()])
    made_with = StringField("Made With", validators=[DataRequired()])
    submit = SubmitField("Add Project")
