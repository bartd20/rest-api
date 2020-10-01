import requests
from pprint import pprint

#url = "https://netbox.lasthop.io/api/"
url = "https://netbox.lasthop.io/api/dcim/"
http_headers = {"accept": "application/json; version=2.4;"}

#response = requests.get(url, verify=False)
response = requests.get(url, headers=http_headers, verify=False)

print("JSON response:")
pprint(response.json())
print()

print("Status code:")
print(response.status_code)
print()

print("Text:")
pprint(response.text)
print()

print("Headers:")
pprint(response.headers)
print()

