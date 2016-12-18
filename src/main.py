#!/usr/bin/python
# Python 3
import Adafruit_DHT.Adafruit_DHT as dht
import Adafruit_GPIO.Adafruit_CharLCD as LCDLibrary
import time
import DHTDataParser as dataParser


def init_lcd():
    lcd = LCDLibrary.Adafruit_CharLCDPlate()
    lcd.set_color(0, 0.0, 0.5)
    return lcd

def init_dht():
    dht_gpio = 4
    seconds_to_sleep = 4
    return (dht_gpio, seconds_to_sleep)


#If the script is run directly, let's start measurement
if __name__ == '__main__':
    DHT_GPIO, SECONDS_TO_SLEEP = init_dht()
    LCD = init_lcd()

    print('Starting data query, every ' + str(SECONDS_TO_SLEEP) + ' seconds')

    while True:
        H, T = dht.read_retry(dht.DHT22, DHT_GPIO)
        H_MSG = 'Humidity='+dataParser.parseHumidity(H)
        T_MSG = 'Temperature='+ dataParser.parseTemp(T)

        LCD.clear()
        LCD.message('Temperature='+ T_MSG)
        print(T_MSG)

        LCD.set_cursor(0, 1)
        LCD.message(H_MSG)
        print(H_MSG)

        time.sleep(SECONDS_TO_SLEEP)
