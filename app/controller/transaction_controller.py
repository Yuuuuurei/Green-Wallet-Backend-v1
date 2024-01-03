from flask import jsonify, request
from app.controller import api
from app.service.transaction_service import TransactionService


# Route to get all books
@api.route('/transactions', methods=['GET'])
def get_transactions():
    transactions = TransactionService.get_all_transactions()
    return jsonify({"transactions": transactions})

@api.route('/transactions/person/<string:name>', methods=['GET'])
def get_transactions_by_person(name):
    transactions = TransactionService.get_all_transactions_by_person(name)
    return jsonify({"transactions": transactions})


# Route to get a specific book by ID
@api.route('/transactions/<int:transaction_id>', methods=['GET'])
def get_transaction(transaction_id):
    transaction = TransactionService.get_transaction(transaction_id)
    if transaction is None:
        return jsonify({"error": "Transaction not found"}), 404
    return jsonify({"transaction": transaction})


# Route to create a new book
@api.route('/transactions', methods=['POST'])
def create_transaction():
    data = request.get_json()
    type = data.get('type')
    amount = data.get('amount')
    category = data.get('category')

    if not type or not amount:
        return jsonify({"error": "Type and Amount are required"}), 400

    new_transaction = TransactionService.create_transaction(type, amount, category)
    return jsonify({"transaction": new_transaction}), 201


@api.route('/transactions/chart', methods=['GET'])
def create_chart_transactions():
    name = request.args.get('name')
    type = request.args.get('type')
    chart_data = TransactionService.get_datacount_category(name, type)
    return chart_data
