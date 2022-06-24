from config import db
from models.user import User


class UserNotValidError(ValueError):
    """Parent class of all exceptions raised by this module."""
    pass


class EmailAlreadyAssociatedError(UserNotValidError):
    """Exception raised when a sign-in fails validation because the email is associated to other username in database"""
    pass


class UserAlreadyCreatedError(UserNotValidError):
    """Exception raised when a sign-in fails validation because the email and username exists in database."""
    pass


class NewUser:

    @staticmethod
    def validate_new_user(*args):
        validate = True
        username = args[0]
        email = args[1]
        user = User.query.filter_by(email=email).first()

        if not user:
            return validate

        if user.username == username:
            raise UserAlreadyCreatedError(
                "the email already created access you can log in to.")

        raise EmailAlreadyAssociatedError(
            "the email already exists associated with another username.")
