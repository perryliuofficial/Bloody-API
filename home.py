from flask import Blueprint, render_template
home = Blueprint('home', __name__)

@home.route('/', methods=['GET', 'POST'])
@home.route('/index', methods=['GET', 'POST'])
def index():
    return render_template("index.html"), 200