#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import time
import json, simplejson
sys.path.append('..')
from freeboxctrl import FreeboxCtrl
from freeboxctrl import NetworkError
from freeboxctrl import AppTokenError

myBox = FreeboxCtrl('presence.id', 'mafreebox.freebox.fr')

try:
    myBox.load_token()
except:
    print('Enable application access with the Freebox front panel')
    myBox.register('ZalarmPi', 'FreeboxCtrl', 'v0.1')
    myBox.save_token()

#Display Lan Hosts conected
try:


    #mac = "ether-84:b1:53:e4:91:54,ether-f0:25:b7:d1:74:e9"
    mac = sys.argv[1]
    jsonform = myBox.state_lan_host(mac)
    jsonlist = myBox.configuration_lan_browser()

    #json.dumps(data, indent=4, separators=(',', ': '), sort_keys=True)
    for key in jsonlist:
        for item, value in key.iteritems():

            if str(item) == "primary_name":
                print(json.dumps(value))

                if str(item) == "host_type":
                    print(json.dumps(value))

                if str(item) == "last_activity":
                    print(json.dumps(value))

                if str(item) == "active":
                    print(json.dumps(value))

                if str(item) == "id":
                    print(json.dumps(value))

        print("------------")

    for key, value in jsonform.iteritems():
        #print(json.dumps(key, value, sort_keys=True, indent=1))
        #print(key, value)
        #print(json.dumps(key))

        if str(key) == "primary_name":
            #print(json.dumps(key))
            print(json.dumps(value))

        if str(key) == "host_type":
            #print(json.dumps(key))
            print(json.dumps(value))

        if str(key) == "last_activity":
            #print(json.dumps(key))
            print(json.dumps(value))

        if str(key) == "active":
            #print(json.dumps(key))
            print(json.dumps(value))



except AppTokenError:
    myBox.remove_token()
    print("invalid token removed")
    #time.sleep(30)
