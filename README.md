#
# RouteGenie-API-Explorer-Kit
Explore the RouteGenie API with this Explorer Kit! Your go-to resource for 
developers getting started with RouteGenie's API. Inside, you'll discover 
a range of tests, examples, and tools for understanding the API's capabilities
and constraints. The goal is for this collection to serve as your 
comprehensive toolkit for experimentation and learning.

Link to RouteGenie's [Open API Documentation](https://documenter.getpostman.com/view/26777355/2s93RZLpYS#917a28e4-8ec6-454b-8dd0-9f3b58773c1d)

## 
## DEMOS
Step-by-step examples of using the API. Typically Jupyter notebooks. These 
demos assume you have some way to run python notebooks.

### Create and Query Jupyter Notebook
Using this notebook you will see how to use the RouteGenie API in python using 'requests'. This demo assumes you have applied the requirments to your system
or python virtual enviorment.

This demo provides an example work flow to:

1. #### Set the Execution Constants and Helper Function
   1. Set ENV variables
   1. Set a TESTID
   1. Set some constants for the Demo
   1. Set a help function
1. #### Request Authentication Access Code
1. #### Get Trip Types
1. #### Construct Modes dictionary
1. #### Request an Order
1. #### Query the Order

## TESTS
Use these tests to incrementally explore the behavior of the API.

The tests as written expect an enviorment file in the TESTS directory

`./TESTS/enviornment.json`

```json
{
    "SECRET":"your-secret",
    "CLIENTID":"your-clientid",
    "HOST":"https://your-subdomain.routegenie.com:8000/",
    ...
}
```

### authTest.py
This example test will:
- load the enviornment file
- make a request to `{HOST}oauth2/token/` using CLIENTID and SECRET
- return the status code and text of this request's response
- try to use the token to make request, return the status

### createOrderTest.py

This example test will require a TESTRIDE in your enviornment.json file

```json
    ...
    "TESTRIDE":{
        "ride_id": "TESTID001",
        "client_internal_id": 1,
        "custom_trip_type": 1,
        "initial_time": "10/01/2025 16:30",
        "pick_up_address":"241 Main St Buffalo NY",
        "drop_off_address":"490 Delaware Ave Buffalo NY",
        "payment_method":1
    }
```

This test will:
 
- use authTest.py to request an access token
   - print the status and response as text
- request an order using the properties added to the enviorment.json file
   - print the order information if it was successfully created.
- return the order details of the created ride, if successful


### accessOrderTest.py

This test will:

- use authTest.py to request an access token
   - print the status and response as text
- query the order of with ride_id
   - return the status code and either return the order details or failure reasons if possilbe. 
   
## UTILS
Tools and utilities that might come in handy!

### RouteGenie API GenKeys
If you don't aldready have some way of generating credentials, you can use 
this to generate API credentials.

#
# Installing Requirements
## Python requirements
Version: Python 3.10+

Either: 
- From the RGAPI explorer directory
    1. `pip install venv` Get the python virtual enviorment package
    1. `python3 -m venv .venv` Create a python virtual enviornment at the 
    current directory. This should be the RGAPI explorer directory
    1. Activate the virtual enviornment
        1. Mac: `source .venv/bin/activate`
        1. Linux: `source .venv/bin/activate`
        1. Windows: (Requires you change execution permission level) 
            - `.\venv\Scripts\activate.bat`
            - `.\venv\Scripts\Activate.ps1`
    1. `pip install -r requirements.txt`
- `pip install requests`

## Other
- Jupyter notebook
