from flask import Flask
from config import Config
from models.user_model import db, bcrypt
from flask_jwt_extended import JWTManager
from flask import render_template
from app_extensions import Mail

from routes.auth_routes import auth_bp
from routes.flight_routes import flight_bp
from routes.booking_routes import booking_bp
from routes.ticket_routes import ticket_bp
from routes.admin_routes import admin_bp



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
app.register_blueprint(ticket_bp)
app.register_blueprint(admin_bp)


mail = Mail()

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'skybooker58@gmail.com'
app.config['MAIL_PASSWORD'] = 'hybq okrv oyvr uwwh' 
app.config['MAIL_DEFAULT_SENDER'] = 'skybooker58@gmail.com'

mail.init_app(app)

if __name__ == "__main__":
    app.run(debug=True)