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
    project_description = CKEditorField("Project Description",
                                        validators=[DataRequired()])
    project_url = StringField("Project URL", validators=[DataRequired(), URL()])
    img_url = StringField("Project Image URL",
                          validators=[DataRequired(), URL()])
    submit = SubmitField("Add Project")


class DeleteProjectForm(FlaskForm):
    project_name = StringField("Project Name", validators=[DataRequired()])
    submit = SubmitField("Delete Project")
