from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Connection to the database
app = Flask(__name__)

uri = 'mysql+pymysql://root:@localhost:3306/stock_log_db'
app.config['SQLALCHEMY_DATABASE_URI'] = uri
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Create a database object using the SQLAlchemy class,
# passing the application instance to connect the Flask
# application with SQLAlchemy.
db = SQLAlchemy(app)
