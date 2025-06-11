#!/usr/bin/env python
# -*- coding: utf-8 -*-

### Salvatore L Greco <salvatore@isi-technology.com>
### ISI Technology/RouteGenie Support and Integrations

"""Authentication and POST Create Order request test."""

import requests
from pprint import pprint

# We import authTest so we can reuse its functionality
import authTest as auth
from authTest import get_access_token

# Get the ENVironment from authTest.py
ENV = auth.ENV

url = f"{ENV["HOST"]}open_api/api/v1/order/"
# Request access token.
access_token = get_access_token()
headers = {
    'Authorization': f'Bearer {access_token}'
}
# Get the Test Ride from the ENVironment
payload = ENV["TEST_RIDE"]

print(f"\n------\nRequesting ride for client_id {ENV["TEST_RIDE"]["client_internal_id"]}")
print(f"From {ENV["TEST_RIDE"]["pick_up_address"]}")
print(f"To {ENV["TEST_RIDE"]["drop_off_address"]}")
if ENV["TEST_RIDE"]["initial_time"]:
    at_text = f"Pickup At {ENV["TEST_RIDE"]["initial_time"]}"
elif ENV["TEST_RIDE"]["appointment_time"]:
    at_text = f"Dropoff by {ENV["TEST_RIDE"]["appointment_time"]}"
print(f"{at_text}")

response = requests.post(
    url, 
    headers=headers, 
    data=payload
)

match response.status_code:
    case 201:
        print(f"Ride created successfully [{response.status_code}]")
    case _:
        print(f"Ride could not be created [{response.status_code}]")