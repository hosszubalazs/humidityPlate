#!/usr/bin/python
# Python 3
import Adafruit_DHT as dht
import Adafruit_GPIO.Adafruit_CharLCD as LCDLibrary
import time
import DHTDataParser


def init_lcd():
    lcd = LCDLibrary.Adafruit_CharLCDPlate()
    lcd.set_color(0, 0.0, 0.5)
    return lcd

def init_dht():
    DHT_GPIO = 4
    SECONDS_TO_SLEEP = 4
    return (DHT_GPIO, SECONDS_TO_SLEEP)


#If the script is run directly, let's start measurement
if __name__ == '__main__':
    DHT_GPIO, SECONDS_TO_SLEEP = init_dht()
    LCD = init_lcd()

    print('Starting data query, every ' + str(SECONDS_TO_SLEEP) + ' seconds')

    while True:
        H, T = dht.read_retry(dht.DHT22, DHT_GPIO)
        LCD.clear()
        LCD.message('Temperature='+ parseTemp(T))

        LCD.set_cursor(0, 1)
        LCD.message('Humidity='+parseHumidity(H))

        time.sleep(SECONDS_TO_SLEEP)
