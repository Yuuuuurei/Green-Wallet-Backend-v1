from app.model.category import db, Category

class CategoryService:
    @staticmethod
    def get_all_categories():
        categories = Category.query.all()
        return [{"id": category.id, "category": category.category} for category in categories]

    @staticmethod
    def get_category(category_id):
        category = Category.query.get(category_id)
        if category is None:
            return None
        return {"id": category.id, "category": category.category}

    @staticmethod
    def create_category(category):
        new_category = Category(category=category)
        db.session.add(new_category)
        db.session.commit()
        return {"id": new_category.id, "category": new_category.category}
