import uuid
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from datetime import datetime

db = SQLAlchemy()
bcrypt = Bcrypt()
def generate_id():
    return uuid.uuid4().hex 

class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.String(32), primary_key=True, default=generate_id)

    # 👤 Name fields
    first_name = db.Column(db.String(50), nullable=False)
    middle_name = db.Column(db.String(50), nullable=True)
    last_name = db.Column(db.String(50), nullable=False)

    # 📧 Contact
    email = db.Column(db.String(100), unique=True, nullable=False)
    phone = db.Column(db.String(15), unique=True, nullable=True)

    # 🔐 Auth
    password = db.Column(db.String(200), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)

    # 🖼️ Profile Image
    image = db.Column(db.String(255), nullable=True)  # store file path

    # 📅 Metadata
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # 👤 Created By (FIXED)
    created_by = db.Column(db.String(32), db.ForeignKey('users.id'), nullable=True)

    creator = db.relationship('User', remote_side=[id], backref='created_users')

    # 🔐 Password Methods
    def set_password(self, password):
        self.password = bcrypt.generate_password_hash(password).decode('utf-8')

    def check_password(self, password):
        return bcrypt.check_password_hash(self.password, password)

    # 🧾 Full name helper
    def full_name(self):
        return f"{self.first_name} {self.middle_name or ''} {self.last_name}".strip()

    def __repr__(self):
        return f"<User {self.email}>"