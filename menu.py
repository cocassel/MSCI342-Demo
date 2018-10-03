from flask import Flask, jsonify, url_for, request, redirect
from flask_cors import CORS
from collections import OrderedDict
from flask import request
import psycopg2
from threading import Thread, Lock


app= Flask(__name__)
CORS(app)

@app.route("/demo", methods=['GET'])
def demo():
    return "Hello World!"

