from flask import Blueprint

# Define a blueprint for the contact routes
contact_bp = Blueprint('contact', __name__)

# Define the route for the contact page
@contact_bp.route('/contact')
def contact():
    return "Contact Page"