from flask_marshmallow import Marshmallow
from schemas.ma import ma


class UserSchema(ma.Schema):
    class Meta:
        fields = ("user_id", "user_name", "email",
                  "hashed_password", "session_id")
