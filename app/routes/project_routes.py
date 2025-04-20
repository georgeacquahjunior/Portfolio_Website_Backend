from flask import Blueprint

# Define a blueprint for the project routes
project_bp = Blueprint('project', __name__)
def projects():
    return "Projects Page"