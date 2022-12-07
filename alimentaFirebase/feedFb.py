#!/usr/bin/env python
# -*- coding: utf-8 -*-
from firebase import firebase
import datetime
import random
import time

FB_URL="IP"

def feedFb():
    global FB_URL
    firebaseApp = firebase.FirebaseApplication(FB_URL, None)

    for i in range(0,100):
        pH = random.randint(1,14)
        temp = random.randint(25,40)

        data = {'ph_value': pH,
                'temp': temp,
                'time_created': datetime.datetime.now()}
        result = firebaseApp.post('/END_NODE1', data)
        print("Firebase post result: \n\t")
        print(result)
        time.sleep(5)

feedFb()
