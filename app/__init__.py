from flask import Flask

from app.blueprints.data.routes import data_blueprint
from app.blueprints.home.routes import home_blueprint


def create_app():
    """
    Create the flask app and register all the available blueprints

    :return: Flask app
    """
    app = Flask(__name__)
    app.register_blueprint(home_blueprint)
    app.register_blueprint(data_blueprint, url_prefix="/data")
    return app
