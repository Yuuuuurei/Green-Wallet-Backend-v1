# # user_controller.py
#
# from flask import Blueprint, jsonify, request
# from flask_login import login_user, login_required, logout_user, current_user
# from app.service import userService
# from app.controller import user_api
#
# @user_api.route('/register', methods=['POST'])
# def register():
#     data = request.get_json()
#     username = data.get('username')
#     email = data.get('email')
#     password = data.get('password')
#
#     if not username or not email or not password:
#         return jsonify({"error": "Missing required fields"}), 400
#
#     userService.register_user(username, email, password)
#
#     return jsonify({"message": "User registered successfully"}), 201
#
# @user_api.route('/login', methods=['POST'])
# def login():
#     data = request.get_json()
#     username = data.get('username')
#     password = data.get('password')
#
#     user = userService.authenticate_user(username, password)
#
#     if user:
#         login_user(user)
#         return jsonify({"message": "Login successful"}), 200
#     else:
#         return jsonify({"error": "Invalid username or password"}), 401
#
# @user_api.route('/logout', methods=['POST'])
# @login_required
# def logout():
#     logout_user()
#     return jsonify({"message": "Logout successful"}), 200
#
# @user_api.route('/profile', methods=['GET'])
# @login_required
# def profile():
#     return jsonify({"username": current_user.username, "email": current_user.email}), 200