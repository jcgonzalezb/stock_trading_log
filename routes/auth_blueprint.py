# flask packages
from flask import Blueprint, Response, request, jsonify, make_response
from config import db
from models.user import User
from schemas.user_schema import UserSchema
from sqlalchemy.exc import NoResultFound

# project resources
from config import db, app
from models.user import User

# external packages
from werkzeug.security import generate_password_hash, check_password_hash
import jwt
import datetime


auth_blueprint = Blueprint('auth_blueprint', __name__, url_prefix='/')
user_schema = UserSchema()
user_schemas = UserSchema(many=True)


@auth_blueprint.route('/signup', methods=['POST'], strict_slashes=False)
def register_user() -> Response:
    """
    POST response method for creating user.
    :return: JSON object
    """
    data = request.get_json()
    email = data.get('email', None)
    password = data.get('password', None)
    name = data.get('name', None)
    hashed_password = generate_password_hash(password, method='sha256')
    new_user = User(email=email, password=hashed_password, name=name)
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'New user created!'})

@auth_blueprint.route('/login', methods=['POST'], strict_slashes=False)
def login() -> Response:
    """
    POST response method for retrieving user web token.
    :return: JSON object
    """
    auth = request.authorization

    if not auth or not auth.username or not auth.password:
        return make_response('Could not verify', 401, {'WWW-Authenticate': 'Basic realm="Login required!"'})

    user = User.query.filter_by(email=auth.username).first()

    if not user:
        return make_response('Could not verify', 401, {'WWW-Authenticate': 'Basic realm="Login required!"'})

    if check_password_hash(user.password, auth.password):
        token = jwt.encode({'email': user.email, 'exp': datetime.datetime.utcnow(
        ) + datetime.timedelta(minutes=60)}, app.config['SECRET_KEY'])

        return jsonify({'token': token})

    return make_response('Could not verify', 401, {'WWW-Authenticate': 'Basic realm="Login required!"'})
