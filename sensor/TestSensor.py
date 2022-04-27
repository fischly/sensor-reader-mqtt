from sensor.Sensor import Sensor

class TestSensor(Sensor):
    def name(self):
        return "TestSensor"
    
    def preferred_measure_interval(self) -> int:
        return 3
    
    def get_measurement(self) -> float:
        return 13.37