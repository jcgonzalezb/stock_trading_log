# flask packages
from flask import Response, request, jsonify, Blueprint, abort
from config import db
from models.user import User
from schemas.user_schema import UserSchema
from sqlalchemy.exc import NoResultFound

#The token verification script
from security.authenticate import token_required

user_blueprint = Blueprint('user_blueprint', __name__, url_prefix='/user')
user_schema = UserSchema()
user_schemas = UserSchema(many=True)

@user_blueprint.route('/<user_id>', methods=['GET'], strict_slashes=False)
@token_required()
def get_user_profile(current_user, request, user_id: str) -> Response:
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
