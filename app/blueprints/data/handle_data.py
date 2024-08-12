import csv

import app.config as config


def process_data(data):
    """
    Utility function to do data processing

    :param data: data downloaded from API
    :return: processed data
    """
    # as per the schema of the data; there's a 'Type' column;
    # capitalize the values in the 'Type' column;
    # and return the processed data
    for row in data:
        row["Type"] = row["Type"].capitalize()
    return data


def download_data():
    """
    Data downloader function that downloads the data from any API
    """
    with open(config.DATA_DIR / ".dummy_data" / "product_template.csv") as file:
        data = list(csv.DictReader(file))

        return data
