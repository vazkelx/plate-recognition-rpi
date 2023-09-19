# Ejecución de código al arranque del sistema

import I2C_LCD_driver
from time import *

mylcd = I2C_LCD_driver.lcd()

mylcd.lcd_display_string("Start: OK", 1)