import os
from flask import Flask
from YourApp import config
from flask_sqlalchemy import SQLAlchemy

# Config load inspired on http://flask.pocoo.org/docs/0.12/config/
app = Flask(__name__)
app.config.from_object(config)
if 'YOURAPPLICATION_SETTINGS' in os.environ:
    app.config.from_envvar('YOURAPPLICATION_SETTINGS')

db = SQLAlchemy(app)

import YourApp.routes

