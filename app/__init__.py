from flask import Flask
from dotenv import load_dotenv # importing secret keys from .env
import os # using sytem files and folders
from app.utils.db import db  # Import db from util/db.py
from app.routes.contact_routes import contact_bp # Import the contact routes blueprint
from app.routes.project_routes import project_bp # Import the project routes blueprint

# Load environment variables from .env file
load_dotenv()

def create_app():
    # Create Flask app instance
    app = Flask(__name__)

    #Load config from environment variable
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # To avoid warnings

    # Initialize db with the app.
    db.init_app(app)

    # Register the blueprints
    app.register_blueprint(contact_bp, url_prefix='/contact')  # Prefix for contact routes
    app.register_blueprint(project_bp, url_prefix='/projects')  # Prefix for project routes

    return app