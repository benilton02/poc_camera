from flask import Flask


app = Flask(__name__)

@app.route("/")
def index():
    return 'Camera server is up, the devoly trinity was here'

@app.route('/god1')
def god1():
    return "Boni"

@app.route('/god2')
def god2():
    return "Le Afonse"

@app.route('/god3')
def god3():
    return "Devnilton"
