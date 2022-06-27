# flask packages
from flask import app, jsonify
from flask_restful import Api
from flask_jwt_extended import JWTManager

# local packages
from config import app, db
from api.routes import create_routes

from models.user import User
from schemas.user_schema import UserSchema
user_schema = UserSchema()
user_schemas = UserSchema(many=True)

# init api and routes
api = Api(app=app)
create_routes(api=api)


# Create the tables that are associated with the models.
db.create_all()

@app.route('/')
def index():
    """ Index page. No token needed """
    return jsonify({'message': 'Welcome to the stock trading log!'})

@app.route('/all_users', methods=['GET'])
def get_users_info():
    """ User information stored in the database """
    results = User.query.all()
    return jsonify(user_schemas.dump(results))


# init jwt manager
jwt = JWTManager(app=app)

if __name__ == '__main__':
    # Main entry point when run in stand-alone mode.
    app.run(debug=True)