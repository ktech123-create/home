import requests
import json
import sys

# Please get your access token via switchbot app
header = {"Authorization": "<your access token>"}

# Get all device information in your switchbot hub
response = requests.get("https://api.switch-bot.com/v1.0/devices", headers=header)
devices  = json.loads(response.text)

# Get deviceId for hygrometer of "your hygrometer device name" in all device information 
device_id = [device['deviceId'] for device in devices['body']['deviceList'] if <your hygrometer device name> in device['deviceName']]

# call hygrometer state via switchbot api
url = "https://api.switch-bot.com/v1.0/devices/" + device_id[0] + '/status'
response = requests.get(url, headers=header)

print(response.text)
