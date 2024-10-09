#!/usr/bin/env python
# -*- coding: utf-8 -*-

### Salvatore L Greco <salvatore@isi-technology.com>
### 7/26/2023
### ISI Technology/RouteGenie Support and Integrations

"""Authentication and Create Order POST request test."""

import requests
import json
import base64
import authTest as auth

# Set the Header
header = {
    "Authorization": f"Basic {auth.get_access_token(auth.ENV['SECRET'], auth.ENV['CLIENTID'])}",
    "Content-Type": "application/x-www-form-urlencoded"
}

# set the Payload
payload = {'grant_type': 'client_credentials'}

# Request authorization token.
token_request = requests.post(f"{auth.ENV['HOST']}oauth2/token/", headers=header, data=payload)
access_token = token_request.json()['access_token']

# Print out the request status and request text
print(token_request.status_code)

print(token_request.text)

# Print out the request status and request text
print(token_request.status_code)
print(token_request.text)

payload = auth.ENV["TEST_RIDE"]

headers = {
  'Authorization': f'Bearer {access_token}'
}

response = requests.request("POST", "https://demo.routegenie.com:8000/open_api/api/v1/order/", headers=headers, data=payload)

print(response.content)