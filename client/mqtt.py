import json

import paho.mqtt.client as mqtt
from django.conf import settings
# from superviseur.models import nodes
from compte.models import *
from datetime import datetime

topics = ['v3/loraatest02@ttn/devices/eui-70b3d57ed005a5c4/up', 'v3/loraatest02@ttn/devices/eui-70b3d57ed005c92e/up', 'v3/loraatest02@ttn/devices/eui-2cf7f1c044900011/up']

def on_connect(mqtt_client, userdata, flags, rc):
    if rc == 0:
        print('Connected successfully')
        mqtt_client.subscribe(topics[0])
        mqtt_client.subscribe(topics[1])
        mqtt_client.subscribe(topics[2])
    else:
        print('Bad connection. Code:', rc)

def on_message(mqtt_client, userdata, msg):
    # Decode the incoming message
    payload_dict =json.loads(msg.payload)
    print("hamza")
    print(payload_dict)
    for topic in topics:
        if msg.topic == topic :
            # Get all nodes
            nodes_list = nodes.objects.all()
            print(nodes_list)
            for node in nodes_list:
                namee=node.Name
                print(namee)
                if msg.topic == f'v3/loraatest02@ttn/devices/{node.Name}/up':
                    temperature = payload_dict['uplink_message']['decoded_payload']['temperature']
                    humidity = payload_dict['uplink_message']['decoded_payload']['humidity']
                    rssi = payload_dict['uplink_message']['rx_metadata'][0]['rssi']
                    snr = payload_dict['uplink_message']['rx_metadata'][0]['snr']

                    print('temperature :', temperature, 'humidity :', humidity, 'rssi :', rssi, 'snr :', snr, '\n')
                    
                    new_data = Data.objects.create(temperature=temperature, humidity=humidity, nodes=node)
                    new_data.save()


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = lambda client, userdata, msg: on_message(client, userdata, msg)

client.username_pw_set(settings.MQTT_USER, settings.MQTT_PASSWORD)

client.connect(
    host=settings.MQTT_SERVER,
    port=settings.MQTT_PORT,
    keepalive=settings.MQTT_KEEPALIVE
)

