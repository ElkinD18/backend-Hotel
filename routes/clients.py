from flask import Blueprint, request, jsonify
from models import db, Client

clients_bp = Blueprint('clients', __name__)

@clients_bp.route('/clients', methods=['POST'])
def create_client():
    data = request.get_json()
    new_client = Client(
        name=data['name'],
        address=data.get('address'),
        phone=data.get('phone'),
        email=data.get('email'),
        room_preferences=data.get('room_preferences'),
        special_requirements=data.get('special_requirements')
    )
    db.session.add(new_client)
    db.session.commit()
    return jsonify({"message": "Client created successfully"}), 201

@clients_bp.route('/clients', methods=['GET'])
def get_clients():
    clients = Client.query.all()
    return jsonify([{
        'client_id': client.client_id,
        'name': client.name,
        'address': client.address,
        'phone': client.phone,
        'email': client.email,
        'room_preferences': client.room_preferences,
        'special_requirements': client.special_requirements
    } for client in clients]), 200

@clients_bp.route('/clients/<int:client_id>', methods=['GET'])
def get_client(client_id):
    client = Client.query.get_or_404(client_id)
    return jsonify({
        'client_id': client.client_id,
        'name': client.name,
        'address': client.address,
        'phone': client.phone,
        'email': client.email,
        'room_preferences': client.room_preferences,
        'special_requirements': client.special_requirements
    }), 200

@clients_bp.route('/clients/<int:client_id>', methods=['PUT'])
def update_client(client_id):
    data = request.get_json()
    client = Client.query.get_or_404(client_id)
    client.name = data['name']
    client.address = data.get('address')
    client.phone = data.get('phone')
    client.email = data.get('email')
    client.room_preferences = data.get('room_preferences')
    client.special_requirements = data.get('special_requirements')
    db.session.commit()
    return jsonify({"message": "Client updated successfully"}), 200

@clients_bp.route('/clients/<int:client_id>', methods=['DELETE'])
def delete_client(client_id):
    client = Client.query.get_or_404(client_id)
    db.session.delete(client)
    db.session.commit()
    return jsonify({"message": "Client deleted successfully"}), 200