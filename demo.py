from flask import Flask, jsonify, url_for, request, redirect
from flask_cors import CORS
from collections import OrderedDict
from flask import request
import psycopg2
from threading import Thread, Lock


app= Flask(__name__)
CORS(app)


# This is a route in Flask. Also called an endpoint. It is identical to what Smucker taught is in class. Your "rest API"
# is a collection of endpoints that do different things when you visit them - just like different URLs
@app.route('/',  methods=['GET'])
def hello():
    return "Hello World!"


# The function below is what gets called when you go to the above route. In Flask you return Strings, JSON dictionaries,
# or HTML. Here we're just returning a simple string.
@app.route('/test',  methods=['GET'])
def testing():
    return "This is a test!"


# Here we are returning HTML. This is called "in-line HTML" but we can also return an HTML page held in a different
# directory. Obviously, for larger HTML files, that will be better
@app.route('/demo',  methods=['GET'])
def html_demo():
    return "<html><head><title>Demo</title></head><body>This is our demo HTML file! This is " \
                  "just regular HTML - nothing fancy!</body></html>"