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

    def generate_pw_hash(self):
        self.password = generate_password_hash(password=self.password).decode('utf-8')
    # Use documentation from BCrypt for password hashing
    generate_pw_hash.__doc__ = generate_password_hash.__doc__

    def check_pw_hash(self, password: str) -> bool:
        return check_password_hash(pw_hash=self.password, password=password)
    # Use documentation from BCrypt for password hashing
    check_pw_hash.__doc__ = check_password_hash.__doc__

    def save(self, *args, **kwargs):
        # Overwrite Document save method to generate password hash prior to saving
        if self._created:
            self.generate_pw_hash()
        super(User, self).save(*args, **kwargs)
