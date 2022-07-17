# This sensor needs the BMP280 library.
# sudo pip3 install adafruit-circuitpython-bmp280

import board
import busio
import digitalio
import adafruit_bmp280
import time

from sensor.Sensor import Sensor
from sensor.SensorDevice import SensorDevice

from .BMP280_Temperature import BMP280_Temperature
from .BMP280_Pressure import BMP280_Pressure

class BMP280(SensorDevice):
    def __init__(self):
        i2c = busio.I2C(board.SCL, board.SDA)

        self.bmp280 = adafruit_bmp280.Adafruit_BMP280_I2C(i2c, address=0x76)
        # self.bmp280.sea_level_pressure = 1025.9
        
        self.sensors = [
            BMP280_Temperature(self),
            BMP280_Pressure(self)
        ]
        

    def get_name(self):
        return "BMP280"

    def get_sensors(self):
        return self.sensors	
