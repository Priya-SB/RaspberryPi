import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

PinTrigger = 3
PinEcho = 5
LED = 7

GPIO.setup(PinTrigger, GPIO.OUT)
GPIO.setup(PinEcho, GPIO.IN)
GPIO.setup(LED, GPIO.OUT)

try:
    while 1:
        GPIO.output(PinTrigger, GPIO.LOW)
        GPIO.output(LED, GPIO.LOW)
        print("Waiting for sensor to configure...")
        time.sleep(2)
        print('Calculating the distance...')
        GPIO.output(PinTrigger, GPIO.HIGH)
        time.sleep(0.1)
        GPIO.output(PinTrigger, GPIO.LOW)
        while GPIO.input(PinEcho) == 0:
            start_time = time.time()
        while GPIO.input(PinEcho) == 1:
            end_time = time.time()
        duration = end_time - start_time
        distance = round(duration * 17150, 2)
        print('Distance =', distance, 'cm')
        if distance > 20:
            GPIO.output(LED, GPIO.HIGH)
            time.sleep(2)
finally:
    GPIO.cleanup()
