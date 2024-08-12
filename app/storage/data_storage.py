import uuid
from typing import Any, Dict, List

processed_data_storage: Dict[str, List[Dict[str, Any]]] = {}


def store_fetched_data(data: List[Dict]):
    """Function to store data into application runtime storage

    :param data: Data to store
    :return : the stored data id
    """
    __store_id = uuid.uuid4().hex[:6]
    processed_data_storage[__store_id] = data
    return __store_id


def retrieve_processed_data(data_id: str):
    """Function to retrieve data from application runtime storage

    :param data_id: Data id to retrieve
    :return: Retrieved data
    """
    return processed_data_storage.get(data_id)
