from abc import ABC, abstractmethod

# from . import SensorDevice


class Sensor(ABC):
    '''Abstract base class that can be used to implement custom sensor logic.'''
    
    @abstractmethod
    def get_name(self) -> str:
        '''The sensor's (unique) name.'''
        pass

    @abstractmethod
    def get_device(self):
        '''The device this sensor belongs to.'''
        pass
    
    @abstractmethod
    def get_preferred_measure_interval(self) -> int:
        '''The preferred interval for doing measurments, in seconds.'''
        pass

    @abstractmethod
    def get_unit(self) -> str:
        '''The unit of this sensor's measurements.'''
        pass
    
    @abstractmethod
    def get_measurement(self) -> float:
        '''Perform a measurements.'''
        pass