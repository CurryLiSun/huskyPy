"""
Routes and views for the flask application.
"""
from datetime import datetime
from huskyPy import app
from flask import render_template
from huskyPy.crawl.crawl_web import *
#
import time
from flask import request

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    print(request.data)
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )

@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.'
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )

@app.route('/crawl')
def crawl():
    #cwb_crawl()
    result_obj = cwb_crawl()
    #print(result_obj)

    return "getURL=>" + result_obj
    pass
