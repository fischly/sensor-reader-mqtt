import random 

from sensor.Sensor import Sensor

class SHTC3_Humidity(Sensor):
    def __init__(self, device):
        self._device = device

    def get_name(self) -> str:
        return 'Humidity'

    def get_device(self):
        return self._device
    
    def get_preferred_measure_interval(self) -> int:
        return 60

    def get_unit(self) -> str:
        return '%'
    
    def get_measurement(self) -> float:
        return self._device.shtc3.relative_humidity
