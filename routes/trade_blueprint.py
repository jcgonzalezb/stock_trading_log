from config import db
from models.trade import Trade
from validators.validator import Validator

from schemas.trade_schema import TradeSchema
from flask import Blueprint, request, jsonify, abort


trade_blueprint = Blueprint('trade_blueprint', __name__, url_prefix='/trades')
trade_schema = TradeSchema()
trade_schemas = TradeSchema(many=True)


@trade_blueprint.route('/new_trade', methods=['POST'], strict_slashes=False)
def create_trade():
    """ Create a trade """
    data = request.get_json()

    trade_status=data.get('trade_status', None)
    trade=data.get('trade', None)
    company=data.get('company', None)
    quantity=data.get('quantity', None)
    price=data.get('price', None)
    ticker=data.get('ticker', None)
    trade_date=data.get('trade_date', None)
    user_id = data. get('user_id', None)

    new_trade = Trade(user_id=user_id, trade_status=trade_status, trade=trade,
                      company=company, ticker=ticker, quantity=quantity,
                      price=price, trade_date=trade_date)
    db.session.add(new_trade)
    db.session.commit()
    return jsonify({'message': 'New trade created!'})

@trade_blueprint.route('/update_status/<trade_id>', methods=['PATCH'], strict_slashes=False)
def update_status(trade_id):
    """ Update a trade """
    trade = Trade.query.filter_by(trade_id=trade_id).first()
    if not trade:
        return jsonify({'message': 'No trade found!'})

    if trade.trade_status == 'enable':
        trade.trade_status = 'disable'
        db.session.commit()
        return jsonify({'message': 'The trade has been deleted!'})
