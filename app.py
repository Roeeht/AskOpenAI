from flask import Flask
from config import Config
from models.user_model import db
from routes.user_routes import user_bp
from routes.general_routes import general_bp

app = Flask(__name__)

#Load configurations
app.config.from_object(Config)

# Initialize the database with the app
db.init_app(app)

# Create the database
with app.app_context():
    db.create_all()

# Register blueprints (for routes)
app.register_blueprint(user_bp)
app.register_blueprint(general_bp)

if __name__ == '__main__':
    app.run(debug=True)
