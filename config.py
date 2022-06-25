from unicodedata import name
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# conection to the database
app = Flask(__name__)
uri = 'mysql+pymysql://root:@localhost:3306/stock_log_db'
app.config['SQLALCHEMY_DATABASE_URI'] = uri
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = "fe620408-4b11-498b-9757-1d47e22b2199"

db = SQLAlchemy(app)
