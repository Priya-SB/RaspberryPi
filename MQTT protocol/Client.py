import paho.mqtt.client as mqtt
import time

#MQTT_SERVER="test.mosquitto.org"
MQTT_SERVER="broker.hivemq.com"
MQTT_TOPIC="mit/distance"

def on_connect(client,userdata,flags,rc):
    print("Connected with result code"+str(rc))
    client.subscribe(MQTT_TOPIC)
    
def on_message(client,userdata,msg):
    print(msg.topic+' '+str(msg.payload))

client=mqtt.Client()
client.on_connect=on_connect
client.on_message=on_message
client.connect(MQTT_SERVER,1883,60)
client.loop_start()
try:
    while True:
        time.sleep(2)
except KeyboardInterrupt:
    client2.loop_stop()
    client2.disconnect()       
    
'''========================= RESTART =========================
>>> %Run Client.py
Connected with result code0
mit/distance b'0.22'
mit/distance b'0.24'''    