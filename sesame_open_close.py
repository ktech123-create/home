import requests
import json
import time
import argparse
import sys

parser = argparse.ArgumentParser(description='This script can open or close to your sesame lock.')
parser.add_argument('--state', help='lock or unlock')

args = parser.parse_args()

sesame_list_url = 'https://api.candyhouse.co/public/sesames'
sesame_cont_url = 'https://api.candyhouse.co/public/sesame/{0}'

api_token = '<your_token>'
header    = {'Authorization': api_token}

response = requests.get(sesame_list_url, headers=header)

for devices in json.loads(response.text):
   if args.state == 'lock':
       body = json.dumps({"command" : "lock"})
   elif args.state == 'unlock':
       body = json.dumps({"command" : "unlock"})
   else:
       sys.exit()
   response = requests.post(sesame_cont_url.format(devices["device_id"]), headers=header, data=body)
   time.sleep(30)
