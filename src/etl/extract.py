# Extract the information from the api into json obj.

import requests
import json
from src import config


def extract_api(section):
    """Iterator yield single json obj at time."""

    url_list = config.api_config(section)

    for url in url_list:
        api_response = requests.get(url)
        json_obj_list = json.loads(api_response.text)
        for json_obj in json_obj_list:
            yield json_obj
