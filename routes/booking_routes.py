from flask import Blueprint, request, jsonify
from models.booking_model import Booking, db
from flask_jwt_extended import jwt_required, get_jwt_identity


booking_bp = Blueprint('booking', __name__)

@booking_bp.route('/book', methods=['POST'])
@jwt_required()
def book_flight():
    user_id = get_jwt_identity()
    data = request.json

    booking = Booking(
        user_id=user_id,
        flight_id=data['flight_id'],
        seats_booked=data['seats']
    )

    db.session.add(booking)
    db.session.commit()

    return jsonify({"msg": "Flight booked"})

@booking_bp.route('/my-bookings', methods=['GET'])
@jwt_required()
def my_bookings():
    user_id = get_jwt_identity()
    bookings = Booking.query.filter_by(user_id=user_id).all()

    return jsonify([b.id for b in bookings])

