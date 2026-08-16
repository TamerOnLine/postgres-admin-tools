import os

from dotenv import load_dotenv
from flask import Flask
from flask_login import LoginManager
from sqlalchemy import URL

from models.db_postgres.db_config import get_database_credentials
from models.models_definitions import User, db

load_dotenv()

login_manager = LoginManager()
login_manager.login_view = "login"


def create_app():
    """Create and configure the Flask application."""
    app = Flask(__name__)

    secret_key = os.getenv("SECRET_KEY")
    if not secret_key:
        raise RuntimeError("SECRET_KEY must be set in the environment.")

    creds = get_database_credentials()
    app.config["SQLALCHEMY_DATABASE_URI"] = URL.create(
        "postgresql+psycopg2",
        username=creds["user"],
        password=creds["password"],
        host=creds["host"],
        port=int(creds["port"]),
        database=creds["dbname"],
    )
    app.config["SECRET_KEY"] = secret_key
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return db.session.get(User, int(user_id))

    @app.route("/")
    def index():
        return "Flask app is running!"

    return app


if __name__ == "__main__":
    app = create_app()
    with app.app_context():
        db.create_all()
        print("Database tables are ready.")

    debug_enabled = os.getenv("FLASK_DEBUG", "").lower() in {"1", "true", "yes"}
    app.run(debug=debug_enabled)
