""" Holds class User"""

from flask_sqlalchemy import SQLAlchemy
from config import db


class User(db.Model):
    """ Representation of user """
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(128), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    session_id = db.Column(db.String(128))
