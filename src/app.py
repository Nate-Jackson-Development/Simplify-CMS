import flask
from flask_cors import CORS
from flask import render_template, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = flask.Flask(__name__)
CORS(app)
app.config["DEBUG"] = True

# SQL Database
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://user:pass@localhost/simplify"

# MD5 hash for fjklshljkfhe;sfhj;ekljsjfslkejflks;e
app.secret_key = '5da99b2d8fd14f004297c08a6feabb4f'
app.config['SESSION_TYPE'] = 'filesystem'
db = SQLAlchemy(app)

import routes, models