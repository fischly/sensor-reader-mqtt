from abc import ABC, abstractmethod

from . import Sensor


class SensorDevice(ABC):
    '''
    Abstract base class for a device, that can include multiple sensors.
    For example, the BME280 is able to measure temperature and pressure.
    The SensorDevice class would represent the BME280, using two Sensor 
    classes that represent the temperature and pressure sensors.
    '''
    
    @abstractmethod
    def get_name(self) -> str:
        '''This device's name.'''
        pass
    
    @abstractmethod
    def get_sensors(self):
        '''A list of all sensors this device has.'''
        pass