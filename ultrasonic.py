import RPi.GPIO as gp
import time
try:
	gp.setmode(gp.BCM)
	gp.setwarnings(False)
	gp.setup(14,gp.OUT)
	gp.setup(15,gp.IN)
	while True:
		time.sleep(1)
		gp.output(14,gp.HIGH)
		time.sleep(0.0001)
		gp.output(14,gp.LOW)
		while (gp.input(15)==0):	
			start=time.time()
		while (gp.input(15)==1):
			end_time=time.time()
			diff=end_time-start
			dist=round((diff*17500),2)
			print "Distance= ",dist,"cm"
finally:
	gp.cleanup() 