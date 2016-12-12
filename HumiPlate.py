#!/usr/bin/python
# Example using a character LCD plate.
import time

import Adafruit_CharLCD as LCD

import Adafruit_DHT as dht

# Initialize the LCD using the pins
PLATE = LCD.Adafruit_CharLCDPlate()

#GPIO setup
GPIO_PORT = 3

SECONDS_TO_SLEEP = 3

PLATE.set_color(0, 0.0, 0.5)

print('Starting data query, every' + SECONDS_TO_SLEEP + 'seconds')
while True:
    H, T = dht.read_retry(dht.DHT22, GPIO_PORT)
    PLATE.clear()
    PLATE.message('Temp={0:0.1f}*C'.format(T))

    PLATE.set_cursor(0, 1)
    PLATE.message('Humidity={0:0.1f}%'.format(H))

    print('Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(T, H))
    time.sleep(SECONDS_TO_SLEEP)



