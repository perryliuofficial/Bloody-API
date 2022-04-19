from flask import Flask, render_template, request

from home import home
from api import api

app = Flask(__name__)

app.register_blueprint(home, url_prefix='/home')
app.register_blueprint(api, url_prefix='/contact')

app.run()