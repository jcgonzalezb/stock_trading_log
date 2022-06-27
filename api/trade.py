# flask packages
from flask import Response, request, jsonify
from flask_restful import Resource
from sqlalchemy.exc import NoResultFound

# project resources
from config import db
from models.trade import Trade
from schemas.trade_schema import TradeSchema
from security.authenticate import token_required #The token verification script

trade_schema = TradeSchema()
trade_schemas = TradeSchema(many=True)


class TradesApi(Resource):
    @token_required
    def get(current_user, request) -> Response:
        """
        GET response method for all trades.
        JSON Web Token is required.
        :return: JSON object
        """
        results = Trade.query.filter_by(user_id=current_user.id).all()
        return jsonify(trade_schemas.dump(results))

    @token_required
    def post(current_user, request) -> Response:
        """
        POST response method for creating trade.
        JSON Web Token is required.
        :return: JSON object
        """
        print("va crear un trade")
        data = request.get_json()
        trade_status = data.get('trade_status', None)
        trade = data.get('trade', None)
        company = data.get('company', None)
        quantity = data.get('quantity', None)
        price = data.get('price', None)
        ticker = data.get('ticker', None)
        trade_date = data.get('trade_date', None)
        new_trade = Trade(user_id=current_user.id, trade_status=trade_status, trade=trade,
                          company=company, ticker=ticker, quantity=quantity,
                          price=price, trade_date=trade_date)
        db.session.add(new_trade)
        db.session.commit()
        return jsonify({'message': 'New trade created!'})


class TradeApi(Resource):
    @token_required
    def get(current_user, request, trade_id: str) -> Response:
        """
        GET response method for single tarde.
        :return: JSON object
        """
        try:
            result = Trade.query.filter_by(id=trade_id).one()
        except NoResultFound:
            return {"message": "User could not be found."}, 400
        return trade_schema.jsonify(result)