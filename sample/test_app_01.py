from urllib.parse import urljoin

import requests

HOST_URL = "http://localhost:5000"


def process_data():
    fetch_data_url = urljoin(HOST_URL, "/fetch-data")
    response = requests.get(fetch_data_url)

    if response.status_code == 200:
        return response.json()

    return None


def retrieve_data(data_id: str):
    retrieve_data_url = urljoin(HOST_URL, "/get-processed-data")
    response = requests.get(retrieve_data_url, params={"data_id": data_id})

    if response.status_code == 200:
        return response.json()

    return None


def main():
    data = process_data()
    print(data)

    assert data is not None

    data = retrieve_data(data["data_id"])
    print(data)


if __name__ == "__main__":
    main()
