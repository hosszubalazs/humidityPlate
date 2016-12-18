#!/usr/bin/python
# Python 3
import Adafruit_DHT as dht
import Adafruit_GPIO.Adafruit_CharLCD as LCD
import time
import DHTParser

def initLCD():
    PLATE = LCD.Adafruit_CharLCDPlate()
    PLATE.set_color(0, 0.0, 0.5)

def initDHT():
    #GPIO setup
    DHT_GPIO = 4
    SECONDS_TO_SLEEP = 4

def initInstrumentation():
    print("Let's initilaie instrumenation")
    initLCD
    initDHT


#If the script is run directly, let's start measurement
if __name__ == '__main__':
    print('Starting data query, every ' + str(SECONDS_TO_SLEEP) + ' seconds')
    initInstrumentation
    while True:
        H, T = dht.read_retry(dht.DHT22, DHT_GPIO)
        PLATE.clear()
        PLATE.message('Temperature='+ parseTemp(T))

        PLATE.set_cursor(0, 1)
        PLATE.message('Humidity='+parseHumidity(H))

        print(TEMP_MSG)
        print(HUM_MSG)
        time.sleep(SECONDS_TO_SLEEP)
