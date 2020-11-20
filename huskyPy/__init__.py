"""
The flask application package.
"""

#from flask import Flask
#app = Flask(__name__)

from quart import Quart

app = Quart(__name__)

import huskyPy.views
