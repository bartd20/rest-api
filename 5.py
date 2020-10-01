import os
import json
import requests
from pprint import pprint

# Set the token based on the NETBOX_TOKEN environment variable
token = os.environ["NETBOX_TOKEN"]

http_headers = {}
http_headers["Content-Type"] = "application/json; version=2.4;"
http_headers["accept"] = "application/json; version=2.4;"
http_headers["Authorization"] = f"Token {token}"

url = "https://netbox.lasthop.io/api/ipam/ip-addresses/207/"
put_data = {}
put_data["address"] = "192.0.2.85/32"
put_data["description"] = "test address"

response = requests.put(url, headers=http_headers, data=json.dumps(put_data), verify=False)

print("Status code:")
print(response.status_code)
print()

print("JSON response:")
pprint(response.json())
print()


