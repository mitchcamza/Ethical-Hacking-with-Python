#!/usr/bin/env python

import requests

def request(url):
    try:
        return requests.get("http://" + url)
    except requests.exceptions.ConnectionError:
        pass

# target_url = "http://10.0.2.10/mutillidae/"
target_url = "10.0.0.5"

response = request(target_url)
print(response.content)
