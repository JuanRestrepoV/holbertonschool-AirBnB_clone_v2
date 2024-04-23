#!/usr/bin/python3
"""
2th task file with a Flask app
"""
from flask import Flask
from markupsafe import escape

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """Root route that returns 'Hello HBNB!'

    Returns:
        str: returns 'Hello HBNB!'
    """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Root route that returns 'HBNB!'

    Returns:
        str: returns 'HBNB!'
    """
    return "HBNB"


@app.route(f"/c/<text>", strict_slashes=False)
def cisfun(text):
    """Root route that returns 'C <text>!'

    Returns:
        str: returns 'C <text>'
    """
    return "C {}".format(text.replace("_", " "))


@app.route(f"/python/", defaults={ 'text': 'is_cool' })
@app.route(f"/python/<text>", strict_slashes=False)
def pythoniscool(text):
    """Root route that returns '/python/<text>'

    Returns:
        str: returns '/python/<text>'
    """
    return "Python {}".format(text.replace("_", " "))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
