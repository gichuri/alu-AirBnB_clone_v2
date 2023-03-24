#!/usr/bin/python3

"""
write a script that starts a web flask application
fetch states from model.storage and 
renders them to a web_page
""" 

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)

@app.route('/states_list', strict_slashes=False)
def states_list():
    """display a HTML page with state names"""
    return render_template('7-states_list.html', states=storage.all('state').values())

@app.teardown_appcontext
def teardown(self):
    """remove sqlalchemy session"""
    storage.close()

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
