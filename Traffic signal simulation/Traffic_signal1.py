import RPi.GPIO as gp
from time import sleep

gp.setmode(gp.BOARD)

in1= 8
in2= 10
gr = 40
yw = 38
rd = 36
gp.setup(in1,gp.OUT)
gp.setup(in2,gp.OUT)
gp.setup(gr,gp.OUT)
gp.setup(rd,gp.OUT)
gp.setup(yw,gp.OUT)
#p = GPIO.PWM(in1,50)

gp.output(in1,gp.LOW)
gp.output(in2,gp.LOW)
gp.output(gr,gp.LOW)
gp.output(rd,gp.LOW)
gp.output(yw,gp.LOW)

try:
	while True:

		signal = input("Choose a signal : ")
		if signal == 1:
			gp.output(rd,gp.HIGH)
			sleep(1)
			gp.output(in1,gp.LOW)
			gp.output(in2,gp.LOW)
			gp.output(rd,gp.LOW)
		elif signal == 2:
			gp.output(yw,gp.HIGH)
			sleep(1)
			gp.output(in1,gp.LOW)
			gp.output(in2,gp.HIGH)
			gp.output(yw,gp.LOW)
		elif signal == 3:
			gp.output(gr,gp.HIGH)
			sleep(1)
			gp.output(in1,gp.HIGH)
			gp.output(in2,gp.LOW)
			gp.output(gr,gp.LOW)
finally:
	gp.cleanup()
