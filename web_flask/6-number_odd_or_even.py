#!/usr/bin/python3
"""
Module doc
"""

from flask import Flask render_template

app = Flask(__name__)
@app.route('/')
def hello():
    return "hello"
