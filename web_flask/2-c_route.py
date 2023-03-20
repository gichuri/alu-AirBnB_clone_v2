#!/usr/bin/python3
"""
Flask Web Application

This script creates a Flask web application that listens on 0.0.0.0, port 5000.
It defines a single route for the homepage that displays the message "Hello HBNB!".

Usage:
    Run this script to start the Flask application:
        python3 <filename>.py

Routes:
    /:
        Displays the message "Hello HBNB!"

Options:
    - strict_slashes=False:
        Ensures that trailing slashes are ignored in the route URL.

"""

from flask import Flask
app = Flask(__name__)


#define a route for the homepage
@app.route('/', strict_slashes=False)
def home():
    """
    Displays a message on the homepage.

    Returns:
        A string with the message "Hello HBNB!".
    """
    return "Hello HBNB!"
# define route for /hbnb

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    Defines a route for /hbnb
    
    Returns: 
        A string with the message "HBNB"
    """
    return "HBNB"
#define route for c

@app.route('/c/<text>', strict_slashes=False)
def c(text):
    """
    Defines a route for /c

    Returns:
        A string with the message C + value of text
    """
    return "C" + text.replace('_', ' ')

# start the application on port 5000 and host 0.0.0.0
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

