#!/usr/bin/python3

import sys
import json
import socket
import time
import os

try:
    stdinput = sys.stdin.readline()
    data = json.loads(stdinput)

    ip = data['params']['ip']
    command = data['params']['command']
    token = data['params']['token']
    pin = data['params']['pin']
    port = data['params']['port']

    if (command == 'on'):
        stream = os.popen('pyvizio --ip=' + ip + ':' + port + ' --auth=' + token + ' power on')
        output = stream.read()
        output
    
    if (command == 'off'):
        stream = os.popen('pyvizio --ip=' + ip + ':' + port + ' --auth=' + token + ' power off')
        output = stream.read()
        output

    print('{ "complete": 1 }')
except:
    print('{ "complete": 1, "code": 999, "description": "Failed to execute." }')
