from flask import Blueprint

api = Blueprint('api', __name__)
# user_api = Blueprint('user_api', __name__)

print(f'name is {__name__}')

from . import wallet_controller, category_controller, transaction_controller
