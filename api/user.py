from flask import jsonify
from flask_restful import Resource

from models.user import User
from schemas.user_schema import UserSchema

user_schema = UserSchema()
user_schemas = UserSchema(many=True)


class UsersApi(Resource):
    def get(self):
        """ Show all trades """
        results = User.query.all()
        return jsonify(user_schemas.dump(results))
