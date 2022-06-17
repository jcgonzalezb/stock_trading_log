from json.tool import main
from crypt import methods
from unicodedata import name
from flask import Flask, jsonify, request, make_response
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import NoResultFound
from flask_marshmallow import Marshmallow
from models.engine.db import app, db
from models.user import Industry
from models.trade import Role
from schemas.ma import ma
from schemas.trade_schema import IndustrySchema
from schemas.user_schema import RoleSchema
from sqlalchemy import exc
import json
import datetime


db.create_all()

# One response
# user_schema = user_schema()
# trade_schema = trade_Schema()

# Many responses
# user_schemas = user_schemas(many=True)
# trade_schemas = trade_Schemas(many=True)


# Testing user access. No token needed
@app.route('/unprotected')
def unprotected():
    return jsonify({'message': 'Anyone can view this!'})


if __name__ == "__main__":
    app.run(debug=True)
