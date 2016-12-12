import time
import os
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

GPIO.setup(21, GPIO.IN)
while True:

	input = GPIO.input(21)
        print(input)

	time.sleep(1)

