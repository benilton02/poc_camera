from controllers.config import MediaServerConfig
from flask import Flask


app = Flask(__name__)

@app.route("/")
def index():
    return 'Media server is up, the devoly trinity was here'

@app.route('/god1')
def god1():
    return "Boni"

@app.route('/god2')
def god2():
    return "Le Afonse"

@app.route('/god3')
def god3():
    return "Devnilton"

