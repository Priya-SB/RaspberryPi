import RPi.GPIO as gp
from time import sleep

gp.setmode(gp.BOARD)

in1= 8
in2= 10
gp.setup(in1,gp.OUT)
gp.setup(in2,gp.OUT)

gp.output(in1,gp.LOW)
gp.output(in2,gp.LOW)

try:
	while True:
		gp.output(in1,gp.LOW)
		gp.output(in2,gp.HIGH)
finally:
	gp.cleanup()

