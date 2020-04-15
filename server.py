import json
from flask import Flask, render_template
from flask_cors import CORS

app = Flask(__name__, template_folder='.')
CORS(app)

icons = {"icons": [False, False]}

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/icons')
def get_icons():
	return json.dumps(icons)

@app.route('/heart/enable')
def enable_heart():
	icons["icons"][0] = True
	return json.dumps(icons) 

@app.route('/facebook/enable')
def enable_facebook():
	icons["icons"][1] = True
	return json.dumps(icons) 