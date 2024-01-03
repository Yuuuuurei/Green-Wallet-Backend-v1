from flask import jsonify, request
from app.controller import api
from app.service.wallet_service import WalletService


# Route to get all books
@api.route('/wallets', methods=['GET'])
def get_wallets():
    wallets = WalletService.get_all_wallets()
    return jsonify({"wallets": wallets})

# Route to get a specific book by ID
@api.route('/wallets/<int:wallet_id>', methods=['GET'])
def get_wallet(wallet_id):
    wallet = WalletService.get_wallet(wallet_id)
    if wallet is None:
        return jsonify({"error": "Wallet not found"}), 404
    return jsonify({"wallet": wallet})

@api.route('/wallets/<string:name>', methods=['GET'])
def get_wallet_by_name(name):
    wallet = WalletService.get_wallet_by_name(name)
    if wallet is None:
        return jsonify({"error": "Wallet not found"}), 404
    return jsonify({"wallet": wallet})

# Route to create a new book
@api.route('/wallets', methods=['POST'])
def create_wallet():
    data = request.get_json()
    name = data.get('name')
    amount = data.get('amount')

    if not name or not amount:
        return jsonify({"error": "Name and Amount are required"}), 400

    new_wallet = WalletService.create_wallet(name, amount)
    return jsonify({"wallet": new_wallet}), 201

# @api.route('/wallets', methods=['PUT'])
# def topup_wallet():
#     data = request.get_json()
#     name = data.get('name')
#     amount = data.get('amount')
#
#     if not name or not amount:
#         return jsonify({"error": "Name and Amount are required"}), 400
#
#     new_wallet = WalletService.topup_wallet(name, amount)
#     return jsonify({"wallet": new_wallet}), 201
#
# @api.route('/wallets', methods=['PUT'])
# def withdraw_wallet():
#     data = request.get_json()
#     name = data.get('name')
#     amount = data.get('amount')
#
#     if not name or not amount:
#         return jsonify({"error": "Name and Amount are required"}), 400
#
#     new_wallet = WalletService.topup_wallet(name, amount)
#     return jsonify({"wallet": new_wallet}), 201

@api.route('/wallets', methods=['PUT'])
def update_wallet():
    data = request.get_json()
    name = data.get('name')
    amount = data.get('amount')
    type = data.get('type')
    category = data.get('category')

    if not name or not amount or not type:
        return jsonify({"error": "Name and Amount are required"}), 400

    new_wallet = WalletService.update_wallet(name, amount, type, category)
    return jsonify({"wallet": new_wallet}), 201