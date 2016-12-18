#!/usr/bin/python
# Python 3

def parseTemp(value):
    return parseWithUnit(value,"*C")

def parseHumidity(value):
    return parseWithUnit(value,"*%")

def parseWithUnit(value, unit):
    return '{0:0.1f}'.format(value)+unit


def initInstrumentation():
    import Adafruit_GPIO.Adafruit_CharLCD as LCD
    import Adafruit_DHT as dht
    print("Let's initilaie instrumenation")
    # Initialize the LCD using the pins
    PLATE = LCD.Adafruit_CharLCDPlate()
    #GPIO setup
    GPIO_PORT = 4
    SECONDS_TO_SLEEP = 4
    PLATE.set_color(0, 0.0, 0.5)

#If the script is run directly, let's start measurement
if __name__ == '__main__':
    import time
    print('Starting data query, every ' + str(SECONDS_TO_SLEEP) + ' seconds')
    initInstrumentation
    while True:
        H, T = dht.read_retry(dht.DHT22, GPIO_PORT)
        PLATE.clear()
        TEMP_MSG = 'Temperature='+ parseTemp(T)
        PLATE.message(TEMP_MSG)

        PLATE.set_cursor(0, 1)
        HUM_MSG = 'Humidity='+parseHumidity(H)
        PLATE.message(HUM_MSG)

        print(TEMP_MSG)
        print(HUM_MSG)
        time.sleep(SECONDS_TO_SLEEP)
