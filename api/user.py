# flask packages
from flask import Response, request, jsonify
from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity

from models.user import User
from schemas.user_schema import UserSchema
from api.authenticate import token_required #The token verification script

user_schema = UserSchema()
user_schemas = UserSchema(many=True)


class UserApi(Resource):
    @token_required
    def get(self, user_id: str) -> Response:
        """
        GET response method for acquiring single user data.
        JSON Web Token is required.
        :return: JSON object
        """
        result = User.query.filter(user_id=user_id).one()
        return user_schema.jsonify(result)
