from flask import Blueprint, request, jsonify
from models import db, Account

accounts_bp = Blueprint('accounts', __name__)

@accounts_bp.route('/accounts', methods=['POST'])
def create_account():
    data = request.get_json()
    new_account = Account(
        account_name=data['account_name'],
        account_type=data['account_type']
    )
    db.session.add(new_account)
    db.session.commit()
    return jsonify({"message": "Account created successfully"}), 201

@accounts_bp.route('/accounts', methods=['GET'])
def get_accounts():
    accounts = Account.query.all()
    return jsonify([{
        'account_id': account.account_id,
        'account_name': account.account_name,
        'account_type': account.account_type
    } for account in accounts]), 200

@accounts_bp.route('/accounts/<int:account_id>', methods=['GET'])
def get_account(account_id):
    account = Account.query.get_or_404(account_id)
    return jsonify({
        'account_id': account.account_id,
        'account_name': account.account_name,
        'account_type': account.account_type
    }), 200

@accounts_bp.route('/accounts/<int:account_id>', methods=['PUT'])
def update_account(account_id):
    data = request.get_json()
    account = Account.query.get_or_404(account_id)
    account.account_name = data['account_name']
    account.account_type = data['account_type']
    db.session.commit()
    return jsonify({"message": "Account updated successfully"}), 200

@accounts_bp.route('/accounts/<int:account_id>', methods=['DELETE'])
def delete_account(account_id):
    account = Account.query.get_or_404(account_id)
    db.session.delete(account)
    db.session.commit()
    return jsonify({"message": "Account deleted successfully"}), 200