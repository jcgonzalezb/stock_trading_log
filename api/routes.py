from api.trade import TradeApi


def create_routes(api):
    api.add_resource(TradeApi, '/trade/')
