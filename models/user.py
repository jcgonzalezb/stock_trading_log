""" Holds class User"""

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.mysql import INTEGER
from config import db


class User(db.Model):
    """ Representation of user """
    __tablename__ = 'user'

    id = db.Column(INTEGER(unsigned=True), primary_key=True,
                   autoincrement=True, nullable=False)
    email = db.Column(db.String(128), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    session_id = db.Column(db.String(128))
