#!/usr/bin/env python

import requests
import re
import urllib.parse as urlparse

target_url = "http://10.0.2.10/mutillidae/"

def extract_links_from(url):
    response = requests.get(url)
    return re.findall('(?:href=")(.*?)"', str(response.content))

href_links = extract_links_from(target_url)
for link in href_links:
    link = urlparse.urljoin(target_url, link)
    if target_url in link:  # remove external links
        print(link) 
