from flask import jsonify
from flask_restful import Resource

from models.trade import Trade
from schemas.ma import ma
from schemas.trade_schema import TradeSchema

trade_schema = TradeSchema()
trade_schemas = TradeSchema(many=True)


class TradeApi(Resource):
    def get(self):
        """ Show all trades """
        results = Trade.query.all()
        return jsonify(trade_schemas.dump(results))
