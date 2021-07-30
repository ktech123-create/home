import requests
import json
import sys

# on or off
# on is power on / off is power off
power =  sys.argv[0]

# Please get your access token via switchbot app
header = {"Authorization": "<your access token>"}

# Get all device information in your switchbot hub
response = requests.get("https://api.switch-bot.com/v1.0/devices", headers=header)
devices  = json.loads(response.text)

# Get deviceId for airconditioner
# 'your airconditioner name' is your airconditioner name in switchbot hub mini
aircon_id  = [device["deviceId"] for device in devices['body']['infraredRemoteList'] if <your airconditioner name> == device['deviceName']]

# create API body 
# suport cool state 
body = {
  "command" : "setAll",
  "parameter" : "26,2,2,{0}".format(power),
  "comandType": "command"
}

# call airconditioner api 
url = "https://api.switch-bot.com/v1.0/devices/" + aircon_id[0] + "/commands"
requests.post(url, headers=header, data=json.dumps(body))
