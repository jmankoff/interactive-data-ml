"""`main` is the top level module for your Flask application."""

# Data Exploration Byte Version 1
# 
# Copyright 1/2016 Jennifer Mankoff
#
# Licensed under GPL v3 (http://www.gnu.org/licenses/gpl.html)
#

# Imports
import os
import jinja2
import webapp2

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

# Import the Flask Framework
from flask import Flask, request
app = Flask(__name__)
    
# Note: We don't need to call run() since our application is embedded within
# the App Engine WSGI application server.

@app.route('/')
def index():
    template = JINJA_ENVIRONMENT.get_template('templates/index.html')
    return template.render()

@app.route('/_update_table', methods=['POST']) 
def update_prediction():
    logging.info(request.get_json())
    features = request.json['features']
    logging.info(cols)
    result = 3#run machine learning here
    logging.info(result)
    return json.dumps({'content' : result})

@app.route('/about')
def about():
    template = JINJA_ENVIRONMENT.get_template('templates/about.html')
    return template.render()

@app.route('/quality')
def quality():
    template = JINJA_ENVIRONMENT.get_template('templates/quality.html')
    return template.render()

@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return 'Sorry, Nothing at this URL.', 404

@app.errorhandler(500)
def application_error(e):
    """Return a custom 500 error."""
    return 'Sorry, unexpected error: {}'.format(e), 500
