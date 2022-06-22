from json.tool import main
from crypt import methods
from unicodedata import name
from flask import Flask, jsonify, request, make_response
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import NoResultFound
from flask_marshmallow import Marshmallow
from config import app, db
from models.user import User
from models.trade import Trade
from schemas.ma import ma
from schemas.trade_schema import TradeSchema
from schemas.user_schema import UserSchema
from sqlalchemy import exc
import uuid
import json
import datetime
import bcrypt

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
    new_trade = Trade(trade_id=str(uuid.uuid4()), user_id=data['user_id'],
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
    return jsonify({'message': 'The trade has been updated!'})


@app.route('/update_status/<trade_id>', methods=['PUT'])
def update_status(trade_id):
    """ Update a trade """
    trade = Trade.query.filter_by(trade_id=trade_id).first()
    if not trade:
        return jsonify({'message': 'No trade found!'})

    if trade.trade_status == 'enable':
        trade.trade_status = 'disable'
        db.session.commit()
        return jsonify({'message': 'The status has been updated to disable!'})
    elif trade.trade_status == 'disable':
        trade.trade_status = 'enable'
        db.session.commit()
        return jsonify({'message': 'The status has been updated to enable!'})


@app.route('/delete/<trade_id>', methods=['DELETE'])
def delete_trade(trade_id):
    """ Delete a trade """
    trade = Trade.query.filter_by(trade_id=trade_id).first()
    if not trade:
        return jsonify({'message': 'No trade found!'})

    db.session.delete(trade)
    db.session.commit()
    return jsonify({'message': 'trade deleted!'})


@app.route('/delete_trades', methods=['DELETE'])
def delete_all_trades():
    """ Delete all trades """
    results = Trade.query.all()
    if results == []:
        return jsonify({'message': 'The user has no trades!'})

    for _ in results:
        trade = Trade.query.filter_by(trade_id=Trade.trade_id).first()
        db.session.delete(trade)
    db.session.commit()
    return jsonify({'message': 'All trades deleted!'})


@app.route('/new_user', methods=['POST'])
def create_user():
    """ Create a user """

    data = request.get_json()
    user_id = data.get('user_id', '')
    email = data.get('email', '')
    password = data.get('password', '')
    session_id = data.get('session_id', '')
    hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    new_user = User(user_id=user_id, email=email,
                    hashed_password=hashed_password,
                    session_id=session_id)
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'New user created!'})


if __name__ == "__main__":
    app.run(debug=True)
