import requests
import json
import hashlib


def get_leads():

    encode = hashlib.md5("Demo".encode('utf-8'))
    password = encode.hexdigest()

    # API URL
    url = "https://suitecrmdemo.dtbc.eu/service/v4/rest.php"

    # Login parameters
    login_parameters = {
        "user_auth": {
            "user_name": "Demo",
            "password": password,
            "version": "1"
        },
        "application_name": "RestTest",
        "name_value_list": [],
    }

    # Convert login parameters to JSON
    login_parameters_json = json.dumps(login_parameters)

    # Create login data payload
    login_data = {
        "method": "login",
        "input_type": "json",
        "response_type": "json",
        "rest_data": login_parameters_json,
    }

    # Send login request
    response = requests.post(url, data=login_data)
    res_json = response.json()

    # Get session id from login response
    session_id = res_json['id']

    # Data payload for get_entry_list method
    get_entry_list_parameters = {
        "session": session_id,
        "module_name": "Leads",
        "query": "",
        "order_by": "",
        "offset": 0,  # For pagination in a future
        "select_fields": [
            'phone_work',
            'first_name',
            'last_name'
        ],
        "link_name_to_fields_array": [],
        "max_results": 10,
        "deleted": 0,  # Don't get deleted records
    }

    # Convert the parameters to JSON
    get_entry_list_parameters_json = json.dumps(get_entry_list_parameters)

    # Create get_entry_list data payload
    get_entry_list_data = {
        "method": "get_entry_list",
        "input_type": "json",
        "response_type": "json",
        "rest_data": get_entry_list_parameters_json,
    }

    response = requests.post(url, data=get_entry_list_data)
    raw_data = response.json().get('entry_list')

    # Saving data

    for data in raw_data:
        phone_work = data.get('name_value_list').get('phone_work').get('value')
        first_name = data.get('name_value_list').get('first_name').get('value')
        last_name = data.get('name_value_list').get('last_name').get('value')

        headers = {
            'accept': 'application/json',
            'Content-Type': 'application/json',
        }

        json_data = {
            'phone_work': phone_work,
            'first_name': first_name,
            'last_name': last_name,
        }

        print(json_data)

        requests.post('http://127.0.0.1:8000/leads/', headers=headers, json=json_data)

get_leads()