import RPi.GPIO as GPIO
GPIO.setwarnings(False)

from time import sleep

def runButton():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(37, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
    
    try:
        while True:
            if GPIO.input(37) == GPIO.LOW:
                return 1
            else:
                return 0
    finally:
        GPIO.cleanup()
