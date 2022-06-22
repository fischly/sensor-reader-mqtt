import json
import logging
import paho.mqtt.client as mqtt

class MQTTManager():
    '''Manages the MQTT client, connection and publishing.'''
    def __init__(self, config):
        mqtt_config = config.get('mqtt', {})

        self.address    = mqtt_config.get('host', 'localhost')
        self.port       = mqtt_config.get('port', 13337)
        self.topic      = mqtt_config.get('topic', 'localhost')
        self.qos        = mqtt_config.get('qos', 0)
        
        self.client = mqtt.Client()
        self.client.on_connect = lambda client, userdata, flags, rc: logging.warning('Connected with result code {}'.format(str(rc)))
        self.client.connect(self.address, self.port, 60)
    
    def send_object(self, object_to_send):
        '''Serializes the given object into JSON and sends it to the connected MQTT broker.'''
        data_to_send = json.dumps(object_to_send)
        
        print('[send_object] sending {}'.format(data_to_send))
        
        self.client.publish(self.topic, payload=data_to_send, qos=self.qos)
        
    def disconnect(self):
        '''Disconnects the underlying MQTT client.'''
        self.client.disconnect()