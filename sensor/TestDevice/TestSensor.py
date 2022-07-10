import random 

from sensor.Sensor import Sensor

class TestSensor(Sensor):
    def __init__(self, device):
        self.device = device

    def name(self) -> str:
        '''The sensor's (unique) name.'''
        return 'TestSensor 1'

    def device(self):
        '''The device this sensor belongs to.'''
        return self.device
    
    def preferred_measure_interval(self) -> int:
        '''The preferred interval for doing measurments, in seconds.'''
        return 2

    def unit(self) -> str:
        '''The unit of this sensor's measurements.'''
        return '°C'
    
    def get_measurement(self) -> float:
        '''Perform a measurements.'''
        return 15 + round(random.random() * 10, 2)