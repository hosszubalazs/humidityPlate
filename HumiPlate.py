#!/usr/bin/python
# Python 3

# Example using a character LCD plate.
import time

#FIXME libraries are not yet committed
import Adafruit_GPIO.Adafruit_CharLCD as LCD

import Adafruit_DHT as dht

# Initialize the LCD using the pins
PLATE = LCD.Adafruit_CharLCDPlate()

#GPIO setup
GPIO_PORT = 3

SECONDS_TO_SLEEP = 4

PLATE.set_color(0, 0.0, 0.5)

print('Starting data query, every' + SECONDS_TO_SLEEP + 'seconds')
while True:
    H, T = dht.read_retry(dht.DHT22, GPIO_PORT)
    PLATE.clear()
    TEMP_MSG = 'Temp={0:0.1f}*C'.format(T)
    PLATE.message(TEMP_MSG)

    PLATE.set_cursor(0, 1)
    HUM_MSG = 'Humidity={0:0.1f}%'.format(H)
    PLATE.message(HUM_MSG)

    print(TEMP_MSG)
    print(HUM_MSG)
    time.sleep(SECONDS_TO_SLEEP)
