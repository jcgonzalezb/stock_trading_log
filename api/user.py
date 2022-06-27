# flask packages
from flask import Response, request, jsonify
from flask_restful import Resource
from sqlalchemy.exc import NoResultFound

from models.user import User
from schemas.user_schema import UserSchema
from security.authenticate import token_required #The token verification script

user_schema = UserSchema()
user_schemas = UserSchema(many=True)


class UserApi(Resource):
    @token_required
    def get(current_user, request, user_id: str) -> Response:
        """
        GET response method for acquiring single user data.
        JSON Web Token is required.
        :return: JSON object
        """
        try:
            result = User.query.filter_by(id=user_id).one()
        except NoResultFound:
            return {"message": "User could not be found."}, 400
        return user_schema.jsonify(result)
