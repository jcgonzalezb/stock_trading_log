""" Holds class User"""

from flask_sqlalchemy import SQLAlchemy
from config import db


class User(db.Model):
    """ Representation of user """
    __tablename__ = 'user'

    user_id = db.Column(db.String(60), primary_key=True, nullable=False)
    user_name = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(128), unique=True, nullable=False)
    hashed_password = db.Column(db.String(128), nullable=False)
    session_id = db.Column(db.String(128), nullable=False)

    def __init__(self, user_id, user_name, email, hashed_password, session_id):
        """ Python class constructor function job is to
        initialize the instance of the class User """
        self.user_id = user_id
        self.user_name = user_name
        self.email = email
        self.hashed_password = hashed_password
        self.session_id = session_id
