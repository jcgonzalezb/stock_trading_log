from config import db
from models.user import User
from schemas.user_schema import UserSchema
from flask import Blueprint, request, jsonify
user_schemas = UserSchema(many=True)

user_blueprint = Blueprint('user_blueprint', __name__, url_prefix='/users')


@user_blueprint.route('/', methods=['GET'])
def get_all_user():
    """ Show all users """
    results = User.query.all()
    return jsonify(user_schemas.dump(results))
