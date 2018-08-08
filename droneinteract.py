import sys
import time
import threading

if(len(sys.argv)!=2):
    print("Usage ./droneinteract.py <(a)ttach/(b)eacon/destruct>")
    exit()
    
try:
    input_ = raw_input
except NameError:
    input_ = input
    
DESTRUCT = 2 # HIGH = on
DETACH   = 3 # LOW  = on
BEACON   = 4 # HIGH = on

JOB_OK   = 17
JOB_FAIL = 27

HOLD_TIME = 1 # in seconds
WAIT_FOR_RESPONSE = 3 # in seconds

RECV_NORESPONSE = 0
RECV_OK         = 1
RECV_FAIL       = 2
    
    
def timeout(): pass

def sendCommand(port):

    time.sleep(HOLD_TIME)
    if RPI:
        GPIO.output(port, GPIO.LOW)
    else:
        print("Send command...")
    return
        
        
def getResponse():
    alarm = threading.Timer(WAIT_FOR_RESPONSE, timeout)
    alarm.start()
    received = RECV_NORESPONSE
    while alarm.is_alive():
        if RPI:
            if(GPIO.input(JOB_OK) == GPIO.HIGH):
                received = received | RECV_OK
            if(GPIO.input(RECV_FAIL) == GPIO.HIGH):
                received = received | RECV_FAIL
    alarm.cancel()
    if not RPI:
        print("Got Response...")
    else:
        if received == RECV_NORESPONSE or received == RECV_OK|RECV_FAIL:
            print("No response received..")
            return RECV_NORESPONSE
    return received
    
    
    
        
def attach():
    if RPI:
        GPIO.output(DETACH, GPIO.HIGH)
    if(getResponse() == RECV_FAIL):
        print("ERROR: JOB_FAIL RECEIVED")
    input_('Press Enter to detach ')
    if RPI:
        GPIO.output(BEACON, GPIO.LOW)
     
    
def beacon():
    if RPI:
        GPIO.output(BEACON, GPIO.HIGH)
    if(getResponse() == RECV_FAIL):
        print("ERROR: JOB_FAIL RECEIVED")
    input_('Press Enter to deactivate the beacon again ')
    if RPI:
        GPIO.output(BEACON, GPIO.LOW)
        
def destruct():
    if RPI:
        GPIO.output(DESTRUCT, GPIO.HIGH)
    time.sleep(10)
    

command = sys.argv[1]
command_function = None
#if command == "detach" or command == "d":
#    command_function = detach
if command == "attach" or command == "a":
    command_function = attach
elif command == "beacon" or command == "b":
    command_function = beacon
elif command == "destruct":
    command = "destruct"
    if not input_('Do you REALLY want activate the destruction? [y/n] ').lower()[0]=='y':
        print("Aborting..")
        exit()
    if not input_('Are you sure? [y/n] ').lower()[0]=='y':
        print("Aborting..")
        exit()
    if not input_('Really? [y/n] ').lower()[0]=='y':
        print("Aborting..")
        exit()
    command_function = destruct
else:
    print("Usage ./droneinteract.py <(a)ttach/(b)eacon/destruct>")
    exit()

try:
    import RPi.GPIO as GPIO
    RPI = True
except:
    RPI = False
    print("Running on test system..")
    


if RPI:
    GPIO.setmode(GPIO.BCM)
    #OUTPUTS
    GPIO.setup(DESTRUCT, GPIO.OUT)
    GPIO.setup(DETACH, GPIO.OUT)
    GPIO.setup(BEACON, GPIO.OUT)
    #INPUTS
    GPIO.setup(JOB_OK, GPIO.IN)
    GPIO.setup(JOB_FAIL, GPIO.IN)
else:
    print("Setup..")
    

command_function()


if RPI:
    GPIO.cleanup()
else:
    print("Cleanup..")
