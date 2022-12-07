

"""
Guan Zheng Huang
March 20
sample file to test everything
"""

from re import L
import RPi.GPIO as GPIO
import time
import sys
import scale
import nutritionCalc
#import LCD
import LED
import camara
import RFID
import button

LEDone_PIN = 11#bottom 6th pin from left
LEDtwo_PIN = 13#bottom 7th pin from left
ScaleDTpin=5#bottom 3th pin from left
ScaleSCKpin=7#bottom 4th pin from left

'''
clean and exit system
'''
def cleanAndExit():
    print("Cleaning...")
    GPIO.cleanup()
    print("Bye!")
    sys.exit()

'''
hardware setup
'''
def setup():
    scale.scaleSetupDEF(ScaleDTpin, ScaleSCKpin)
    LED.LEDSetUp(LEDone_PIN, LEDtwo_PIN)

'''
Overwrite input to predefined exsisting file (mass record)
param: mass: input to write to file, not not contain EOF signal
'''
def writeMassFile(mass):
    file = open("/home/pi/Desktop/291PROJECT2/mass.txt", "w")
    file.write(mass)
    file.close()

'''
Overwrite input to predefined exsisting file (calories record)
param: calo: input to write to file, not not contain EOF signal
'''
def writeCaloFile(type, calo):
    file = open("/home/pi/Desktop/291PROJECT2/calories.txt", "w")
    file.write( )
    file.write('|')
    file.write(calo)
    file.close()

def loop():
    #mass=scale.putMass()
    #writeMassFile("100")
    #camara.runCamara()
    RFIDFlag = 1
     
    if RFID.runRFID() == 2:
         print("YES")
    elif RFID.runRFID() == 1:
         print("NO")
    elif  RFIDFlag == 1:
         print("NO CARD")
    #if button.runButton() == 1:
        #print("PRESSED")
    #else:
        #print("NOT PRESSED")

    '''
    image=XXX.GETXXX(image)# take phto
    imgType = XXX.GETXXX(image)# get type based on photo
    calo=nutritionCalc.getCalo(imgType, mass)
    writeCaloFile(imgType, calo)
    '''

if __name__ == "__main__":

    #setup()
    while True:
        loop()
        time.sleep(0.1)