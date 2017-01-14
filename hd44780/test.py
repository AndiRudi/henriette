import lcddriver
from time import *

lcd = lcddriver.lcd()
lcd.lcd_clear()

lcd.lcd_display_string("Hallo", 1)
lcd.lcd_display_string("Tina", 2)
