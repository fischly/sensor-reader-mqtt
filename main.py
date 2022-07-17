import json

from sensor.SensorManager import SensorManager
from sensor.TestDevice.TestDevice import TestDevice
from sensor.BMP280.BMP280 import BMP280

config = {}

with open('./config.json', 'r') as config_file:
    config = json.load(config_file)

sm = SensorManager(config)
# sm.add_sensor_device(TestDevice())
sm.add_sensor_device(BMP280())