import requests
import json
import pprint

url = 'https://api.punkapi.com/v2/beers?page=5&per_page=80'

r = requests.get(url)
api_json = json.loads(r.text)

# pprint.pprint(api_json)\
# print(len(api_json))
for i in api_json:
    print(i)