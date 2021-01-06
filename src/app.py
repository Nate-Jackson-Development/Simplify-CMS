import flask
from flask_cors import CORS
from flask import render_template, url_for, redirect

app = flask.Flask(__name__)
CORS(app)
app.config["DEBUG"] = True
app.secret_key = 'super secret key'
app.config['SESSION_TYPE'] = 'filesystem'

@app.route('/', methods=['GET','POST'])
def home():
    return 'Starting Development'