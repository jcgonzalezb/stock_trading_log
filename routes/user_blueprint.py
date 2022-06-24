from config import db
from models.user import User
from validators.validator import Validator
from validators.password_validator import Password, PasswordNotValidError
from schemas.user_schema import UserSchema
from flask import Blueprint, request, jsonify, abort
import bcrypt

user_blueprint = Blueprint('user_blueprint', __name__, url_prefix='/users')
user_schemas = UserSchema(many=True)

@user_blueprint.route('/', methods=['GET'], strict_slashes=False)
def get_user_profile():
    """ User information stored in the database """
    user_id = request.id
    try:
        user = User.query.filter_by(id=user_id).first()
        return jsonify(user_schemas.dump(user)), 200
    except Exception as e:
        abort(403)
    
@user_blueprint.route('/', methods=['POST'], strict_slashes=False)
def create_user():
    """ Create a user in the database """
    data = request.get_json()
    email = data.get('email', None)
    password = data.get('password', None)
    non_empty = Validator.validate_nonempty(email, password)

    if non_empty:

        try:
            Password.validate_password(password)
        except PasswordNotValidError as e:
            return {'message': f'sorry, {e}'}, 400

        hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
        password = hashed_password.decode()
        new_user = User(email=email, password=password)
        db.session.add(new_user)
        db.session.commit()
        return jsonify({'message': 'New user created!'})

    else:
        return jsonify({'message': 'Some parameters are missing'}), 400
