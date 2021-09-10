import requests
import json
import sys
import time

header = {"Authorization": "<your token>"}

response = requests.get("https://api.switch-bot.com/v1.0/devices", headers=header)
devices  = json.loads(response.text)

light_id  = [device["deviceId"] for device in devices['body']['infraredRemoteList'] if "<your light name>" == device['deviceName']]

down_body = {
   "command" : "brightnessDown",
   "parameter" : "default",
   "comandType": "command"
}

up_body = {
   "command" : "brightnessUp",
   "parameter" : "default",
   "comandType": "command"
}

off_body = {
   "command" : "TurnOff",
   "parameter" : "default",
   "comandType": "command"
}

on_body = {
   "command" : "TurnOn",
   "parameter" : "default",
   "comandType": "command"
}

url = "https://api.switch-bot.com/v1.0/devices/" + light_id[0] + "/commands"

# ライトをだんだん暗くする
for i in range(20):
   requests.post(url, headers=header, data=json.dumps(down_body))
   time.sleep(2)
   
# ライトをだんだん明るくする   
for i in range(20):
   requests.post(url, headers=header, data=json.dumps(up_body))
   time.sleep(2)

# ライトを消す
requests.post(url, headers=header, data=json.dumps(off_body))
time.sleep(5)

# ライトをつける
requests.post(url, headers=header, data=json.dumps(on_body))
time.sleep(5)
