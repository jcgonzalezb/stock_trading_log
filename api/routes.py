# flask packages
from flask_restful import Api

# project resources
from api.authentication import SignUpApi, LoginApi
from api.user import UsersApi
from api.trade import TradesApi


def create_routes(api):

    api.add_resource(SignUpApi, '/authentication/signup/')
    api.add_resource(LoginApi, '/authentication/login/')

    api.add_resource(UsersApi, '/user/')

    api.add_resource(TradesApi, '/trade/')
    api.add_resource(TradesApi, '/trade/<trade_id>')

