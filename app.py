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


@app.route('/update/<trade_id>', methods=['PUT'])
def update_trade(trade_id):
    """ Update a trade """
    trade = Trade.query.filter_by(trade_id=trade_id).first()
    if not trade:
        return jsonify({'message': 'No trade found!'})

    data = request.get_json()
    trade.trade_id = data['trade_id']
    trade.user_id = data['user_id']
    trade.trade_status = data['trade_status']
    trade.trade = data['trade']
    trade.company = data['company']
    trade.ticker = data['ticker']
    trade.quantity = data['quantity']
    trade.price = data['price']
    trade.trade_date = data['trade_date']
    db.session.commit()
    return jsonify({'message' : 'The trade register has been updated!'})


@app.route('/delete/<trade_id>', methods=['DELETE'])
def delete_trade(trade_id):
    """ Delete a trade """
    trade = Trade.query.filter_by(trade_id=trade_id).first()
    if not trade:
        return jsonify({'message': 'No trade found!'})

    db.session.delete(trade)
    db.session.commit()

    return jsonify({'message': 'trade deleted!'})


if __name__ == "__main__":
    app.run(debug=True)
