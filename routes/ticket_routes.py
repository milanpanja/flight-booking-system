from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from models.ticket_model import db, Ticket
from models.user_model import User
from utils.email_service import send_email

ticket_bp = Blueprint('ticket', __name__)

@ticket_bp.route('/book-ticket', methods=['POST'])
@jwt_required()
def book_ticket():
    user_id = get_jwt_identity()
    data = request.json

    ticket = Ticket(
        user_id=user_id,
        passenger_name=data['passenger_name'],
        from_city=data['from_city'],
        to_city=data['to_city'],
        departure_time=data['departure_time'],
        arrival_time=data['arrival_time'],
        flight_name=data['flight_name'],
        seat_number=data['seat_number'],
        ticket_price=data['ticket_price']
    )

    db.session.add(ticket)
    db.session.commit()   # ✅ MUST commit first

    # ✅ GET USER DETAILS
    user = User.query.get(user_id)

    # ✅ SEND EMAIL
    send_email(
        user.email,
        "Flight Ticket Confirmation ✈️",
        f"""
Hello {user.full_name()},

Your ticket is booked successfully!

Flight: {data['flight_name']}
From: {data['from_city']}
To: {data['to_city']}
Seat: {data['seat_number']}
Departure: {data['departure_time']}
Arrival: {data['arrival_time']}

Status: Confirmed ✅

Thank you for booking with us!
"""
    )

    return jsonify({"msg": "Ticket booked successfully"})

@ticket_bp.route('/my-tickets', methods=['GET'])
@jwt_required()
def get_my_tickets():
    user_id = get_jwt_identity()

    tickets = Ticket.query.filter_by(user_id=user_id).all()

    result = []

    for t in tickets:
        result.append({
            "ticket_id": t.id,
            "passenger_name": t.passenger_name,
            "from": t.from_city,
            "to": t.to_city,
            "departure": t.departure_time,
            "arrival": t.arrival_time,
            "flight": t.flight_name,
            "seat": t.seat_number,
            "price": t.ticket_price,
            "status": t.status,
            "booked_at": str(t.created_at)
        })

    return jsonify(result)

@ticket_bp.route('/cancel-ticket/<int:id>', methods=['DELETE'])
@jwt_required()
def cancel_ticket(id):
    user_id = get_jwt_identity()

    ticket = Ticket.query.filter_by(id=id, user_id=user_id).first()

    if not ticket:
        return jsonify({"msg": "Ticket not found"}), 404

    db.session.delete(ticket)
    db.session.commit()

    return jsonify({"msg": "Ticket cancelled"})