# Extract the information from the api into json obj.

import requests
import json
from src import config


def extract_api(section):
    url_list = config.api_config(section)
    api_response = requests.get(url_list[0])
    json_obj = json.loads(api_response.text)

    return json_obj
