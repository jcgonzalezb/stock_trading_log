#!/usr/bin/env python3
# local packages
from config import app, db
from routes.index_blueprint import index_blueprint
from routes.auth_blueprint import auth_blueprint
from routes.user_blueprint import user_blueprint
from routes.trade_blueprint import trade_blueprint


# Create the tables that are associated with the models.
db.create_all()

app.register_blueprint(index_blueprint)
app.register_blueprint(auth_blueprint)
app.register_blueprint(user_blueprint)
app.register_blueprint(trade_blueprint)

if __name__ == '__main__':
    # Main entry point when run in stand-alone mode.
    app.run(debug=True)
