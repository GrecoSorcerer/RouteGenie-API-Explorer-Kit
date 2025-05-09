#!/usr/bin/env python
# -*- coding: utf-8 -*-

### Salvatore L Greco <salvatore@isi-technology.com>
### ISI Technology/RouteGenie Support and Integrations

"""Authentication and POST Create Order request test."""

import requests

# We import authTest so we can reuse its functionality
import authTest as auth
from authTest import get_access_token

# Get the ENV from authTest.py
ENV = auth.ENV

# Set the Header
header = {
    "Authorization": f"Basic {get_access_token(ENV['SECRET'], ENV['CLIENTID'])}",
    "Content-Type": "application/x-www-form-urlencoded"
}

# set the Payload
payload = {'grant_type': 'client_credentials'}

# Request authorization token.
token_request = requests.post(f"{ENV['HOST']}oauth2/token/",
                              headers=header,
                              data=payload)
access_token = token_request.json()['access_token']

# Print out the request status and request text
print(token_request.status_code)
print(token_request.text)

payload = ENV["TEST_RIDE"]

headers = {
  'Authorization': f'Bearer {access_token}'
}

response = requests.post(f"{ENV["HOST"]}open_api/api/v1/order/", 
                         headers=headers, 
                         data=payload)

print(response.content)