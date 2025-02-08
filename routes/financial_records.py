from flask import Blueprint, request, jsonify
from models import db, FinancialRecord

financial_records_bp = Blueprint('financial_records', __name__)

@financial_records_bp.route('/financial_records', methods=['POST'])
def create_financial_record():
    data = request.get_json()
    new_record = FinancialRecord(
        record_type=data['record_type'],
        amount=data['amount'],
        description=data.get('description'),
        record_date=data['record_date']
    )
    db.session.add(new_record)
    db.session.commit()
    return jsonify({"message": "Financial record created successfully"}), 201

@financial_records_bp.route('/financial_records', methods=['GET'])
def get_financial_records():
    records = FinancialRecord.query.all()
    return jsonify([{
        'record_id': record.record_id,
        'record_type': record.record_type,
        'amount': record.amount,
        'description': record.description,
        'record_date': record.record_date
    } for record in records]), 200

@financial_records_bp.route('/financial_records/<int:record_id>', methods=['GET'])
def get_financial_record(record_id):
    record = FinancialRecord.query.get_or_404(record_id)
    return jsonify({
        'record_id': record.record_id,
        'record_type': record.record_type,
        'amount': record.amount,
        'description': record.description,
        'record_date': record.record_date
    }), 200

@financial_records_bp.route('/financial_records/<int:record_id>', methods=['PUT'])
def update_financial_record(record_id):
    data = request.get_json()
    record = FinancialRecord.query.get_or_404(record_id)
    record.record_type = data['record_type']
    record.amount = data['amount']
    record.description = data.get('description')
    record.record_date = data['record_date']
    db.session.commit()
    return jsonify({"message": "Financial record updated successfully"}), 200

@financial_records_bp.route('/financial_records/<int:record_id>', methods=['DELETE'])
def delete_financial_record(record_id):
    record = FinancialRecord.query.get_or_404(record_id)
    db.session.delete(record)
    db.session.commit()
    return jsonify({"message": "Financial record deleted successfully"}), 200