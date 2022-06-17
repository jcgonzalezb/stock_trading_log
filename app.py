from json.tool import main
from crypt import methods
from unicodedata import name
from flask import Flask, jsonify, request, make_response
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import NoResultFound
from flask_marshmallow import Marshmallow
from models.db import app, db
from models.user import User
from models.trade import Trade
from schemas.ma import ma
from schemas.trade_schema import TradeSchema
from schemas.user_schema import UserSchema
from sqlalchemy import exc
import json
import datetime


db.create_all()

# One response
user_schema = UserSchema()
trade_schema = TradeSchema()

# Many responses
user_schemas = UserSchema(many=True)
trade_schemas = TradeSchema(many=True)


# Testing user access. No token needed
@app.route('/unprotected')
def unprotected():
    return jsonify({'message': 'Anyone can view this!'})


if __name__ == "__main__":
    app.run(debug=True)
