from flask import jsonify, request
from app.controller import api
from app.service.category_service import CategoryService


# Route to get all books
@api.route('/categories', methods=['GET'])
def get_categories():
    categories = CategoryService.get_all_categories()
    return jsonify({"categories": categories})

# Route to get a specific book by ID
@api.route('/categories/<int:category_id>', methods=['GET'])
def get_category(category_id):
    category = CategoryService.get_category(category_id)
    if category is None:
        return jsonify({"error": "Category not found"}), 404
    return jsonify({"category": category})

# Route to create a new book
@api.route('/categories', methods=['POST'])
def create_category():
    data = request.get_json()
    category = data.get("category")

    if not category:
        return jsonify({"error": "Category is required"}), 400

    new_category = CategoryService.create_category(category)
    return jsonify({"category": new_category}), 201