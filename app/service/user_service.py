# from app import db
# from app.model.user import User
# from flask_bcrypt import Bcrypt
#
# class UserService:
#     @staticmethod
#     def register_user(username, email, password):
#         hashed_password = Bcrypt.generate_password_hash(password).decode('utf-8')
#         new_user = user(username=username, email=email, password=hashed_password)
#
#         db.session.add(new_user)
#         db.session.commit()
#
#     @staticmethod
#     def authenticate_user(username, password):
#         user = User.query.filter_by(username=username).first()
#
#         if user and Bcrypt.check_password_hash(user.password, password):
#             return user
#
#         return None