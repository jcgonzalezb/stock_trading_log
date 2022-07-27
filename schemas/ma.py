#!/usr/bin/python3
# marshmallow package
from flask_marshmallow import Marshmallow

# local package
from config import app

# Flask-Marshmallow application
ma = Marshmallow(app)
