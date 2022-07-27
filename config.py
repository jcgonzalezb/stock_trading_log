#!/usr/bin/env python3
# flask packages
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Create flask app
app = Flask(__name__)

# Connection to the database
uri = 'mysql+pymysql://root:@localhost:3306/stock_log_db'
app.config['SQLALCHEMY_DATABASE_URI'] = uri
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# JWT configuration
app.config['SECRET_KEY'] = "fe620408-4b11-498b-9757-1d47e22b2199"

# Create a database object using the SQLAlchemy class,
# passing the application instance to connect the Flask
# application with SQLAlchemy.
db = SQLAlchemy(app)
