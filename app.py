from flask import Flask
from config import Config
from models.user_model import db, bcrypt
from flask_jwt_extended import JWTManager
from flask import render_template

from routes.auth_routes import auth_bp
from routes.flight_routes import flight_bp
from routes.booking_routes import booking_bp

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
with app.app_context():
    db.create_all()
    print("✅ Database tables created!")
bcrypt.init_app(app)
jwt = JWTManager(app)

app.register_blueprint(auth_bp)
app.register_blueprint(flight_bp)
app.register_blueprint(booking_bp)


if __name__ == "__main__":
    app.run(debug=True)