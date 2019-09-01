import RPi.GPIO as GPIO
import httplib,urllib
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(15,GPIO.OUT)
GPIO.setup(14,GPIO.IN)
Pin_Trigger=15
Pin_Echo=14
key = 'ZUBX6DTLLCXKAZXL'
try:
	while True:
		#print("Calculating Distance")
		GPIO.output(Pin_Trigger,GPIO.HIGH)
		time.sleep(0.00001)
		GPIO.output(Pin_Trigger,GPIO.LOW)
		while GPIO.input(Pin_Echo)==0 :
			start_time=time.time()
		while(GPIO.input(Pin_Echo)==1):
			end_time=time.time()
			duration_time=end_time-start_time
			distance=round(duration_time*17150,2)
			print'Distance is: ',distance
			time.sleep(1)
		param=urllib.urlencode({'field1':distance,'key':key})
		headers={"Content-typZZe":"application/x-www-form-urlencoded","Accept":"text/plain"}
		conn=httplib.HTTPConnection("api.thingspeak.com:80")
		
		conn.request("POST","/update",param,headers)
		response=conn.getresponse()
		print response.status , response.reason
		data=response.read()
		conn.close()
		
		
except KeyboardInterrupt:
	GPIO.cleanup()
	print (' Connection failed ')
