# from datetime import datetime
# from flask_login import UserMixin
# from app.model import db
# from flask_bcrypt import Bcrypt
#
# bcrypt = Bcrypt()
#
# class User(db.Model, UserMixin):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(50), unique=True, nullable=False)
#     email = db.Column(db.String(120), unique=True, nullable=False)
#     password = db.Column(db.String(60), nullable=False)  # Hashed password
#     create_date = db.Column(db.DateTime, default=datetime.utcnow)
#
#     def set_password(self, password):
#         self.password = bcrypt.generate_password_hash(password).decode('utf-8')
#
#     def check_password(self, password):
#         return bcrypt.check_password_hash(self.password, password)
