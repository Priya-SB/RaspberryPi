import RPi.GPIO as GPIO
import time 
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(27,GPIO.IN)    
count=0
state=0
try:
	while True:
		print(" Finding Objects ")
		print(count)
		state=GPIO.input(27)
		if(state==0):
			count+=1
		file=open('abc.txt','w')
		file.write(" Final Count : " + str(count))
		file.close()
		time.sleep(3)
	
except KeyboardInterrupt:
	GPIO.cleanup()
