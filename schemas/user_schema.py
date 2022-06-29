# local package
from schemas.ma import ma


class UserSchema(ma.Schema):
    """
    User Marshmallow Schema
    Marshmallow schema used for loading Users
    """
    class Meta:
        """ Fields to expose """
        fields = ("id", "email", "password", "name")
