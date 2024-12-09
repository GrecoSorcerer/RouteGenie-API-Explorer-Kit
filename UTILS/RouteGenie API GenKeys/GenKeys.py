#!/usr/bin/env python
# -*- coding: utf-8 -*-

### Salvatore L Greco <salvatore@isi-technology.com>
### 7/26/2023
### ISI Technology/RouteGenie

from secrets import token_hex
"""Generate API Keys for RouteGenie API Integrations.
    Used to generate keys for the RouteGenie API for 
    clients integrating 3rd Party software and brokers 
    integrating with RouteGenie."""

def main():
    """Print new Client Sectret and Client ID to the command line.
        May be called from CLI or will be called 
        at run time if saved to a .py file as a script."""
    # Char length of keys / 2
    CLIENT_ID_BYTES = 20
    CLINET_SECRET_BYTES = 50
    
    # Generate the new credentials
    CID = token_hex(CLIENT_ID_BYTES)
    CS  = token_hex(CLINET_SECRET_BYTES)
    
    # Print the new credentials
    print('')
    print(f'New Client Secret [ {CS} ]')
    print(f'New Client ID [ {CID} ]')

# Run Script
if __name__ == '__main__':
    """When called from a """
    main()
