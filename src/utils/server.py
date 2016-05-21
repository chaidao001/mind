from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)


@app.route('/')
def my_form():
    return render_template("index.html")


@app.route('/', methods=['POST'])
def get_market():
    text = request.form['text']
    processed_text = text.upper()
    return processed_text


def run():
    app.run()
