#!/usr/bin/python3
# create a new web application and configure ports

from flask import Flask
app = Flask(__name__)

@pp.route('/', strict_slashes=False)
def home():
    return "Hello HBNB!"

# start application on port 5000
if __name__ == "__main__":
    app.run(debug-True, host='0.0.0.0', port=5000)
