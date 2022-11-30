#!/usr/bin/env python
# -*- coding: utf-8 -*-
import paho.mqtt.client as mqtt
from firebase import firebase
import datetime

'''
    Configurações do MQTT
'''
broker = "127.0.0.1"
port = 1883

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("SENSOR_DATA/PH_VALUE")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print("Message received\n\t"+msg.topic+" "+str(msg.payload))
    send_to_firebase_server(msg)

def send_to_firebase_server(msg):
    firebaseApp = firebase.FirebaseApplication('$URL_DO_FIREBASE', None)   

    data = {'ph_value': msg.payload,
            'time_created': datetime.datetime.now()}
    result = firebaseApp.post('/SENSOR_DATA', data)
    print("Firebase post result: \n\t")
    print result

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(broker, port)

client.subscribe("SENSOR_DATA/PH_VALUE")

client.loop_forever()
