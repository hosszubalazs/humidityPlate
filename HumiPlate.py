#!/usr/bin/python
# Example using a character LCD plate.
import time

import Adafruit_CharLCD as LCD

import Adafruit_DHT as dht

# Initialize the LCD using the pins
lcd = LCD.Adafruit_CharLCDPlate()

lcd.set_color(0, 0.0, 0.5)

print 'jon a parti'
while(True):
        h,t = dht.read_retry(dht.DHT22,4)
	lcd.clear()
	lcd.message('Temp={0:0.1f}*C'.format(t))
	
	lcd.set_cursor(0,1);
	lcd.message('Humidity={0:0.1f}%'.format(h))

        print 'Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(t, h)
        time.sleep(3)



