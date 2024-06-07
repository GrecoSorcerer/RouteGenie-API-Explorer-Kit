#!/usr/bin/env python
# -*- coding: utf-8 -*-

### Salvatore L Greco <salvatore@isi-technology.com>
### 7/26/2023
### ISI Technology/RouteGenie Support and Integrations

"""Authentication and Create Order POST request test."""

import requests
import json
import base64


def get_access_token(client_secret, client_id):
    """Returns the base64 encoded access token credential.

    Parameters:
    client_secret (str): The RGAPI Client Secret.
    client_id (str): The RGAPI Client ID.
    """
    # Format the credential.
    credentials = f"{client_id}:{client_secret}"

    # Credentials is encoded from utf-8 to a base64 byte string.
    # The encoded credential is then converted from a byte string to a string.
    encoded_credentials = base64.b64encode(credentials.encode("utf-8")).decode("utf-8")

    # DEMONSTRATION of common error
    encoded_credentials_byte = base64.b64encode(credentials.encode("utf-8"))
    # Print value that will NOT send correctly
    print(encoded_credentials_byte)
    # Pritn value that will send correctly
    print(encoded_credentials)


    return encoded_credentials


# Load the environment variables. 
# NOTE: This is not the only way environment varibles can be set.
with open('./environment.json') as env_file:
    ENV = json.load(env_file)

# Set the Header
header = {
    "Authorization": f"Basic {get_access_token(ENV['SECRET'], ENV['CLIENTID'])}",
    "Content-Type": "application/x-www-form-urlencoded"
}

# set the Payload
payload = {'grant_type': 'client_credentials'}

# Request authorization token.
token_request = requests.post(f"{ENV['HOST']}oauth2/token/", headers=header, data=payload)
access_token = token_request.json()['access_token']

# Print out the request status and request text
print(token_request.status_code)

print(token_request.text)

# Print out the request status and request text
print(token_request.status_code)
print(token_request.text)

payload = {
    "ride_id": "132A",
    "client_internal_id": 613,
    "custom_trip_type": 1,
    "initial_time": "03/06/2024 13:45",
    "pick_up_address":"490 Delaware Ave, Buffalo NY 14213",
    "drop_off_address":"1770 Colvin Blvd, Buffalo NY 14223",
    "payment_method":0
}


headers = {
  'Authorization': f'Bearer {access_token}'
}

response = requests.request("POST", "https://demo.routegenie.com:8000/open_api/api/v1/order/", headers=headers, data=payload)

print(response.content)