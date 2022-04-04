import requests
import json
response_API = requests.get('https://api.covid19india.org/state_district_wise.json')
print(response_API)
data = response_API.text
#  json.loads() function parses the data into a JSON format.
json.loads(data)
print(response_API.status_code)
