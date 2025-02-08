from flask import Blueprint, request, jsonify
from models import db, Room

rooms_bp = Blueprint('rooms', __name__)

@rooms_bp.route('/rooms', methods=['POST'])
def create_room():
    data = request.get_json()
    new_room = Room(
        room_number=data['room_number'],
        room_type=data['room_type'],
        availability=data.get('availability', True)
    )
    db.session.add(new_room)
    db.session.commit()
    return jsonify({"message": "Room created successfully"}), 201

@rooms_bp.route('/rooms', methods=['GET'])
def get_rooms():
    rooms = Room.query.all()
    return jsonify([{
        'room_id': room.room_id,
        'room_number': room.room_number,
        'room_type': room.room_type,
        'availability': room.availability
    } for room in rooms]), 200

@rooms_bp.route('/rooms/<int:room_id>', methods=['GET'])
def get_room(room_id):
    room = Room.query.get_or_404(room_id)
    return jsonify({
        'room_id': room.room_id,
        'room_number': room.room_number,
        'room_type': room.room_type,
        'availability': room.availability
    }), 200

@rooms_bp.route('/rooms/<int:room_id>', methods=['PUT'])
def update_room(room_id):
    data = request.get_json()
    room = Room.query.get_or_404(room_id)
    room.room_number = data['room_number']
    room.room_type = data['room_type']
    room.availability = data.get('availability', room.availability)
    db.session.commit()
    return jsonify({"message": "Room updated successfully"}), 200

@rooms_bp.route('/rooms/<int:room_id>', methods=['DELETE'])
def delete_room(room_id):
    room = Room.query.get_or_404(room_id)
    db.session.delete(room)
    db.session.commit()
    return jsonify({"message": "Room deleted successfully"}), 200