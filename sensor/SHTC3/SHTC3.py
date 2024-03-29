# This sensor needs the BMP280 library.
# sudo pip3 install adafruit-circuitpython-bmp280

import board
import busio
import digitalio
import adafruit_shtc3
import time

from sensor.Sensor import Sensor
from sensor.SensorDevice import SensorDevice

from .SHTC3_Temperature import SHTC3_Temperature
from .SHTC3_Humidity import SHTC3_Humidity

from ..I2CManager import I2CManager

class SHTC3(SensorDevice):
    def __init__(self):
        i2c_manager = I2CManager()

        self.shtc3 = adafruit_shtc3.SHTC3(i2c_manager.get_i2c())
        
        self.sensors = [
            SHTC3_Temperature(self),
            SHTC3_Humidity(self)
        ]
        

    def get_name(self):
        return "SHTC3"

    def get_sensors(self):
        return self.sensors	
