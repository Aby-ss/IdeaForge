import json
import requests

from rich.traceback import install
install(show_locals=True)

# set up the request parameters
params = {
'api_key': '098DE11908BF480FBE85735565EEB280',
  'engine': 'google',
  'search_type': 'trends',
  'q': 'Abdulrehman'
}

# make the http GET request to SerpWow
api_result = requests.get('https://api.serpwow.com/search', params)

# print the JSON response from SerpWow
print(json.dumps(api_result.json()))