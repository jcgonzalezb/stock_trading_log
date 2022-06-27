# flask packages
from flask_restful import Api

# project resources
from api.authentication import SignUpApi, LoginApi
from api.user import UserApi

from api.trade import TradeApi
from api.trade import TradesApi


def create_routes(api):

    api.add_resource(SignUpApi, '/authentication/signup/')
    api.add_resource(LoginApi, '/authentication/login/')

    api.add_resource(UserApi, '/user/<user_id>')

    api.add_resource(TradesApi, '/trade/')
    api.add_resource(TradeApi, '/trade/<trade_id>')
