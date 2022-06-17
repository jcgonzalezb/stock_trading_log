""" Holds class Trade"""

from flask_sqlalchemy import SQLAlchemy
from models.db import db


class Trade(db.Model):
    """ Representation of trade """
    __tablename__ = 'trade'

    trade_id = db.Column(db.String(60), primary_key=True)
    user_id = db.Column(db.String(60), db.ForeignKey('user.user_id'))
    trade_status = db.Column(db.String(60))
    trade = db.Column(db.String(60))
    company = db.Column(db.String(128))
    ticker = db.Column(db.String(60))
    number_employees = db.Column(db.Integer)
    price = db.Column(db.Float)
    trade_date = db.Column(db.DateTime)

    def __init__(self, trade_id, user_id, trade_status, trade, company,
                 ticker, number_employees, price, trade_date):

        self.trade_id = trade_id
        self.user_id = user_id
        self.trade_status = trade_status
        self.trade = trade
        self.company = company
        self.ticker = ticker
        self.number_employees = number_employees
        self.price = price
        self.trade_date = trade_date
