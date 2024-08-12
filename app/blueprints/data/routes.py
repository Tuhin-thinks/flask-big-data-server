from flask import jsonify, request

from app.storage.data_storage import retrieve_processed_data, store_fetched_data

from . import data_blueprint
from .handle_data import download_data, process_data


@data_blueprint.route("/fetch-data")
def fetch_data():
    """
    This route fetches data from shopify;
    processes it and stores it in the flask session storage;
    Returns the processed data id as a response;

    :return: Processed data id
    """
    data = download_data()

    processed_data = process_data(data)

    stored_data_id = store_fetched_data(processed_data)

    return (
        jsonify(
            {
                "data_id": stored_data_id,
                "message": "Processed data instance created successfully.",
            }
        ),
        200,
    )


@data_blueprint.route("/get-processed-data")
def get_processed_data():
    """
    This route fetches the processed data from the flask session storage;
    Returns the processed data as a response;

    :return: Processed data
    """
    data_id = request.args.get("data_id")
    if not data_id:
        return jsonify({"error": "data_id is required"}), 400

    retrieved_data = retrieve_processed_data(data_id)
    return jsonify({"data": retrieved_data}), 200
