import random 

from sensor.Sensor import Sensor

class TestSensor(Sensor):
    def __init__(self, device):
        self._device = device

    def get_name(self) -> str:
        '''The sensor's (unique) name.'''
        return 'TestSensor 1'

    def get_device(self):
        '''The device this sensor belongs to.'''
        return self._device
    
    def get_preferred_measure_interval(self) -> int:
        '''The preferred interval for doing measurments, in seconds.'''
        return 2

    def get_unit(self) -> str:
        '''The unit of this sensor's measurements.'''
        return '°C'
    
    def get_measurement(self) -> float:
        '''Perform a measurements.'''
        return 15 + round(random.random() * 10, 2)