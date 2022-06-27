# flask packages
from flask import Response, Blueprint, request, jsonify, abort
from config import db
from models.trade import Trade
from sqlalchemy.exc import NoResultFound

#The token verification script
from security.authenticate import token_required

from schemas.trade_schema import TradeSchema

trade_blueprint = Blueprint('trade_blueprint', __name__, url_prefix='/trade')
trade_schema = TradeSchema()
trade_schemas = TradeSchema(many=True)


@trade_blueprint.route('/new', methods=['POST'], strict_slashes=False)
@token_required
def create_trade(current_user, request) -> Response:
    """
    POST response method for creating trade.
    JSON Web Token is required.
    :return: JSON object
    """
    data = request.get_json()

    trade_status=data.get('trade_status', None)
    trade=data.get('trade', None)
    company=data.get('company', None)
    quantity=data.get('quantity', None)
    price=data.get('price', None)
    ticker=data.get('ticker', None)
    trade_date=data.get('trade_date', None)
    new_trade = Trade(user_id=current_user.id, trade_status=trade_status, trade=trade,
                      company=company, ticker=ticker, quantity=quantity,
                      price=price, trade_date=trade_date)
    db.session.add(new_trade)
    db.session.commit()
    return jsonify({'message': 'New trade created!'})

@trade_blueprint.route('/all', methods=['GET'], strict_slashes=False)
@token_required
def all_trades(current_user, request) -> Response:
    """
    GET response method for all trades.
    JSON Web Token is required.
    :return: JSON object
    """
    results = Trade.query.filter_by(user_id=current_user.id).all()
    return jsonify(trade_schemas.dump(results))

@trade_blueprint.route('/<trade_id>', methods=['GET'], strict_slashes=False)
@token_required
def profile_trade(current_user, request, trade_id: str) -> Response:
    """
    GET response method for single trade.
    :return: JSON object
    """
    try:
        result = Trade.query.filter_by(trade_id=trade_id).one()
    except NoResultFound:
        return {"message": "User could not be found."}, 400
    return trade_schema.jsonify(result)

@trade_blueprint.route('/update_status/<trade_id>', methods=['PATCH'], strict_slashes=False)
@token_required
def update_status(current_user, request, trade_id) -> Response:
    """ Update a trade """
    trade = Trade.query.filter_by(trade_id=trade_id).first()
    if not trade:
        return jsonify({'message': 'No trade found!'})

    if trade.trade_status == 'enable':
        trade.trade_status = 'disable'
        db.session.commit()
        return jsonify({'message': 'The trade has been deleted!'})

