from flask import render_template, url_for, redirect
import app

@app.app.route('/', methods=['GET','POST'])
def home():
    return render_template('index.html')

@app.app.route('/auth', methods=['GET','POST'])
def auth():
    return render_template('auth.html')