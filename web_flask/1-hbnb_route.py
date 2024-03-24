#!/usr/bin/python3
<<<<<<< HEAD
"""Write a script that starts a Flask web application"""
=======
"""script that starts a Flask web application"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """Hello HBNB!"""
    return "Hello HBNB!"
@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """HBNB"""
    return "HBNB"
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
>>>>>>> eedb17c7eb4ffabe5017d9e58adef3dc8b241c3a
