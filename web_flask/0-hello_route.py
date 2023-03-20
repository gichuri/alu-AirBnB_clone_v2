#!/usr/bin/python3

from flask import Flask

#create a new flask web application

app = Flask(__name__)

#define a route for the homepage
@pp.route('/', strict_slashes=False)
def home():
    return "Hello HBNB!"

# start application on port 5000 and port 0.0.0.0
if __name__ == "__main__":
    app.run(debug-True, host='0.0.0.0', port=5000)
