import json
from flask import Flask, render_template, redirect, url_for
from flask_cors import CORS

app = Flask(__name__, template_folder='.')
CORS(app)

icons = [False, False]

@app.route('/')
def index():
	return render_template('index.html', icons=icons)

@app.route('/heart/enable')
def enable_heart():
	icons[0] = True
	return redirect(url_for('index')) 

@app.route('/facebook/enable')
def enable_facebook():
	icons[1] = True
	return redirect(url_for('index')) 