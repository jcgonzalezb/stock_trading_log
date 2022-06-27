from schemas.ma import ma

class TradeSchema(ma.Schema):
    class Meta:
        fields = ("trade_id", "user_id", "trade_status", "trade", "company",
                  "ticker", "quantity", "price", "trade_date")
