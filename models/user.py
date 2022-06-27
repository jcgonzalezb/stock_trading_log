""" Holds class User"""

from sqlalchemy.dialects.mysql import INTEGER
from config import db
from flask_bcrypt import generate_password_hash, check_password_hash

class User(db.Model):
    """ Representation of user """
    __tablename__ = 'user'

    id = db.Column(INTEGER(unsigned=True), primary_key=True,
                   autoincrement=True, nullable=False)
    email = db.Column(db.String(128), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    session_id = db.Column(db.String(128))

