import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
from time import sleep

def runRFID():
    print('in')
    reader = SimpleMFRC522()
    print('in')
    
    id, text = reader.read()
    print('in')
    if id == 1075769263901:
        print('in2')
        return 2

    elif id == 582943552171:
        print('in3')
        return 1
    else:
        print('in22')
        return 0


