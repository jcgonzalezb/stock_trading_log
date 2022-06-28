from flask_marshmallow import Marshmallow
from schemas.ma import ma


class UserSchema(ma.Schema):
    class Meta:
        fields = ("id", "email", "password", "name")
