import sys
import Adafruit_DHT
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18,GPIO.OUT)
while True:
	humidity,temperature=Adafruit_DHT.read_retry(11,4)
	print 'temp:{0:0.01f}C humidity:{1:0.01f}%'.format(temperature,humidity)
	if (temperature==30.00):
		print("Led on")
		GPIO.output(18,1)
		time.sleep(1)
		print("Led off")
		GPIO.output(18,0)
		time.sleep(1)
    	
