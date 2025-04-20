from datetime import datetime
from app.utils.db import db

class Project(db.model):
    __tablename__ = 'projects'

    id = db.Column(db.Integer, primary_key = True) # Unique ID for each project (PK)
    title = db.Column(db.String(150), nullable = False) # Name or title of the project
    description = db.Column(db.Text, nullable = False) # Short description of the project
    link = db.Column(db.String(255)) # Optional project link
    created_at = db.Column(db.DateTime, default = datetime.utcnow)

    def __repr__(self):
        return f'<Project {self.title}>'