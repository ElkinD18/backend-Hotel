from flask import Blueprint, request, jsonify
from models import db, GeneralParameter

general_parameters_bp = Blueprint('general_parameters', __name__)

@general_parameters_bp.route('/general_parameters', methods=['POST'])
def create_general_parameter():
    data = request.get_json()
    new_parameter = GeneralParameter(
        parameter_name=data['parameter_name'],
        parameter_value=data['parameter_value']
    )
    db.session.add(new_parameter)
    db.session.commit()
    return jsonify({"message": "General parameter created successfully"}), 201

@general_parameters_bp.route('/general_parameters', methods=['GET'])
def get_general_parameters():
    parameters = GeneralParameter.query.all()
    return jsonify([{
        'parameter_id': parameter.parameter_id,
        'parameter_name': parameter.parameter_name,
        'parameter_value': parameter.parameter_value
    } for parameter in parameters]), 200

@general_parameters_bp.route('/general_parameters/<int:parameter_id>', methods=['GET'])
def get_general_parameter(parameter_id):
    parameter = GeneralParameter.query.get_or_404(parameter_id)
    return jsonify({
        'parameter_id': parameter.parameter_id,
        'parameter_name': parameter.parameter_name,
        'parameter_value': parameter.parameter_value
    }), 200

@general_parameters_bp.route('/general_parameters/<int:parameter_id>', methods=['PUT'])
def update_general_parameter(parameter_id):
    data = request.get_json()
    parameter = GeneralParameter.query.get_or_404(parameter_id)
    parameter.parameter_name = data['parameter_name']
    parameter.parameter_value = data['parameter_value']
    db.session.commit()
    return jsonify({"message": "General parameter updated successfully"}), 200

@general_parameters_bp.route('/general_parameters/<int:parameter_id>', methods=['DELETE'])
def delete_general_parameter(parameter_id):
    parameter = GeneralParameter.query.get_or_404(parameter_id)
    db.session.delete(parameter)
    db.session.commit()
    return jsonify({"message": "General parameter deleted successfully"}), 200