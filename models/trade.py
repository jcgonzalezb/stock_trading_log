""" Holds class Trade"""

from flask_sqlalchemy import SQLAlchemy
from models.db import db


class Trade(db.Model):
    """ Representation of trade """
    __tablename__ = 'trade'

    trade_id = db.Column(db.String(60), primary_key=True, nullable=False)
    user_id = db.Column(db.String(60), db.ForeignKey('user.user_id'),
                        nullable=False)
    trade_status = db.Column(db.String(60), nullable=False)
    trade = db.Column(db.String(60), nullable=False)
    company = db.Column(db.String(128), nullable=False)
    ticker = db.Column(db.String(60), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Float)
    trade_date = db.Column(db.DateTime(timezone=True))

    def __init__(self, trade_id, user_id, trade_status, trade, company,
                 ticker, quantity, price, trade_date):
        """ Python class constructor function job is to
        initialize the instance of the class Trade """
        self.trade_id = trade_id
        self.user_id = user_id
        self.trade_status = trade_status
        self.trade = trade
        self.company = company
        self.ticker = ticker
        self.quantity = quantity
        self.price = price
        self.trade_date = trade_date
