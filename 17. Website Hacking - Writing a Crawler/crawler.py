#!/usr/bin/env python

import requests

url = "10.0.0.6"
try:
    get_response = requests.get("http://" + url)
    print(get_response)
except requests.exceptions.ConnectionError:
    pass