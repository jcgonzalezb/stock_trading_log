from json.tool import main
from crypt import methods
from unicodedata import name
from flask import Flask, jsonify, request
from routes.user_blueprint import user_blueprint
from routes.trade_blueprint import trade_blueprint
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import NoResultFound
from flask_marshmallow import Marshmallow
from config import app, db
from models.user import User
from models.trade import Trade
from schemas.ma import ma
from schemas.trade_schema import TradeSchema
from schemas.user_schema import UserSchema



# Create the tables that are associated with the models.
db.create_all()

# One response
user_schema = UserSchema()
trade_schema = TradeSchema()

# Many responses
user_schemas = UserSchema(many=True)
trade_schemas = TradeSchema(many=True)

app.register_blueprint(user_blueprint)
app.register_blueprint(trade_blueprint)

@app.route('/')
def index():
    """ Index page. No token needed """
    return jsonify({'message': 'Welcome to the stock trading log!'})

@app.route('/all_users', methods=['GET'])
def get_users_info():
    """ User information stored in the database """
    results = User.query.all()
    return jsonify(user_schemas.dump(results))

@app.route('/unprotected')
def unprotected():
    """ Testing user access. No token needed """
    return jsonify({'message': 'Anyone can view this!'})


@app.route('/all', methods=['GET'])
def get_all_trades():
    """ Show all trades """
    results = Trade.query.all()
    return jsonify(trade_schemas.dump(results))

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

if __name__ == "__main__":
    app.run(debug=True)
