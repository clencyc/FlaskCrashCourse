from flask import Blueprint

# define the blueprint
# Blueprint is a way to organize a group of related views and other code

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return "<h1>Test</h1>"
