#!/usr/bin/env python
# -*- coding: utf-8 -*-

### Salvatore L Greco <salvatore@isi-technology.com>
### 7/26/2023
### ISI Technology/RouteGenie Support and Integrations

"""Authentication and Create Order POST request test."""

import requests
import json
import base64

from pprint import pprint
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
print(f'Requesting Authentication ["{auth.ENV['HOST']}" - {token_request.status_code}]')    
print(f"->  {token_request.text}")

try:
    HEADER = {
        'Authorization': f'Bearer {access_token}'
    }

    PARAM = {
        "ride_id":auth.ENV["TEST_RIDE"]["ride_id"]
    }

    query_string = f"{auth.ENV['HOST']}open_api/api/v1/order/{PARAM['ride_id']}/"

    print(f"Querying ORDER {PARAM['ride_id']}")
    queryorders = requests.get(query_string, 
                            headers = HEADER)

    print(f"Query Order Response: [{queryorders.status_code}]")
 
    DATA = queryorders.json()

    pprint(DATA, indent=4)
except:
    print(f"This request could not be processed! Request Status Code [{queryorders.status_code}]")
    print(f"->  {queryorders.reason}")
