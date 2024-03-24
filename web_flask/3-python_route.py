#!/usr/bin/python3
""" module doc """
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """ def doc """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """ def doc """
    return "HBNB"

@app.route("/c/<text>", strict_slashes=False)
def c(text):
    """ def doc """
    return 'C + {}'.format(text.replace("_", " "))
@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python(text):
    """def doc """
    return 'python + {}'.format(text.replace('_', ' '))


if __name__ == "__main__":
    app.run(debug=True)
