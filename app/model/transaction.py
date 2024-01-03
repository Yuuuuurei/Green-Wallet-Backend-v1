from datetime import datetime
from app.model import db

class Transaction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    wallet_id = db.Column(db.Integer, nullable=False)
    amount = db.Column(db.Double, nullable=False)
    type = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(100), nullable=False)
    createDate = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    modifiedDate = db.Column(db.DateTime, index=True, default=datetime.utcnow)

