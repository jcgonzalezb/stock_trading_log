# flask packages
from flask import jsonify, request
from flask_sqlalchemy import SQLAlchemy

# The token verification script
from security.authenticate import token_required

# local packages
from config import app, db
from models.user import User

from routes.auth_blueprint import auth_blueprint
from routes.user_blueprint import user_blueprint
from routes.trade_blueprint import trade_blueprint

from schemas.trade_schema import TradeSchema
from schemas.user_schema import UserSchema

# One response
user_schema = UserSchema()
trade_schema = TradeSchema()

# Many responses
user_schemas = UserSchema(many=True)
trade_schemas = TradeSchema(many=True)

# Create the tables that are associated with the models.
db.create_all()

app.register_blueprint(auth_blueprint)
app.register_blueprint(user_blueprint)
app.register_blueprint(trade_blueprint)


@app.route('/')
def index():
    """
    Index page. No token needed
    :return: JSON object
    """
    return jsonify({'message': 'Welcome to the stock trading log!'})


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
    return jsonify(user_schemas.dump(results))


if __name__ == '__main__':
    # Main entry point when run in stand-alone mode.
    app.run(debug=True)
