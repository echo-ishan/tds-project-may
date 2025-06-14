
# /// script
# requires-python = ">=3.11"
# dependencies = [
#   "requests<3",
#   "rich",
# ]
# ///


#https://discourse.onlinedegree.iitm.ac.in/directory_items.json?order=likes_received&page=1&period=all&user_field_ids=1
import requests
import json
response = requests.get('https://discourse.onlinedegree.iitm.ac.in/directory_items.json?order=likes_received&page=1&period=all&user_field_ids=1')

with open('discourse.json',  'w') as file:
    json.dump(response.json(), file, indent=4)
