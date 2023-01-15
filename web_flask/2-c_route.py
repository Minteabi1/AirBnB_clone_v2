#!/usr/bin/python3

""" Hello Flask """

from flask import Flask

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/', strict_slashes=False)
def hello():
    """hello Hbnb returns"""
    return 'Hello HBNB!'


@app.route('/hbnb')
def hello_hbnb():
    """hello Hbnb returns"""
    return 'HBNB'


@app.route('/c/<text>')
def clove(text):
    """C is Fun """
    return f'C {text.replace("_"," ")}'


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
