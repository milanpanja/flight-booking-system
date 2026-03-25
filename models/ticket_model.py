from models.user_model import db, generate_id
from datetime import datetime

class Ticket(db.Model):
    __tablename__ = "tickets"

    id = db.Column(db.String(32), primary_key=True, default=generate_id)

    user_id = db.Column(db.String(32), db.ForeignKey('users.id'), nullable=False)

    passenger_name = db.Column(db.String(100))
    from_city = db.Column(db.String(100))
    to_city = db.Column(db.String(100))

    departure_time = db.Column(db.String(50))
    arrival_time = db.Column(db.String(50))

    flight_name = db.Column(db.String(100))
    seat_number = db.Column(db.String(20))
    ticket_price = db.Column(db.Float)

    status = db.Column(db.String(20), default="Confirmed")

    created_at = db.Column(db.DateTime, default=datetime.utcnow)