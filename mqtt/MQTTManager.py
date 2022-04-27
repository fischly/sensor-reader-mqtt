import json
import logging
import paho.mqtt.client as mqtt

class MQTTManager():
    '''Manages the MQTT client, connection and publishing.'''
    def __init__(self):
        self.port = 13337           # todo: move to config file
        self.address = 'localhost'  # todo: move to config file
        self.topic = 'dci-test' # todo: move to config file
        
        self.client = mqtt.Client()
        self.client.on_connect = lambda client, userdata, flags, rc: logging.warning('Connected with result code {}'.format(str(rc)))
        self.client.connect(self.address, self.port, 60)
    
    def send_object(self, object_to_send):
        '''Serializes the given object into JSON and sends it to the connected MQTT broker.'''
        data_to_send = json.dumps(object_to_send)
        
        print('[send_object] sending {}'.format(data_to_send))
        
        self.client.publish(self.topic, payload=data_to_send, qos=0)
        
    def disconnect(self):
        '''Disconnects the underlying MQTT client.'''
        self.client.disconnect()