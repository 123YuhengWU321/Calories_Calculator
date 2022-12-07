import RPi.GPIO as GPIO
import time

'''
LEDset up
param: LEDonePin/LEDtwoPin: pins to setup led
'''
def LEDSetUp(LEDonePin, LEDtwoPin):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(LEDonePin, GPIO.OUT)
    GPIO.setup(LEDtwoPin, GPIO.OUT)

'''
light the led for one second then dim it
param: LEDpin: LED to light/dim
'''
def lightLEDoneSec(LEDpin):
    GPIO.output(LEDpin, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(LEDpin, GPIO.LOW)
    
'''
light the led for one second then dim it
param: LEDpin: LED to light/dim
'''
def blinkLED(LEDpin):
    GPIO.output(LEDpin, GPIO.HIGH)
    time.sleep(0.7)
    GPIO.output(LEDpin, GPIO.LOW)
'''
light led and keep it light
param: LEDpin: LED to light/dim
'''
def lightLED(LEDpin):
    GPIO.output(LEDpin, GPIO.HIGH)
'''
Dim led and keep it dim
param: LEDpin: LED to light/dim
'''
def dimLED(LEDpin):
    GPIO.output(LEDpin, GPIO.LOW)