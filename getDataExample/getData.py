#!/usr/bin/env python
# -*- coding: utf-8 -*-
from firebase import firebase
import datetime
import random
import time
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure

FB_URL="IP"
data = []

def getData():
    global FB_URL, data
    firebaseApp = firebase.FirebaseApplication(FB_URL, None)

    result = firebaseApp.get('/END_NODE1', None)
    
    #print(result)
    for value in result:
        #print(result[value]['time_created'])
        data.append((result[value]['time_created'], result[value]['ph_value']))


def plot():
    global data
    figure(figsize=(9, 6), dpi=300)
    ## reverte a ordem para pegar dados mais atuais
    data = data[::-1]
    ## pega apenas os 20 primeiros
    data = data[:20]
    print(data)

    fig = plt.figure()
    plt.plot(list(zip(*data))[0], list(zip(*data))[1])

    plt.xticks(rotation=30, ha='right')
    plt.xlabel('Date')
    plt.xlabel('pH')
    plt.rc('axes', labelsize=8)

    plt.gcf().autofmt_xdate()

    plt.savefig('my_plot.png', dpi=300)


getData()
plot()
