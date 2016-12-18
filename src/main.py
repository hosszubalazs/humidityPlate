#!/usr/bin/python
# Python 3
import Adafruit_DHT.Adafruit_DHT as dht
import Adafruit_GPIO.Adafruit_CharLCD as LCDLibrary
import time
import DHTDataParser as dataParser
import constants as c
import LCDHelper as lcdHelper

def init_lcd():
    lcd = LCDLibrary.Adafruit_CharLCDPlate()
    lcd.set_color(c.LCD_COLD_BLUE)
    return lcd

#If the script is run directly, let's start measurement
if __name__ == '__main__':
    LCD = lcdHelper.init_lcd()

    print('Starting data query, every ' + str(c.SECONDS_TO_SLEEP) + ' seconds')

    while True:
        H, T = dht.read_retry(dht.DHT22, c.DHT_GPIO)
        H_MSG = 'Humidity='+dataParser.parseHumidity(H)
        T_MSG = 'Temperature='+ dataParser.parseTemp(T)

        LCD.clear()
        LCD.message('Temperature='+ T_MSG)
        print(T_MSG)

        LCD.set_cursor(0, 1)
        LCD.message(H_MSG)
        print(H_MSG)

        LCD.set_color(lcdHelper.map_heat_to_bgcolor(T))
        time.sleep(c.SECONDS_TO_SLEEP)
