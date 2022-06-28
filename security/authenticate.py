# flask packages
from flask import jsonify, request

# project resources
from config import app
from models.user import User

# jwt implementation
import jwt
from functools import wraps

# Decorator for token support


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None

        if 'token' in request.headers:
            token = request.headers['token']

        if not token:
            return jsonify({'message': 'Token is missing!'}), 401

        try:
            data = jwt.decode(
                token, app.config['SECRET_KEY'], algorithms=['HS256', ])
            current_user = User.query.filter_by(
                id=data['id']).first()
        except Exception as e:
            return jsonify({'message': 'Token is invalid!'}), 401

        return f(current_user, *args, **kwargs)

    return decorated
