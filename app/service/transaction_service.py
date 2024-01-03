import json
from datetime import datetime

from sqlalchemy import func

from app.model.transaction import db, Transaction
from app.model.wallet import Wallet
from app.utilities import format_util


class TransactionService:
    @staticmethod
    def get_all_transactions():
        transactions = Transaction.query.all()
        return [{"id": transaction.id, "amount": transaction.amount, "type": transaction.type,
                 "createDate": transaction.createDate, "category": transaction.category} for transaction in
                transactions]

    @staticmethod
    def get_all_transactions_by_person(name):
        wallet = Wallet.query.filter(Wallet.name.ilike(f"%{name}%")).first()
        transactions = Transaction.query.filter(Transaction.wallet_id == wallet.id).all()

        return [{"id": transaction.id, "amount": transaction.amount, "type": transaction.type,
                 "createDate": transaction.createDate, "category": transaction.category} for transaction in
                transactions]


    @staticmethod
    def get_transaction(transaction_id):
        transaction = Transaction.query.get(transaction_id)
        if transaction is None:
            return None
        return {"id": transaction.id, "amount": transaction.amount, "type": transaction.type,
                "createDate": transaction.createDate, "category": transaction.category}

    @staticmethod
    def create_transaction(type, amount, category, wallet_id):
        new_transaction = Transaction(type=type, amount=amount, category=category, createDate=datetime.now(),
                                      wallet_id=wallet_id)
        db.session.add(new_transaction)
        db.session.commit()
        return {"id": new_transaction.id, "amount": new_transaction.amount, "type": new_transaction.type,
                "category": new_transaction.category, "wallet id": new_transaction.wallet_id}

    @staticmethod
    def get_datacount_category(name, type):
        wallet_id = 10
        result = (Transaction.query.with_entities(Transaction.category, func.sum(Transaction.amount)).
                  filter(Transaction.wallet_id == wallet_id, Transaction.type == type).
                  group_by(Transaction.category).all())

        categoryList = [category[0] for category in result]
        sumList = [format_util.format_rupiah(sum[1]) for sum in result]
        resultMap = {}
        resultMap["category"] = categoryList
        resultMap["sum"] = sumList
        return resultMap
