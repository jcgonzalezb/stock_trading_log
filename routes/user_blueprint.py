# flask packages
from flask import Response, request, jsonify, Blueprint, render_template

# project resources
from config import db
from models.user import User
from schemas.user_schema import UserSchema
from validators.errors import forbidden_update_user, empty_data

# The token verification script
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
    token = request.headers['token']
    decoded = jwt.decode(token, options={"verify_signature": False})
    user = User.query.filter_by(id=decoded["id"]).one()
    return render_template('profile.html', user=user)
    #return user_schema.jsonify(user), 200


@user_blueprint.route('/update', methods=['PATCH'], strict_slashes=False)
@token_required
def update_user(current_user) -> Response:
    """
    PATCH response method for updating a single user.
    JSON Web Token is required.
    :return: JSON object
    """
    token = request.headers['token']
    decoded = jwt.decode(token, options={"verify_signature": False})
    user = User.query.filter_by(id=decoded["id"]).one()

    data = request.get_json()
    if len(data) == 0:
        return empty_data()
    if 'id' in data or 'email' in data or 'password' in data:
        return forbidden_update_user()
    if 'name' in data:
        user.name = data.get('name', None)
        db.session.commit()
        return jsonify({'message': 'The user has been updated!'})
