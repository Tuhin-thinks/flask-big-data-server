from flask import Blueprint

data_blueprint = Blueprint("data", __name__)

from . import handle_data, routes
