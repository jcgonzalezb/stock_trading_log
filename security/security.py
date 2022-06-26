import bcrypt
from flask import request

from models.user import User


def authenticate(email, password):
    """
    This function is used to authenticate a user.
    Check the validity of a user's email and password,
    and then tell Flask-JWT to store the user's id inside the JWT.
    """
    user = User.query.filter_by(email=email).first()
    if user and bcrypt.checkpw(password.encode(), user.password.encode()):
        return user


def identity(payload):
    """
    This function takes the payload inside a JWT and
    returns the user's id property.
    """
    user_id = payload['identity']
    setattr(request, 'user_id', user_id)
    return User.query.get(user_id)
