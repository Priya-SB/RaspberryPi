import RPi.GPIO as gp
import time
gp.setmode(gp.BOARD)
cntr_pin=[8,10,12,16]

for pin in cntr_pin:
	gp.setup(pin,gp.OUT)
	gp.output(pin,0)
	
def run(x):
	half_seq=[
		[1,0,0,0],
		[1,1,0,0],
		[0,1,0,0],
		[0,1,1,0],
		[0,0,1,0],
		[0,0,1,1],
		[0,0,0,1],
		[1,0,0,1]
	]
	print("Start..")
	if(x==1):	
		for i in range(512):
			for halfstep in range(8):
				for pin in range(4):
					gp.output(cntr_pin[pin],half_seq[halfstep][pin])
				time.sleep(0.01)
	else:
		for i in range(512):
			for halfstep in range(7,0,-1):
				for pin in range(4):
					gp.output(cntr_pin[pin],half_seq[halfstep][pin])
				time.sleep(0.01)
def fullstep():
	full_seq=[
		[1,0,0,0],
		[0,1,0,0],
		[0,0,1,0],
		[0,0,0,1]
	]
	for i in range(512):
		for halfstep in range(4):
			for pin in range(4):
				gp.output(cntr_pin[pin],full_seq[halfstep][pin])
				time.sleep(0.01)
			time.sleep(0.001)

try:
	inp=input("Enter choice: \n1)Forward, 2)Backward, 3)Fullstep, 4)Stop")
	while(inp!=0):			
		if(inp==1):
			run(1)
		elif(inp==2):
			run(2)
		elif(inp==3):
			fullstep()
		else:
			for pin in cntr_pin:
				gp.output(pin,0)
		inp=input("Enter choice: \n1)Forward, 2)Backward, 3)Fullstep, 4)Stop")
finally:
		gp.cleanup()	

