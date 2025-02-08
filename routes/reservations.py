from flask import Blueprint, request, jsonify
from models import db, Reservation

reservations_bp = Blueprint('reservations', __name__)

@reservations_bp.route('/reservations', methods=['POST'])
def create_reservation():
    data = request.get_json()
    new_reservation = Reservation(
        client_id=data['client_id'],
        room_id=data['room_id'],
        check_in=data['check_in'],
        check_out=data['check_out'],
        status=data.get('status', 'confirmada')
    )
    db.session.add(new_reservation)
    db.session.commit()
    return jsonify({"message": "Reservation created successfully"}), 201

@reservations_bp.route('/reservations', methods=['GET'])
def get_reservations():
    reservations = Reservation.query.all()
    return jsonify([{
        'reservation_id': reservation.reservation_id,
        'client_id': reservation.client_id,
        'room_id': reservation.room_id,
        'check_in': reservation.check_in,
        'check_out': reservation.check_out,
        'status': reservation.status
    } for reservation in reservations]), 200

@reservations_bp.route('/reservations/<int:reservation_id>', methods=['GET'])
def get_reservation(reservation_id):
    reservation = Reservation.query.get_or_404(reservation_id)
    return jsonify({
        'reservation_id': reservation.reservation_id,
        'client_id': reservation.client_id,
        'room_id': reservation.room_id,
        'check_in': reservation.check_in,
        'check_out': reservation.check_out,
        'status': reservation.status
    }), 200

@reservations_bp.route('/reservations/<int:reservation_id>', methods=['PUT'])
def update_reservation(reservation_id):
    data = request.get_json()
    reservation = Reservation.query.get_or_404(reservation_id)
    reservation.client_id = data['client_id']
    reservation.room_id = data['room_id']
    reservation.check_in = data['check_in']
    reservation.check_out = data['check_out']
    reservation.status = data.get('status', reservation.status)
    db.session.commit()
    return jsonify({"message": "Reservation updated successfully"}), 200

@reservations_bp.route('/reservations/<int:reservation_id>', methods=['DELETE'])
def delete_reservation(reservation_id):
    reservation = Reservation.query.get_or_404(reservation_id)
    db.session.delete(reservation)
    db.session.commit()
    return jsonify({"message": "Reservation deleted successfully"}), 200