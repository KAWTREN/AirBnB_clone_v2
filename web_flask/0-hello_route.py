#!/usr/bin/python3
""" module doc """
from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    """ def doc """
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run(debug=True)
