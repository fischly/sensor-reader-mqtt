from abc import ABC, abstractmethod

class Sensor(ABC):
    '''Abstract base class that can be used to implement custom sensor logic.'''
    
    @abstractmethod
    def name(self) -> str:
        pass
    
    @abstractmethod
    def preferred_measure_interval(self) -> int:
        pass
    
    @abstractmethod
    def get_measurement(self) -> float:
        pass