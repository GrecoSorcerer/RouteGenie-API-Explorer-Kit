#!/usr/bin/env python
# -*- coding: utf-8 -*-

### Salvatore L Greco <salvatore@isi-technology.com>
### ISI Technology/RouteGenie Support and Integrations

"""Authentication POST request test."""

import requests
from requests.auth import HTTPBasicAuth
import json

# Load the environment variables. 
# NOTE: This is not the only way environment varibles can be set.
with open('./TESTS/environment.json') as env_file:
    ENV = json.load(env_file)


def get_access_token():
    # Set the Header
    header = {
        "Content-Type": "application/x-www-form-urlencoded"
    }

    # set the Payload
    payload = {
        'grant_type': 'client_credentials'
    }

    # Request authorization token.
    token_request = requests.post(
        f"{ENV['HOST']}oauth2/token/", 
        headers=header,
        auth=(ENV["CLIENTID"],ENV["SECRET"]),
        data=payload
    )
    
    # Print out the request status and request text.
    print(f'Requesting Authentication ["{ENV['HOST']}" - {token_request.status_code}]')    

    return token_request.json()['access_token']


if __name__ == "__main__":
    # Request an access token.
    access_token = get_access_token()

    # Use the Payer API GET "Get list of available payers" to check our token.
    url = f"{ENV['HOST']}open_api/api/v1/payer/"
    payload={}
    header = {
        'Authorization': f'Bearer {access_token}'
    }

    results = requests.get(
        url,
        headers=header,
        data=payload
    )

    print(f"Verifying Access Token [{results.status_code}]")