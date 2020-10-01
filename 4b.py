import os
import requests
from pprint import pprint

# Set the token based on the NETBOX_TOKEN environment variable
token = os.environ["NETBOX_TOKEN"]

http_headers = {}
http_headers["accept"] = "application/json; version=2.4;"
http_headers["Authorization"] = f"Token {token}"

url = "https://netbox.lasthop.io/api/ipam/ip-addresses/212/"

response = requests.get(url, headers=http_headers, verify=False)
output = response.json()

print("JSON response:")
pprint(output)
print()

