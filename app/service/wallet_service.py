from datetime import datetime
from app.model.wallet import db, Wallet
from app.service.transaction_service import TransactionService


class WalletService:
    @staticmethod
    def get_all_wallets():
        wallets = Wallet.query.all()
        return [{"id": wallet.id, "amount": wallet.amount, "name": wallet.name, "createDate":wallet.createDate} for wallet in wallets]

    @staticmethod
    def get_wallet(wallet_id):
        wallet = Wallet.query.get(wallet_id)
        if wallet is None:
            return None
        return {"id": wallet.id, "amount": wallet.amount, "name": wallet.name,"createDate":wallet.createDate}

    @staticmethod
    def get_wallet_by_name(name):
        wallet = Wallet.query.filter(Wallet.name.ilike(f"%{name}%")).first()
        if wallet is None:
            return None
        return {"id": wallet.id, "amount": wallet.amount, "name": wallet.name,"createDate":wallet.createDate}


    @staticmethod
    def create_wallet(name, amount):
        new_wallet = Wallet(name=name, amount=amount, createDate=datetime.now())
        db.session.add(new_wallet)
        db.session.commit()
        return {"id": new_wallet.id, "amount": new_wallet.amount, "name": new_wallet.name}

    # @staticmethod
    # def topup_wallet(name, amount):
    #     wallet = Wallet.query.get(name)
    #     if wallet:
    #         wallet.amount = wallet.amount + amount
    #         wallet.modifiedDate = datetime.now()
    #         db.session.commit()
    #     return {"id": wallet.id, "amount": wallet.amount, "name": wallet.name}
    #
    # @staticmethod
    # def withdraw_wallet(name, amount):
    #     wallet = Wallet.query.get(name)
    #     if wallet:
    #         wallet.amount = wallet.amount - amount
    #         wallet.modifiedDate = datetime.now()
    #         db.session.commit()
    #     return {"id": wallet.id, "amount": wallet.amount, "name": wallet.name}

    @staticmethod
    def update_wallet(name, amount, type, category):
        wallet = Wallet.query.filter(Wallet.name.ilike(f"%{name}%")).first()
        if wallet:
            if type == "Debit":
                wallet.amount = wallet.amount + amount
            elif type == "Kredit":
                wallet.amount = wallet.amount - amount
            # else:
            #     return "Invalid transaction type"
        wallet.modifiedDate = datetime.now()
        db.session.commit()
        new_transaction = TransactionService.create_transaction(type, amount, category, wallet.id)
        return new_transaction