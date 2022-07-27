#!/usr/bin/env python3
# flask packages
from flask import Response, Blueprint, request, jsonify, render_template
from sqlalchemy.exc import NoResultFound

# project resources
from config import db
from models.trade import Trade
from models.user import User
from schemas.trade_schema import TradeSchema
from validators.errors import trade_not_found, forbidden, empty_data
from validators.errors import forbidden_status, forbidden_new_trade
from validators.errors import forbidden_trade

# The token verification script
from security.authenticate import token_required
import jwt

trade_blueprint = Blueprint('trade_blueprint', __name__, url_prefix='/trades')
trade_schema = TradeSchema()
trade_schemas = TradeSchema(many=True)


@trade_blueprint.route('/new', methods=['POST'], strict_slashes=False)
@token_required
def create_trade(current_user) -> Response:
    """
    POST response method for creating trade.
    JSON Web Token is required.
    :return: JSON object
    """
    data = request.get_json()
    if len(data) == 0:
        return empty_data()
    if 'trade_id' in data or 'user_id' in data:
        return forbidden_new_trade()

    trade_status = data.get('trade_status', 'enable')
    trade = data.get('trade', None)
    company = data.get('company', None)
    ticker = data.get('ticker', None)
    quantity = data.get('quantity', None)
    price = data.get('price', None)
    trade_date = data.get('trade_date', None)
    new_trade = Trade(user_id=current_user.id, trade_status=trade_status,
                      trade=trade, company=company, ticker=ticker,
                      quantity=quantity, price=price, trade_date=trade_date)
    db.session.add(new_trade)
    db.session.commit()
    return jsonify({'message': 'New trade created!'})


@trade_blueprint.route('/all', methods=['GET'], strict_slashes=False)
@token_required
def all_trades(current_user) -> Response:
    """
    GET response method for all trades.
    JSON Web Token is required.
    :return: JSON object
    """
    trades = Trade.query.filter_by(user_id=current_user.id).all()
    return render_template('all_trades.html',
                           trades=trade_schemas.dump(trades))


@trade_blueprint.route('/<trade_id>', methods=['GET'], strict_slashes=False)
@token_required
def profile_trade(current_user, trade_id: str) -> Response:
    """
    GET response method for single trade.
    JSON Web Token is required.
    :return: JSON object
    """
    token = request.headers['token']
    decoded = jwt.decode(token, options={"verify_signature": False})
    user = User.query.filter_by(id=decoded["id"]).one()
    try:
        trade = Trade.query.filter_by(trade_id=trade_id).one()
        if user.id != trade.user_id:
            return forbidden_trade()
    except NoResultFound:
        return trade_not_found()
    return render_template('trade_profile.html', trade=trade)


@trade_blueprint.route('/update_status/<trade_id>',
                       methods=['PATCH'], strict_slashes=False)
@token_required
def update_status(current_user, trade_id) -> Response:
    """
    PATCH response method for updating the status of single trade.
    PATCH is used instead of DELETE to make the trade unavailable.
    JSON Web Token is required.
    :return: JSON object
    """
    try:
        token = request.headers['token']
        decoded = jwt.decode(token, options={"verify_signature": False})
        user = User.query.filter_by(id=decoded["id"]).one()
        trade = Trade.query.filter_by(trade_id=trade_id).one()
        if user.id != trade.user_id:
            return forbidden_trade()
        if trade.trade_status == 'disable':
            return forbidden_status()
        if trade.trade_status == 'enable':
            trade.trade_status = 'disable'
            db.session.commit()
            return jsonify({'message': 'The trade has been deleted!'})
    except NoResultFound:
        return trade_not_found()


@trade_blueprint.route('/<trade_id>', methods=['PATCH'], strict_slashes=False)
@token_required
def update_trade(current_user, trade_id: str) -> Response:
    """
    PATCH response method for updating a single trade.
    JSON Web Token is required.
    :return: JSON object
    """
    data = request.get_json()
    if len(data) == 0:
        return empty_data()
    try:
        token = request.headers['token']
        decoded = jwt.decode(token, options={"verify_signature": False})
        user = User.query.filter_by(id=decoded["id"]).one()
        trade = Trade.query.filter_by(trade_id=trade_id).one()
        if user.id != trade.user_id:
            return forbidden_trade()
        if trade.trade_status == 'disable':
            return forbidden_status()
        if 'trade_id' in data or 'user_id' in data or 'trade_status' in data:
            return forbidden()
        if 'trade' in data:
            trade.trade = data.get('trade', None)
        if 'company' in data:
            trade.company = data.get('company', None)
        if 'ticker' in data:
            trade.ticker = data.get('ticker', None)
        if 'quantity' in data:
            trade.quantity = data.get('quantity', None)
        if 'price' in data:
            trade.price = data.get('price', None)
        if 'trade_date' in data:
            trade.trade_date = data.get('trade_date', None)
        db.session.commit()
    except NoResultFound:
        return trade_not_found()
    return jsonify({'message': 'The trade has been updated!'})
