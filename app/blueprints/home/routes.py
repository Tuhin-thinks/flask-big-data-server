from flask import jsonify

from . import home_blueprint


@home_blueprint.route("/")
def home():
    return (
        jsonify(
            {
                "message": "Welcome to Shopify Data Retriever!",
                "Author": "Tuhin Mitra",
                "Version": "1.0",
                "website": "https://github.com/Tuhin-thinks/flask-big-data-server",
            }
        ),
        200,
    )
