# flask packages
from flask import Response, request, jsonify, Blueprint
from config import db
from models.user import User
from schemas.user_schema import UserSchema
from sqlalchemy.exc import NoResultFound

#The token verification script
from security.authenticate import token_required
import jwt

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
    head = request.headers
    token = head['token']
    decoded = jwt.decode(token, options={"verify_signature": False})
    user = User.query.filter_by(id=decoded["id"]).one()
    return user_schema.jsonify(user), 200

@user_blueprint.route('/update', methods=['PATCH'], strict_slashes=False)
@token_required
def update_user(current_user) -> Response:
    """
    PATCH response method for updating a single user data.
    JSON Web Token is required.
    :return: JSON object
    """
    head = request.headers
    token = head['token']
    decoded = jwt.decode(token, options={"verify_signature": False})
    user = User.query.filter_by(id=decoded["id"]).one()
    
    data = request.get_json()
    if 'name' in data:
        user.name = data.get('name', None)
        db.session.commit()
        return jsonify({'message': 'The user has been updated!'})
