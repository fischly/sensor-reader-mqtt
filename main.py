import json

from sensor.SensorManager import SensorManager
from sensor.TestSensor import TestSensor

config = {}

with open('./config.json', 'r') as config_file:
    config = json.load(config_file)

sm = SensorManager(config)
sm.add_sensor(TestSensor())