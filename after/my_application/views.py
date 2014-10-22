from flask import Blueprint

my_application_bp = Blueprint('my_application', __name__)

@my_application_bp.route('/')
def index():
    return '<h1>Hello, world!</h1>'
