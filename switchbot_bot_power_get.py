import json
import requests

# Please get your access token via switchbot app
header = {"Authorization": "<your access token>"}

# Get all device information in your switchbot hub
response = requests.get("https://api.switch-bot.com/v1.0/devices", headers=header)
devices  = json.loads(response.text)

# Get switchbot bot "deviceId" in all device information
bots_id  = [device["deviceId"] for device in devices['body']['deviceList'] if "Bot" == device["deviceType"]]

# Get all switchbot bot power state and output on your display
for bot_id in bots_id:
  
 response = requests.get("https://api.switch-bot.com/v1.0/devices/" + bot_id + "/status", headers=header)
 bot      = json.loads(response.text)
 power    = bot['body']['power']

 print("bot id (" + bot_id + ") power : " + power)
