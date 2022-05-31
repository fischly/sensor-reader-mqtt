import time
import logging

from sensor.Sensor import Sensor
from mqtt.MQTTManager import MQTTManager
from util.IntervalTimer import IntervalTimer


class SensorManager:
    '''
    Sensor manager that allows to add sensors, calling their get_measurement() 
    function in their preferred time interval. 
    '''
    def __init__(self, config):
        self.timers = []
        self.mqtt = MQTTManager(config) # todo: move mqtt manager out of the sensor manager

    def add_sensor(self, sensor) -> None:
        # create a new IntervalTimer for the sensor to add
        sensor_timer = IntervalTimer(
            sensor.preferred_measure_interval(),  # timer interval
            self.do_measurment,                   # callback for timer             
            sensor                                # argument used for calling the callback
        )
        
        # store it in the timers list
        self.timers.append(sensor_timer)
        
        logging.warning('[add_sensor] added the sensor {} with a measure interval of {} seconds to the SensorManager'.format(sensor.name(), sensor.preferred_measure_interval()))
        
    def do_measurment(self, sensor):
        measured_value = sensor.get_measurement()
        print('[do_measurment] self: {0}. sensor: {1} ===> measured: {2}'.format(self, sensor, measured_value))
        self.mqtt.send_object({ 'name': sensor.name(), 'value': measured_value })