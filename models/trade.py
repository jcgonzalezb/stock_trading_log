""" Holds class Trade"""

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.mysql import INTEGER
from config import db


class Trade(db.Model):
    """ Representation of trade """
    __tablename__ = 'trade'

    trade_id = db.Column(INTEGER(unsigned=True), primary_key=True,
                         autoincrement=True, nullable=False)
    user_id = db.Column(INTEGER(unsigned=True), db.ForeignKey(
        'user.id'), nullable=False)
    trade_status = db.Column(db.String(60), nullable=False)
    trade = db.Column(db.String(60), nullable=False)
    company = db.Column(db.String(128), nullable=False)
    ticker = db.Column(db.String(60), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Float)
    trade_date = db.Column(db.DateTime(timezone=True))
