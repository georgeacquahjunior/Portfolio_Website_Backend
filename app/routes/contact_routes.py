from flask import Blueprint, request, jsonify
from ..models.contact import Contact
from ..utils.db import db

contact_bp = Blueprint('contact', __name__)

@contact_bp.route('/', methods=['POST'])
def submit_contact():
    data = request.get_json()

    name = data.get('name')
    email = data.get('email')
    message = data.get('message')

    # Basic validation
    if not name or not email or not message:
        return jsonify({'error': 'All fields are required'}), 400

    new_contact = Contact(name=name, email=email, message=message)

    try:
        db.session.add(new_contact)
        db.session.commit()
        return jsonify({'message': 'Contact form submitted successfully'}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500
