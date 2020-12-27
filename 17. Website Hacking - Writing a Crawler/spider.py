#!/usr/bin/env python

import requests
import re

def request(url):
    try:
        return requests.get("http://" + url)
    except requests.exceptions.ConnectionError:
        pass

# target_url = "http://10.0.2.10/mutillidae/"
target_url = "10.0.0.5/admin"

response = request(target_url)
href_links = re.findall('(?:href=")(.*?)"', str(response.content))
print(href_links)
