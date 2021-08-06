import requests
import json

hue_url = 'http://<your hue bridge ip>/api/<your username>/lights'

request  = requests.get(hue_url)
response = json.loads(request.text)

for number in response.keys():
   if '<your device name>' == response[number]['name']:

       light_url = hue_url + '/' + str(number) + '/state'
       body      = json.dumps({"on":False})

       requests.put(light_url, data=body)
