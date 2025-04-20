from datetime import datetime
from app.utils.db import db

class Contact(db.Model):
    __tablename__ = 'contacts'

    id = db.Column(db.Integer, primary_key = True) # Unique ID for each message (PK)
    name = db.Column(db.String(100), nullable = False) # Full name of the person contacting
    email = db.Column(db.String(100), nullable = False) # Email address of the sender
    message = db.Column(db.Text, nullable = False) # The content of the message
    timestamp = db.Column(db.DateTime, default = datetime.utcnow) # Timestamp of when message was sent

    def __repr__(self):
        return f'<Contact {self.name}>'