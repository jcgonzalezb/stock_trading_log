from unicodedata import name
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# conection to the database
app = Flask(__name__)
uri = 'mysql+pymysql://root:@localhost:3306/stock_log_db'
app.config['SQLALCHEMY_DATABASE_URI'] = uri
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
