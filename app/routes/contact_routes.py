from flask import Blueprint, request, jsonify
from app.models.contact import Contact
from app.utils.db import db

# Define a blueprint for the contact routes
contact_bp = Blueprint('contact', __name__)

# Define the route for the contact page
@contact_bp.route('/', methods = ['POST'])
def submit_contact():
    data = request.get_json()

    name = data.get('name')
    email = data.get('email')
    message = data.get('message')

    if not name or not email or not message:
        return jsonify({'error': 'All fields are required'}), 400
    
    new_contact = Contact(name = name, email = email, message = message)
    db.session.add(new_contact)
    db.session.commit()

    return jsonify({'message': 'Contact submitted successfully!'}), 201