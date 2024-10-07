from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from models import db


class Qa(db.Model):
    __tablename__ = 'qa'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    question = db.Column(db.String(255), unique=True, nullable=False)
    answer = db.Column(db.Text, nullable=False)  # Use Text for longer answers
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __init__(self, question, answer):
        self.question = question
        self.answer = answer

    def to_dict(self):
        return {
            'id': self.id,
            'question': self.question,
            'answer': self.answer,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat()
        }
