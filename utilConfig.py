import keyboard as key
import json
import os

from utilContext import *
from utilControl import *

def loadConfig():
    # check if local config exists if not create blank file and prompt filling
    # info: login, draggers
    if not os.path.exists('localConfig.json'):
        print('creating new localConfig.json')

        o = {}
        o['user'] = ''
        o['pass'] = ''

        d1 = {}
        d1['name'] = ''
        d1['x'] = 0
        d1['y'] = 0
        d1['dx'] = 0
        d1['dy'] = 0

        o['drag1'] = d1
        o['drag2'] = d1
        o['drag2_02'] = d1
        o['drag2_02'] = d1
        o['retreats_02'] = []

        with open('localConfig.json', 'w') as config:
            json.dump(o, config, indent=4)
    else:
        print('loading localConfig.json')

        with open('localConfig.json', 'r') as config:
            o = json.load(config)
            
            cd.username = o['user']
            cd.password = o['pass']

            d1 = o['drag1']
            cd.clickDps1 = (((d1['x'], d1['y']), (d1['dx'], d1['dy']), 0), 0.8, 0.5, False)

            d2 = o['drag2']
            cd.clickDps2 = (((d2['x'], d2['y']), (d2['dx'], d2['dy']), 0), 0.8, 0.5, False)

            d1_02 = o['drag1_02']
            cd.clickDps1_02 = (((d1_02['x'], d1_02['y']), (d1_02['dx'], d1_02['dy']), 0), 0.8, 0.5, False)

            d2_02 = o['drag2_02']
            cd.clickDps2_02 = (((d2_02['x'], d2_02['y']), (d2_02['dx'], d2_02['dy']), 0), 0.8, 0.5, False)

            cd.retreats_02 = o['retreats_02']
            cd.special_repair = o['special_repair']

            cd.globalx = o['global_x_offset']
            cd.globaly = o['global_y_offset']

def login():
    rClick(*((938, 469), (56.0, 10.5), 0))
    wait(0.1666, 0)
    key.write(cd.username)
    wait(0.5, 0)
    rClick(*((928, 514), (45.5, 9.0), 0))
    wait(0.1666, 0)
    key.write(cd.password)
    wait(0.5, 0)
    rClick(*((1091, 571), (81.5, 14.5), 0))