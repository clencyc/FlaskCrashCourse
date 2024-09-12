from flask import Blueprint, render_template

# define the blueprint
# Blueprint is a way to organize a group of related views and other code

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template("home.html")
