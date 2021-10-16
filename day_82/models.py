from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
import os
from main import db


class Admin(UserMixin, db.Model):
    __tablename__ = "admin"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    project = relationship("Portfolio", back_populates="author")


class Portfolio(db.Model):
    __tablename__ = "portfolio"
    id = db.Column(db.Integer, primary_key=True)
    author_id = db.Column(db.Integer, db.ForeignKey("admin.id"))
    author = relationship("Admin", back_populates="project")
    project_name = db.Column(db.String(100), unique=True)
    project_description = db.Column(db.String(500))
    project_url = db.Column(db.String(300))
    img_url = db.Column(db.String(300))


def create_db():
    """Creates database if it doesn't exists in expected directory."""
    if not os.path.isfile("portfolio.db"):
        db.create_all()
