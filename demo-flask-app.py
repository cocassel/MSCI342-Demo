# Import the flask module.
from flask import Flask
from flask import render_template


# Don't worry about this line. It just initializing the app
app = Flask(__name__)


# This is a route in Flask. Also called an endpoint. It is identical to what Smucker taught is in class. Your "rest API"
# is a collection of endpoints that do different things when you visit them - just like different URLs
@app.route('/')
def hello():
    return "Hello World!"


@app.route('/test')
# The function below is what gets called when you go to the above route. In Flask you return Strings, JSON dictionaries,
# or HTML. Here we're just returning a simple string.
def testing():
    return "This is a test!"

# Here we are returning HTML. This is called "in-line HTML" but we can also return an HTML page held in a different
# directory. Obviously, for larger HTML files, that will be better
@app.route('/demo')
def html_demo():
    return "<html><head><title>Demo</title></head><body>This is our demo HTML file! This is " \
                  "just regular HTML - nothing fancy!</body></html>"
