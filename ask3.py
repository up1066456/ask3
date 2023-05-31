import paho.mqtt.client as mqtt
import requests

client = mqtt.Client()
client.connect("broker.emqx.io", 1883, 60)



def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("topic/test")

def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))

url = 'http://example.com/api'
data = {'key1': 'value1', 'key2': 'value2'}
headers = {'Content-type': 'application/json'}

response = requests.post(url, json=data, headers=headers)

client.publish("topic/test", response.text)
client.on_connect = on_connect
client.on_message = on_message

client.connect("broker.emqx.io", 1883, 60)

client.loop_forever()