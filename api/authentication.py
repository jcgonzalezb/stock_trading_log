# flask packages
from flask import Response, request, jsonify, make_response
from flask_restful import Resource

# project resources
from config import db, app
from models.user import User

# external packages
from werkzeug.security import generate_password_hash, check_password_hash
import jwt
import datetime


class SignUpApi(Resource):
    """
    Flask-resftul resource for creating new user.
    :Example:
    >>> from flask import Flask
    >>> from flask_restful import Api
    >>> from app import default_config
    # Create flask app, config, and resftul api, then add SignUpApi route
    >>> app = Flask(__name__)
    >>> app.config.update(default_config)
    >>> api = Api(app=app)
    >>> api.add_resource(SignUpApi, '/authentication/signup')
    """
    @staticmethod
    def post() -> Response:
        """
        POST response method for creating user.
        :return: JSON object
        """
        data = request.get_json()
        email = data.get('email', None)
        password = data.get('password', None)
        hashed_password = generate_password_hash(password, method='sha256')
        new_user = User(email=email, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        return jsonify({'message': 'New user created!'})


class LoginApi(Resource):
    """
    Flask-resftul resource for retrieving user web token.
    :Example:
    >>> from flask import Flask
    >>> from flask_restful import Api
    >>> from app import default_config
    # Create flask app, config, and resftul api, then add LoginApi route
    >>> app = Flask(__name__)
    >>> app.config.update(default_config)
    >>> api = Api(app=app)
    >>> api.add_resource(LoginApi, '/authentication/login')
    """
    @staticmethod
    def post() -> Response:
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
