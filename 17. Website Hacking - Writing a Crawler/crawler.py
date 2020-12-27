#!/usr/bin/env python

import requests

def request(url):
    try:
        return requests.get("http://" + url)
    except requests.exceptions.ConnectionError:
        pass

# target_url = "http://10.0.2.10/mutillidae/"
target_url = "google.co.za"

# with open("17. Website Hacking - Writing a Crawler/subdomains.txt", "r") as subdomains:
#     for line in subdomains:
#         word = line.strip()
#         test_url = word + "." + target_url
#         response = request(test_url)
#         if response:
#             print("[+] Discovered subdomain --> " + test_url)

results = open(f"17. Website Hacking - Writing a Crawler/{target_url}_results.txt", "w+")
with open("17. Website Hacking - Writing a Crawler/directories.txt", "r") as directories:
    for line in directories:
        word = line.strip()
        test_url = target_url + "/" + word
        response = request(test_url)
        if response:
            print("[+] Discovered URL --> " + test_url)
            results.write(str(test_url) + '\n')

results.close()