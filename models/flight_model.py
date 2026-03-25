import uuid
from models.user_model import db
def generate_id():
    return uuid.uuid4().hex

class Flight(db.Model):
    __tablename__ = "flights"
    id = db.Column(db.String(32), primary_key=True, default=generate_id)
    source = db.Column(db.String(100))
    destination = db.Column(db.String(100))
    date = db.Column(db.String(50))
    seats = db.Column(db.Integer)
    price = db.Column(db.Float)