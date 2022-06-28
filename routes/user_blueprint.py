# flask packages
from flask import Response, request, jsonify, Blueprint
from config import db
from models.user import User
from schemas.user_schema import UserSchema

#The token verification script
from security.authenticate import token_required
import jwt

user_blueprint = Blueprint('user_blueprint', __name__, url_prefix='/users')
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
    head = request.headers
    token = head['token']
    decoded = jwt.decode(token, options={"verify_signature": False})
    result = User.query.filter_by(id=decoded["id"]).one()
    return user_schema.jsonify(result), 200
