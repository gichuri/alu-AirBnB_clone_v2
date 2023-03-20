#!/usr/bin/python3

"""
 script that starts a Flask web application:
 Your web application must be listening on 0.0.0.0, port 5000
Routes:
/: display “Hello HBNB!”
/hbnb: display “HBNB”
You must use the option strict_slashes=False in your route definition
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

# define a route for /hbnb

@app.route('/hbnb' strict_slashes=False)
def hbnb():
    """
    Defines a route for /hbnb
    
    Returns: 
        A string with the message "HBNB"
    """
    return "HBNB"

# start the application on port 5000 and host 0.0.0.0
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)

