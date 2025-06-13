from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

db = SQLAlchemy()


class User(db.Model, UserMixin):
    """Database model for users.

    Attributes:
        id (int): Primary key.
        email (str): User's email address.
        username (str): Unique username.
        password_hash (str): Hashed password.
        role (str): Role of the user (e.g., user, admin).
        products (list): List of products associated with the user.
        created_at (datetime): Account creation timestamp.
    """

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.Text, nullable=False)
    role = db.Column(db.String(20), default='user')
    products = db.relationship('Product', backref='merchant', lazy=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def set_password(self, password):
        """Generate and store a password hash.

        Args:
            password (str): The plaintext password to hash.
        """
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        """Verify the provided password against the stored hash.

        Args:
            password (str): The plaintext password to verify.

        Returns:
            bool: True if the password matches, False otherwise.
        """
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        """Return a string representation of the user."""
        return f'<User {self.username}>'





if __name__ == '__main__':
    from flask import Flask
    import os

    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///test.db')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    with app.app_context():
        db.create_all()
        print("✅ Tables created.")


        if not User.query.filter_by(username="admin").first():
            user = User(username="admin", email="admin@example.com", role="admin")
            user.set_password("12345")
            db.session.add(user)
            db.session.commit()
            print("👤 Admin user created.")


