#!/usr/bin/env python

### Salvatore L Greco <salvatore@isi-technology.com>
### ISI Technology/RouteGenie Support and Integrations

"""Authentication and GET Report Test."""

import requests

# We import authTest so we can reuse its functionality
import authTest as auth
from authTest import get_access_token

import csv
import io

# Get the ENV from authTest.py
ENV = auth.ENV

# Request access token.
access_token = get_access_token()
header = {
    'Authorization': f'Bearer {access_token}'
}
payload = ENV["REPORT_REQUEST"]

# Request the instance generate our report.
# We'll get a dict with urls for files we can download.
report_links = requests.post(
    f"{ENV["HOST"]}open_api/api/v1/report/",
    headers=header,
    data=payload 
)

# Request the CSV version of the report from the instance.
report_csv = requests.get(
    report_links.json()["csv"],
    headers=header
)

# Convert the request text to a StringIO text stream.
csv_file = io.StringIO(report_csv.text)
# Read the CSV file.
csv_reader = csv.reader(csv_file)
# Print each row of the CSV file.
for row in csv_reader:
    print(", ".join(row))
# Close the file / text stream.
csv_file.close()