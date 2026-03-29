from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required
from models.user_model import db, User
from models.flight_model import Flight
from models.ticket_model import Ticket
from utils.admin_middleware import admin_required

admin_bp = Blueprint('admin', __name__)
# Get all users (Admin Only)
@admin_bp.route('/users', methods=['GET'])
@jwt_required()
@admin_required
def get_all_users():
    users = User.query.all()

    return jsonify([
        {
            "id": u.id,
            "name": u.full_name(),
            "email": u.email,
            "is_admin": u.is_admin
        } for u in users
    ])
# Delete a user (Admin Only)
@admin_bp.route('/delete-user/<string:id>', methods=['DELETE'])
@jwt_required()
@admin_required
def delete_user(id):
    user = User.query.get(id)

    if not user:
        return jsonify({"msg": "User not found"}), 404

    db.session.delete(user)
    db.session.commit()

    return jsonify({"msg": "User deleted"})
# Add a flight (Admin Only)
@admin_bp.route('/add-flight', methods=['POST'])
@jwt_required()
@admin_required
def add_flight():
    data = request.json

    flight = Flight(
        flight_name=data['flight_name'],
        from_city=data['from_city'],
        to_city=data['to_city'],
        departure_time=data['departure_time'],
        arrival_time=data['arrival_time'],
        price=data['price']
    )

    db.session.add(flight)
    db.session.commit()

    return jsonify({"msg": "Flight added"})

# Update a flight (Admin Only)
@admin_bp.route('/update-flight/<string:id>', methods=['PUT'])
@jwt_required()
@admin_required
def update_flight(id):
    flight = Flight.query.get(id)

    if not flight:
        return jsonify({"msg": "Flight not found"}), 404

    data = request.json

    flight.flight_name = data.get('flight_name', flight.flight_name)
    flight.price = data.get('price', flight.price)

    db.session.commit()

    return jsonify({"msg": "Flight updated"})

# Delete a flight (Admin Only)
@admin_bp.route('/delete-flight/<string:id>', methods=['DELETE'])
@jwt_required()
@admin_required
def delete_flight(id):
    flight = Flight.query.get(id)

    if not flight:
        return jsonify({"msg": "Flight not found"}), 404

    db.session.delete(flight)
    db.session.commit()

    return jsonify({"msg": "Flight deleted"})

# Get all tickets (Admin Only)
@admin_bp.route('/tickets', methods=['GET'])
@jwt_required()
@admin_required
def get_all_tickets():
    tickets = Ticket.query.all()

    return jsonify([
        {
            "id": t.id,
            "user_id": t.user_id,
            "flight": t.flight_name,
            "status": t.status
        } for t in tickets
    ])