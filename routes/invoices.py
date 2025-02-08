from flask import Blueprint, request, jsonify
from models import db, Invoice

invoices_bp = Blueprint('invoices', __name__)

@invoices_bp.route('/invoices', methods=['POST'])
def create_invoice():
    data = request.get_json()
    new_invoice = Invoice(
        reservation_id=data['reservation_id'],
        issue_date=data['issue_date'],
        total_amount=data['total_amount'],
        tax_amount=data['tax_amount'],
        payment_method=data['payment_method']
    )
    db.session.add(new_invoice)
    db.session.commit()
    return jsonify({"message": "Invoice created successfully"}), 201

@invoices_bp.route('/invoices', methods=['GET'])
def get_invoices():
    invoices = Invoice.query.all()
    return jsonify([{
        'invoice_id': invoice.invoice_id,
        'reservation_id': invoice.reservation_id,
        'issue_date': invoice.issue_date,
        'total_amount': invoice.total_amount,
        'tax_amount': invoice.tax_amount,
        'payment_method': invoice.payment_method
    } for invoice in invoices]), 200

@invoices_bp.route('/invoices/<int:invoice_id>', methods=['GET'])
def get_invoice(invoice_id):
    invoice = Invoice.query.get_or_404(invoice_id)
    return jsonify({
        'invoice_id': invoice.invoice_id,
        'reservation_id': invoice.reservation_id,
        'issue_date': invoice.issue_date,
        'total_amount': invoice.total_amount,
        'tax_amount': invoice.tax_amount,
        'payment_method': invoice.payment_method
    }), 200

@invoices_bp.route('/invoices/<int:invoice_id>', methods=['PUT'])
def update_invoice(invoice_id):
    data = request.get_json()
    invoice = Invoice.query.get_or_404(invoice_id)
    invoice.reservation_id = data['reservation_id']
    invoice.issue_date = data['issue_date']
    invoice.total_amount = data['total_amount']
    invoice.tax_amount = data['tax_amount']
    invoice.payment_method = data['payment_method']
    db.session.commit()
    return jsonify({"message": "Invoice updated successfully"}), 200

@invoices_bp.route('/invoices/<int:invoice_id>', methods=['DELETE'])
def delete_invoice(invoice_id):
    invoice = Invoice.query.get_or_404(invoice_id)
    db.session.delete(invoice)
    db.session.commit()
    return jsonify({"message": "Invoice deleted successfully"}), 200