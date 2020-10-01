import os
import requests
from pprint import pprint

# Set the token based on the NETBOX_TOKEN environment variable
token = os.environ["NETBOX_TOKEN"]

http_headers = {}
http_headers["accept"] = "application/json; version=2.4;"
http_headers["Authorization"] = f"Token {token}"

url = "https://netbox.lasthop.io/api/dcim/devices/"

#response = requests.get(url, verify=False)
response = requests.get(url, headers=http_headers, verify=False)
output = response.json()

#print("JSON response:")
#pprint(output)
#print()

devices = output["results"]

for elem in devices:
    print(elem["display_name"])

