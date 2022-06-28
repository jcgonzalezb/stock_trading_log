# local package
from schemas.ma import ma


class TradeSchema(ma.Schema):
    """
    Trade Marshmallow Schema
    Marshmallow schema used for loading/dumping Trades
    """
    class Meta:
        """ Fields to expose """
        fields = ("trade_id", "user_id", "trade_status", "trade", "company",
                  "ticker", "quantity", "price", "trade_date")
