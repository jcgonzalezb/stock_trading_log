from flask import jsonify
from flask_restful import Resource

from models.trade import Trade

class TradeApi(Resource):
    def get(self):
        output = Trade.query.all()
        print(type(output))
        print(output.to_dict())
        return jsonify({'result': output.to_dict()})