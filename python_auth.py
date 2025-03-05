#! /usr/bin/python3

import requests
import os
import passwords

user = passwords.user
password = passwords.password

print(requests.get("http://172.17.0.2/basic-auth/russ/test", auth=(user, password)).text)

