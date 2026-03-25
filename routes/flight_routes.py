from flask import Blueprint, request, jsonify
from models.flight_model import Flight, db
from flask_jwt_extended import jwt_required

flight_bp = Blueprint('flight', __name__)

@flight_bp.route('/add-flight', methods=['POST'])
@jwt_required()
def add_flight():
    data = request.json

    flight = Flight(
        source=data['source'],
        destination=data['destination'],
        date=data['date'],
        seats=data['seats'],
        price=data['price']
    )

    db.session.add(flight)
    db.session.commit()

    return jsonify({"msg": "Flight added"})

@flight_bp.route('/flights', methods=['GET'])
def get_flights():
    flights = Flight.query.all()
    return jsonify([{
        "id": f.id,
        "source": f.source,
        "destination": f.destination,
        "price": f.price
    } for f in flights])

@flight_bp.route('/flights/<string:flight_id>', methods=['GET'])
def get_single_flight(flight_id):
    flight = Flight.query.get(flight_id)

    if not flight:
        return jsonify({"msg": "Flight not found"}), 404

    return jsonify({
        "id": flight.id,
        "source": flight.source,
        "destination": flight.destination,
        "date": str(flight.date),
        "seats": flight.seats,
        "price": flight.price
    })

@flight_bp.route('/flights/<string:flight_id>', methods=['PUT'])
@jwt_required()
def update_flight(flight_id):
    data = request.json

    flight = Flight.query.get(flight_id)

    if not flight:
        return jsonify({"msg": "Flight not found"}), 404

    # Update fields (only if provided)
    flight.source = data.get('source', flight.source)
    flight.destination = data.get('destination', flight.destination)
    flight.date = data.get('date', flight.date)
    flight.seats = data.get('seats', flight.seats)
    flight.price = data.get('price', flight.price)

    db.session.commit()

    return jsonify({"msg": "Flight updated successfully"})

@flight_bp.route('/flights/<string:flight_id>', methods=['DELETE'])
@jwt_required()
def delete_flight(flight_id):
    flight = Flight.query.get(flight_id)

    if not flight:
        return jsonify({"msg": "Flight not found"}), 404

    db.session.delete(flight)
    db.session.commit()

    return jsonify({"msg": "Flight deleted successfully"})