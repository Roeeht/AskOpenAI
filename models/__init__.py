from flask_sqlalchemy import SQLAlchemy

# Create the SQLAlchemy object, but don't initialize it with the app yet
db = SQLAlchemy()

def init_db(app):
    """Initialize the database with the Flask app context."""
    db.init_app(app)
    with app.app_context():
        db.create_all()  # Create tables in the database
