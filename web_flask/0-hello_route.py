#!/usr/bin/python3

"""
Flask Web Application

This script creates a Flask web application that listens on 0.0.0.0, port 5000.
defines a route for the homepage; displays the message "Hello HBNB!".

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

# create a new Flask web application
app = Flask(__name__)

# define a route for the homepage


@app.route('/', strict_slashes=False)
def home():
    """
    Displays a message on the homepage.

    Returns:
        A string with the message "Hello HBNB!".
    """
    return "Hello HBNB!"


# start the application on port 5000 and host 0.0.0.0
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
