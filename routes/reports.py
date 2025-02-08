from flask import Blueprint, request, jsonify
from models import db, Report

reports_bp = Blueprint('reports', __name__)

@reports_bp.route('/reports', methods=['POST'])
def create_report():
    data = request.get_json()
    new_report = Report(
        report_name=data['report_name'],
        report_data=data['report_data']
    )
    db.session.add(new_report)
    db.session.commit()
    return jsonify({"message": "Report created successfully"}), 201

@reports_bp.route('/reports', methods=['GET'])
def get_reports():
    reports = Report.query.all()
    return jsonify([{
        'report_id': report.report_id,
        'report_name': report.report_name,
        'report_data': report.report_data,
        'generated_at': report.generated_at
    } for report in reports]), 200

@reports_bp.route('/reports/<int:report_id>', methods=['GET'])
def get_report(report_id):
    report = Report.query.get_or_404(report_id)
    return jsonify({
        'report_id': report.report_id,
        'report_name': report.report_name,
        'report_data': report.report_data,
        'generated_at': report.generated_at
    }), 200

@reports_bp.route('/reports/<int:report_id>', methods=['PUT'])
def update_report(report_id):
    data = request.get_json()
    report = Report.query.get_or_404(report_id)
    report.report_name = data['report_name']
    report.report_data = data['report_data']
    db.session.commit()
    return jsonify({"message": "Report updated successfully"}), 200

@reports_bp.route('/reports/<int:report_id>', methods=['DELETE'])
def delete_report(report_id):
    report = Report.query.get_or_404(report_id)
    db.session.delete(report)
    db.session.commit()
    return jsonify({"message": "Report deleted successfully"}), 200