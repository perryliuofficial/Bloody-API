from flask import Blueprint, render_template
api = Blueprint('api', __name__)

@api.route('/<string:input>/')
def hello(input):
    return "Hello " + input, 200