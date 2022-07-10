import random 

from sensor.Sensor import Sensor
from sensor.SensorDevice import SensorDevice

from .TestSensor import TestSensor
from .TestSensor2 import TestSensor2

class TestDevice(SensorDevice):
    def __init__(self):
        self.sensors = [
            TestSensor(self),
            TestSensor2(self)
        ]
        pass

    def get_name(self):
        return "TestDevice"

    def get_sensors(self):
        return self.sensors	
