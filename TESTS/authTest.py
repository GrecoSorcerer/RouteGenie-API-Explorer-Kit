#!/usr/bin/env python
# -*- coding: utf-8 -*-

### Salvatore L Greco <salvatore@isi-technology.com>
### ISI Technology/RouteGenie Support and Integrations

"""Authentication POST request test."""

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

    print("Generating Token")
    # Credentials is encoded from utf-8 to a base64 byte string.
    # The encoded credential is then converted from a byte string to a string.
    encoded_credentials = base64.b64encode(credentials.encode("utf-8")).decode("utf-8")

    # DEMONSTRATION of common error
    #encoded_credentials_byte = base64.b64encode(credentials.encode("utf-8"))
    
    # Print value that will NOT send correctly
    #print(encoded_credentials_byte)


    # Print value that WILL send correctly
    #print(encoded_credentials)
    
    return encoded_credentials

# Load the environment variables. 
# NOTE: This is not the only way environment varibles can be set.
with open('./TESTS/environment.json') as env_file:
    ENV = json.load(env_file)


if __name__ == "__main__":
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

    # Print out the request status and request text
    print(f'Requesting Authentication ["{ENV['HOST']}" - {token_request.status_code}]')    
    print(f"->  {token_request.text}")

    # Use the Payer API GET "Get ilst of available payers" to check our token
    url = f"{ENV['HOST']}open_api/api/v1/payer/"
    payload={}
    headers = {
        'Authorization': f'Bearer {token_request.json()['access_token']}'
    }

    results = requests.get(url, 
                           headers=headers, 
                           data=payload)

    print(f"Verifying Access Token [{results.status_code}]")

