#!/usr/bin/env python

### Salvatore L Greco <salvatore@isi-technology.com>
### ISI Technology/RouteGenie Support and Integrations

"""Authentication and GET Order request test."""

import requests

from pprint import pprint

# We import authTest so we can reuse its functionality
import authTest as auth
from authTest import get_access_token

# Get the ENV from authTest.py
ENV = auth.ENV

# Request access token.
access_token = get_access_token()

try:
    HEADER = {
        'Authorization': f'Bearer {access_token}'
    }

    PARAM = {
        "ride_id":ENV["TEST_RIDE"]["ride_id"]
    }

    query_string = f"{ENV['HOST']}open_api/api/v1/order/{PARAM['ride_id']}/"

    print(f"Querying ORDER {PARAM['ride_id']}")
    queryorders = requests.get(
        query_string, 
        headers = HEADER
    )
    
    order =  queryorders.json()

    print(f"Query Order Response: [{queryorders.status_code}]")
    print(f"From {order["drop_off_address"]}")
    print(f"To {order["initial_time"]}")

except:
    print(f"    This request could not be processed!\n    Check that you have correctly setup your environment.json file,\n    and that your API credentials are correct.")
