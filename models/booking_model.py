import uuid
from models.user_model import db
def generate_id():
    return uuid.uuid4().hex

class Booking(db.Model):
    __tablename__ = "bookings"
    id = db.Column(db.String(32), primary_key=True, default=generate_id)
    user_id = db.Column(db.String(32), db.ForeignKey('users.id'))
    
    # ✅ FIX HERE (must match "flights.id")
    flight_id = db.Column(db.String(32), db.ForeignKey('flights.id'))
    seats_booked = db.Column(db.Integer)