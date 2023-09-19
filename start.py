# Ejecución de código al arranque del sistema

import Configuracion.I2C_LCD_driver as lcd
from time import *

mylcd = lcd.I2C_LCD_driver.lcd()

mylcd.lcd_display_string("Start: OK", 1)