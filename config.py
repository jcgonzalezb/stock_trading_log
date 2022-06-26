import datetime
from unicodedata import name
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Connection to the database
app = Flask(__name__)
uri = 'mysql+pymysql://root:@localhost:3306/stock_log_db'
app.config['SQLALCHEMY_DATABASE_URI'] = uri
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# JWT configuration
app.config['SECRET_KEY'] = "fe620408-4b11-498b-9757-1d47e22b2199"
app.config['JWT_AUTH_USERNAME_KEY'] = "email"
app.config['JWT_EXPIRATION_DELTA'] = datetime.timedelta(minutes=20)

# Create a database object using the SQLAlchemy class,
# passing the application instance to connect the Flask
# application with SQLAlchemy.
db = SQLAlchemy(app)
