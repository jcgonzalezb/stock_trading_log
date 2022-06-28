# flask packages
from flask import Response, request, jsonify, Blueprint, abort
from config import db
from models.user import User
from schemas.user_schema import UserSchema
from sqlalchemy.exc import NoResultFound

#The token verification script
from security.authenticate import token_required
import jwt
import requests

user_blueprint = Blueprint('user_blueprint', __name__, url_prefix='/user')
user_schema = UserSchema()
user_schemas = UserSchema(many=True)

@user_blueprint.route('/profile', methods=['GET'], strict_slashes=False)
@token_required
def get_user_profile(current_user) -> Response:
    """
    GET response method for acquiring single user data.
    JSON Web Token is required.
    :return: JSON object
    """
    url = "http://127.0.0.1:5000/user"
    response = requests.get(url)
    token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MSwiZXhwIjoxNjU2Mzg3ODg2fQ.4KzCyUs7IEsMPdlw2CZfbRpjFYEGoA5lFwIC89hiKpw"

    decoded = jwt.decode(token, options={"verify_signature": False}) # works in PyJWT >= v2.0
    print (decoded)
    print (decoded["id"])
    try:
        result = User.query.filter_by(id=decoded["id"]).one()
    except NoResultFound:
        return {"message": "User could not be found."}, 400
    return user_schema.jsonify(result), 200
