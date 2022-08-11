import random 

from sensor.Sensor import Sensor

class SHTC3_Temperature(Sensor):
    def __init__(self, device):
        self._device = device

    def get_name(self) -> str:
        return 'Temperature'

    def get_device(self):
        return self._device
    
    def get_preferred_measure_interval(self) -> int:
        return 60

    def get_unit(self) -> str:
        return '°C'
    
    def get_measurement(self) -> float:
        return self._device.shtc3.temperature