# INSTALACIÓN

## Configuración de la SD
Para cargar el sistema operativo en la SD se utiliza el programa "Raspberry Pi imager". Aquí podemos configurar:
 * Usuario: adria
 * Contraseña: ***
 * Hostname: rpiext.local
 * Conexión wireless: O2_HOME
 * etc.

## Primera conexión mediante SSH
Para acceder por primera vez no es necesario insertar la ip, con el hostname nos sirve. Usamos el usario por defecto creado en la instalacióin de la SD.

### Actualizamos paquetes:
```bash
sudo apt-get update
```
```bash
sudo apt-get upgrade
```

### Configurar raspberry pi
```bash
sudo raspi-config
```
```
3 Interface Options 
     I1 Legacy Camera Enable/disable legacy camera support
     I5 I2C           Enable/disable automatic loading of I2C kernel module
```
```
sudo reboot
```

### Probar cámara
```bash
mkdir test
cd test
raspistill -o test.jpg
raspivid -o test.h264 -t 20000
```
Streaming con librería:
python3 rpi_camera_surveillance_system.py

### Probar display
```bash
sudo apt-get install i2c-tools
```
Instalamos la librería 'I2C_LCD_driver.py' y ejecutamos una prueba:
```python
import I2C_LCD_driver
from time import *

mylcd = I2C_LCD_driver.lcd()

mylcd.lcd_display_string("Hola mundo.", 1)
```