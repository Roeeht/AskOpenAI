from flask import Blueprint

general_bp = Blueprint('general_bp', __name__)

@general_bp.route('/')
def home():
    return "Hello, Flask!"

@general_bp.route('/about')
def about():
    return "This is the about page."
