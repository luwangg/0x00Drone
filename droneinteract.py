#!/usr/bin/env python3
# coding: utf-8

import sys
import time
import threading
import RPi.GPIO as GPIO
from collections import deque

if sys.version_info[0] == 2:
    input = raw_input

DESTRUCT_QUESTIONS = [
    'Do you REALLY want activate the destruction? [y/n] ',
    'Are you sure? [y/n] ',
    'Really? [y/n] ',
]

GPIO_OUTPUT = {
    'destruct': 2,
    'detach'  : 3,
    'beacon'  : 4
}

GPIO_INPUT = {
    'JOB_OK'  : 17,
    'JOB_FAIL': 27
}

HOLD_TIME = 1 # in seconds
WAIT_FOR_RESPONSE = 3 # in seconds

RECV_NORESPONSE = 0
RECV_OK         = 1
RECV_FAIL       = 2

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

deque(map(lambda pin: GPIO.setup(pin, GPIO.INPUT), GPIO_INPUT.values()), 0)
deque(map(lambda pin: GPIO.setup(pin, GPIO.OUTPUT), GPIO_OUTPUT.values()), 0)

def send_command(port):
    time.sleep(HOLD_TIME)
    GPIO.output(port, GPIO.LOW)
    print('Send command...')

def get_response():
    alarm = threading.Timer(WAIT_FOR_RESPONSE, lambda: None)
    alarm.start()
    received = RECV_NORESPONSE

    while alarm.is_alive():
        if GPIO.input(GPIO_INPUT['JOB_OK']) == GPIO.HIGH:
            received = received | RECV_OK

        if GPIO.input(RECV_FAIL) == GPIO.HIGH:
            received = received | RECV_FAIL
    
    alarm.cancel()
    if (received == RECV_NORESPONSE) or (received == RECV_OK | RECV_FAIL):
        print('No response received..')
        return RECV_NORESPONSE

    return received

def attach():
    GPIO.output(GPIO_OUTPUT['detach'], GPIO.HIGH)

    if get_response() == RECV_FAIL:
        print('ERROR: JOB_FAIL RECEIVED')

    input('Press Enter to detach')
    GPIO.output(GPIO_OUTPUT['beacon'], GPIO.LOW)

def beacon():
    GPIO.output(GPIO_OUTPUT['beacon'], GPIO.HIGH)

    if get_response() == RECV_FAIL:
        print('ERROR: JOB_FAIL RECEIVED')

    input('Press Enter to deactivate the beacon again ')
    GPIO.output(GPIO_OUTPUT['beacon'], GPIO.LOW)

def destruct():
    GPIO.output(GPIO_OUTPUT['destruct'], GPIO.HIGH)
    time.sleep(10)

def main(command):
    command_dict = {
        'attach'  : attach,
        'beacon'  : beacon,
        'destruct': destruct
    }

    if command == 'destruct':
        if all([input(q) == 'y' for q in DESTRUCT_QUESTIONS]) == False:
            print('Aborting...')
            sys.exit()

    command_dict.get(command, sys.exit)()

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage ./droneinteract.py <attach/beacon/destruct>")
        sys.exit()

    main(sys.argv[1].lower())