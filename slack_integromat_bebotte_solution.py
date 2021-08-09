import time
import json
import paho.mqtt.client as mqtt

# slack and webhook is channel and resource names, respectivity.
# if you use different names, you need to change the bellow names
def on_connect(client, data, flags, rc):
 client.subscribe("slack/webhook", 1)

def on_message(client, data, msg):
  message = json.loads((msg.payload).decode('utf-8'))
  message = message['data'].replace('#','')
  print(message)

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.tls_set("mqtt.beebotte.com.pem")

# your token is token obrained by beebotte
client.username_pw_set("token:<your token>")
client.connect("mqtt.beebotte.com", 8883, 60)

client.loop_forever()
