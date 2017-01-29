#!/usr/bin/python
# Python 3

import time
import Adafruit_DHT as dht
import Adafruit_GPIO.Adafruit_CharLCD as LCDLibrary
import src.DHTDataParser as dataParser
import src.constants as c
import src.LCDHelper as lcdHelper

def init_lcd():
    lcd = LCDLibrary.Adafruit_CharLCDPlate()
    lcd.set_color(c.LCD_COLD_BLUE[0], c.LCD_COLD_BLUE[1], c.LCD_COLD_BLUE[2])
    return lcd

#If the script is run directly, let's start measurement
if __name__ == '__main__':
    LCD = init_lcd()

    print('Starting data query, every ' + str(c.SECONDS_TO_SLEEP) + ' seconds')

    while True:
        H, T = dht.read_retry(dht.DHT22, c.DHT_GPIO)
        H_MSG = 'Humi.='+dataParser.parseHumidity(H)
        T_MSG = 'Temp.='+ dataParser.parseTemp(T)

        LCD.clear()
        LCD.message(T_MSG)
        print(T_MSG)

        LCD.set_cursor(0, 1)
        LCD.message(H_MSG)
        print(H_MSG)

        targetColor = lcdHelper.map_heat_to_bgcolor(T)
        LCD.set_color(targetColor[0], targetColor[1], targetColor[2])
        time.sleep(c.SECONDS_TO_SLEEP)
