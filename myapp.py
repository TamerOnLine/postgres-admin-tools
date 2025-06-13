import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from dotenv import load_dotenv
from models.models_definitions import db, User

# Load environment variables from a .env file
load_dotenv()

# Create the Flask application instance
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URL")
app.config['SECRET_KEY'] = os.getenv("SECRET_KEY", 'default_secret_key')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Bind SQLAlchemy to the Flask app
db.init_app(app)

# Initialize Flask-Login
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

def load_user(user_id):
    """
    Callback to reload the user object from the user ID stored in the session.

    Args:
        user_id (int): The ID of the user to load.

    Returns:
        User: An instance of the User model corresponding to the given user ID.
    """
    return User.query.get(int(user_id))

login_manager.user_loader(load_user)

# Create the database tables if they do not exist
with app.app_context():
    db.create_all()
    print("User system is ready.")
