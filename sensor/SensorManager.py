import time
import logging

from sensor.Sensor import Sensor
from sensor.SensorDevice import SensorDevice
from mqtt.MQTTManager import MQTTManager
from util.IntervalTimer import IntervalTimer


class SensorManager:
    '''
    Sensor manager that allows to add sensors, calling their get_measurement() 
    function in their preferred time interval. 
    '''
    def __init__(self, config):
        self.devices = []
        self.timers = []
        self.mqtt = MQTTManager(config) # todo: move mqtt manager out of the sensor manager

    def add_sensor_device(self, sensor_device) -> None:

        # add the device to the sensor list
        self.devices.append(sensor_device)

        # create a new IntervalTimer for each sensor of this device
        for sensor in sensor_device.get_sensors():
            sensor_timer = IntervalTimer(
                sensor.preferred_measure_interval(),  # timer interval
                self.do_measurment,                   # callback for timer             
                sensor                                # argument used for calling the callback
            )
        
            # store it in the timers list
            self.timers.append(sensor_timer)
        
            logging.warning('[add_sensor] added the sensor {} with unit {} and a measure interval of {} seconds, belonging to device {} to the SensorManager'.format(sensor.name(), sensor.unit(), sensor.preferred_measure_interval(), sensor.device().name()))
        
    def do_measurment(self, sensor):
        measured_value = sensor.get_measurement()
        print('[do_measurment] self: {0}. sensor: {1} ===> measured: {2}'.format(self, sensor.name(), measured_value))
        
        # send the sensor name, the measured value and the measuring time in milliseconds since epoch
        self.mqtt.send_object({ 'name': sensor.name(), 'value': measured_value, 'device': sensor.device().name(), 'send_time': time.time_ns() // 1_000_000 })