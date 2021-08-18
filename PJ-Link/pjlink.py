#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: David Stevens 

from os import error
import sys
import time
import json
import logging

from pypjlink.projector import MUTE_AUDIO, MUTE_VIDEO

#logging.basicConfig(level=logging.INFO)

#sys.path.append('../')
from pypjlink import Projector

stdinput = sys.stdin.readline()
data = json.loads(stdinput)

try:
    host = data['params']['host']
    command = data['params']['command']

    print("Host:" + host)
    print("Command:" + command)
    try:
        with Projector.from_address(host) as projector:
            projector.authenticate()
            if command == 'On':
                projector.set_power('on')
            elif command == 'Off':
                projector.set_power('off')
        print("End of list")

    except KeyboardInterrupt:
        pass


    print('{ "complete": 1 }')
except:
    print(error)
    print('{ "complete": 1, "code": 999, "description": "Failed to execute." }')
