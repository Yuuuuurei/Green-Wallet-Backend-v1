from datetime import datetime
from app.model import db

class Wallet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Double, nullable=False)
    name = db.Column(db.String(100), nullable=False)
    createDate = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    modifiedDate = db.Column(db.DateTime, index=True, default=datetime.utcnow)
