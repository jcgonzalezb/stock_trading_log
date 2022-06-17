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

# Create the tables that are associated with the models.
db.create_all()

# One response
user_schema = UserSchema()
trade_schema = TradeSchema()

# Many responses
user_schemas = UserSchema(many=True)
trade_schemas = TradeSchema(many=True)


@app.route('/')
def index():
    """ Index page. No token needed """
    return jsonify({'message': 'Welcome to the stock trading log!'})


@app.route('/unprotected')
def unprotected():
    """ Testing user access. No token needed """
    return jsonify({'message': 'Anyone can view this!'})


@app.route('/all', methods=['GET'])
def get_all_trades():
    """ Show all trades """
    results = Trade.query.all()
    return jsonify(trade_schemas.dump(results))


@app.route('/new_trade', methods=['POST'])
def create_trade():
    """ Create a trade """
    data = request.get_json()
    new_trade = Trade(trade_id=data['trade_id'], user_id=data['user_id'],
                      trade_status=data['trade_status'], trade=data['trade'],
                      company=data['company'], ticker=data['ticker'],
                      quantity=data['quantity'], price=data['price'],
                      trade_date=data['trade_date'])
    db.session.add(new_trade)
    db.session.commit()

    return jsonify({'message': 'New trade created!'})


if __name__ == "__main__":
    app.run(debug=True)
