import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18,GPIO.OUT)
while True:
    print("Led on")
    GPIO.output(18,1)
    time.sleep(1)
    print("Led off")
    GPIO.output(18,0)
    time.sleep(1)
    
