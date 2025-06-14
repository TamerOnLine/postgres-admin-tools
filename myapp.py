import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from dotenv import load_dotenv
from models.models_definitions import db, User
from models.db_postgres.db_config import get_database_credentials

# Load environment variables from .env file
load_dotenv()

# Initialize Flask-Login
login_manager = LoginManager()
login_manager.login_view = 'login'

def create_app():
    """
    Factory function to create and configure the Flask application.

    Returns:
        Flask: A configured Flask application instance.
    """
    app = Flask(__name__)

    # Get DB credentials from either DATABASE_URL or DB_* vars
    creds = get_database_credentials()
    database_uri = (
        f"postgresql://{creds['user']}:{creds['password']}@{creds['host']}:{creds['port']}/{creds['dbname']}"
    )
    app.config['SQLALCHEMY_DATABASE_URI'] = database_uri
    app.config['SECRET_KEY'] = os.getenv("SECRET_KEY", 'default_secret_key')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Bind extensions to the application
    db.init_app(app)
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        """
        Load a user by ID.

        Args:
            user_id (int): The ID of the user to retrieve.

        Returns:
            User: The user instance if found, otherwise None.
        """
        return User.query.get(int(user_id))

    @app.route("/")
    def index():
        """
        Simple welcome page route.

        Returns:
            str: A welcome message.
        """
        return "Flask app is running!"

    return app

if __name__ == "__main__":
    app = create_app()
    with app.app_context():
        db.create_all()
        print("User system is ready.")
    app.run(debug=True)