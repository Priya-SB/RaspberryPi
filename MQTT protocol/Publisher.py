import RPi.GPIO as GPIO
import time
import sys
import paho.mqtt.client as paho
GPIO.setwarnings(False)
broker="broker.hivemq.com"
#broker="iot.eclipse.org"
#broker="test.mosquitto.org"

trigger = 10
echo = 20

def on_connect(client2,userdata,flags,rc):
    print ("Publisher connected with result code "+str(rc))
    time.sleep(2)

client2=paho.Client("client-001")
print("---Connecting to broker ",broker)
client2.connect(broker)
client2.on_connect=on_connect
client2.loop_start()
try :
    while True:
            GPIO.setmode(GPIO.BCM)
            GPIO.setup(trigger,GPIO.OUT)
            GPIO.setup(echo,GPIO.IN)
            GPIO.output(trigger,0)
            time.sleep(1)
            GPIO.output(trigger,1)
            time.sleep(0.00001)
            GPIO.output(trigger,0)
            while GPIO.input(echo) ==0:
                start = time.time()
            while GPIO.input(echo) ==1:
                end = time.time()
                pulse = end - start
                dist = round(pulse * 17150,2)
                print ('Distance = ',dist,' cm')
                print ("Publishing....")
                client2.publish("mit/distance",str(dist))
                time.sleep(10)
except KeyboardInterrupt:
    client2.loop_stop()
    client2.disconnect()
finally :    
    GPIO.cleanup()   
 
'''pi@raspberrypi:~/Desktop $ python3 ppp.py
---Connecting to broker  broker.hivemq.com
Publisher connected with result code 0
Distance =  0.24  cm
Publishing....
Publisher connected with result code 0
Publisher connected with result code 0
Publisher connected with result code 0
Distance =  0.21  cm
Publishing....
Publisher connected with result code 0
Publisher connected with result code 0
Publisher connected with result code 0
Distance =  0.22  cm
Publishing....
Distance =  0.24  cm
Publishing....
Distance =  0.22  cm
Publishing....
Distance =  0.22  cm
Publishing....
Distance =  0.27  cm
Publishing....
'''   

