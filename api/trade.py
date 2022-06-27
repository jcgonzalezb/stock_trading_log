# flask packages
from flask import Response, request, jsonify
from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity

# project resources
from config import db
from models.trade import Trade
from schemas.trade_schema import TradeSchema

trade_schema = TradeSchema()
trade_schemas = TradeSchema(many=True)


class TradesApi(Resource):
    @jwt_required
    def get(self) -> Response:
        """
        GET response method for all trades.
        JSON Web Token is required.
        :return: JSON object
        """
        results = Trade.query.all()
        return jsonify(trade_schemas.dump(results))

    @jwt_required
    def post(self) -> Response:
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
        user_id = data. get('user_id', None)
        new_trade = Trade(user_id=user_id, trade_status=trade_status, trade=trade,
                        company=company, ticker=ticker, quantity=quantity,
                        price=price, trade_date=trade_date)
        db.session.add(new_trade)
        db.session.commit()
        return jsonify({'message': 'New trade created!'})

class TradeApi(Resource):
    @jwt_required
    def get(self, trade_id: str) -> Response:
        """
        GET response method for single tarde.
        :return: JSON object
        """
        result = Trade.query.filter(trade_id=trade_id).one()
        return trade_schema.jsonify(result)
