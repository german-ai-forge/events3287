
from flask import Blueprint


home = Blueprint('home', __name__)


@home.route('/')

def index():

    return 'Welcome to the homepage!'


about = Blueprint('about', __name__)


@about.route('/about')

def about():

    return 'This is the about page.'