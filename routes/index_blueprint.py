# flask packages
from security.authenticate import token_required
from flask import Blueprint, jsonify, render_template

# project resources
from config import app, db
from models.user import User
from schemas.user_schema import UserSchema

# One response
user_schema = UserSchema()

# Many responses
user_schemas = UserSchema(many=True)

# The token verification script

index_blueprint = Blueprint('index_blueprint', __name__, url_prefix='/')


@app.route('/')
def index():
    """
    Index page. No token needed
    :return: JSON object
    """
    return render_template('welcome.html')


@app.route('/unprotected')
def unprotected():
    """
    Testing user access. No token needed
    :return: JSON object
    """
    return jsonify({'message': 'Anyone can view this!'})


@app.route('/protected')
@token_required
def protected(current_user):
    """
    Testing user access.
    JSON Web Token is required.
    :return: JSON object
    """
    return jsonify({'message':
                    'This section is available for people with valid tokens.'})


@app.route('/all_users', methods=['GET'])
def get_users_info():
    """
    GET response method for acquiring all users data.
    :return: JSON object
    """
    results = User.query.all()
    return render_template('all_users.html',
                           results=user_schemas.dump(results))
