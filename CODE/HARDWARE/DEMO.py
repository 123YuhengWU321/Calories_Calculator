

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

LEDonePin = 13#bottom xth pin from left
LEDtwoPin = 6#bottom xth pin from left
scaleDTpin = 17#bottom 6th pin from left
scaleSCKpin = 27#bottom 7th pin from left
switchPin = 26 #bottom 8th pin from left

systemState = "on"
debug = False

'''
clean and exit system
'''
def cleanAndExit():
    print("Cleaning")
    GPIO.cleanup()
    print("Exit")
    sys.exit()
    
'''
hardware setup
'''
def setup():
    global switchPin
    print("system setup")
    GPIO.setwarnings(False)
    print("system setup scale")
    scale.scaleSetupDEF(scaleDTpin, scaleSCKpin)
    print("system setup LED")
    LED.LEDSetUp(LEDonePin, LEDtwoPin)
    print("system switch")
    GPIO.setup(switchPin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    
'''
Overwrite input to predefined exsisting file (mass record)
param: mass: input to write to file, not not contain EOF signal
'''
def writeMassFile(mass):
    file = open("ms.txt", "w")
    file.write(str(mass))
    file.close()
    print("wrote to mass")
    
'''
Overwrite input to predefined exsisting file (mass record)
param: mass: input to write to file, not not contain EOF signal
return: NONE if nothing is found, vegetable type in string if match
'''
def readTypeFile():
    #file read
    file = open("/home/pi/Desktop/291PROJECT2/pred_result.txt", "r")
    type=file.read()
    file.close()
    #if file contain information, clear such information
    if (type!="NONE"):
        file = open("/home/pi/Desktop/291PROJECT2/pred_result.txt", "w")
        file.write("NONE")
        file.close()
    return type

'''
Overwrite input to predefined exsisting file (calories record)
param: calo: input to write to file, not not contain EOF signal
'''
def writeCaloFile(type, calo):
    file = open("tpcalo.txt", "w")
    file.write(type)
    file.write('|')
    file.write(str(calo))
    file.close()
    
'''
Overwrite input to predefined exsisting file (calories record)
param: calo: input to write to file, not not contain EOF signal
'''
def writeAllCalo(type, mass, calo):
    file = open("allInfoCalo.txt", 'w')
    file.write(type)
    file.write("   ")
    file.write(str(mass))
    file.write("   ")
    file.write(str(calo))
    file.close()
    
'''
concat input to predefined exsisting file (calories record)

'''
def concatAllCalo(type, mass, calo):
    file = open("history.txt", 'a')
    file.write(type)
    file.write("   ")
    file.write(str(mass))
    file.write("   ")
    file.write(str(calo))
    file.write("\n")
    file.close()
    
'''
Overwrite input to predefined exsisting file (calories record)
param: calo: input to write to file, not not contain EOF signal
'''
def writeAllPrice(type, mass, price):
    file = open("allInfoCalo.txt", 'w')
    file.write(str(type))
    file.write("   ")
    file.write(str(mass))
    file.write("   ")
    file.write(str(price))
    file.close()
'''
Overwrite input to predefined exsisting file (calories record)

'''
def concatAllPrice(type, mass, price):
    file = open("receipt.txt", 'a')
    file.write(type)
    file.write("   ")
    file.write(str(mass))
    file.write("   ")
    file.write(str(price))
    file.write("\n")
    file.close()
'''
clear history of all file
'''
def clearFile():
    file = open("history.txt", "w")
    file.close()
    file = open("receipt.txt", "w")
    file.close()
'''
main body of logic, each loop represent one scan-upload cycle
'''
def loop():
    counter=0
    mass:float=0
    lastmass:float=0
    global systemState
    if (debug): print("bf loop")
    while (systemState =="on" or systemState =="sleep"):
        if (debug): print("in loop")
        sysState()
        lastmass=mass
        mass=scale.getAvgMass()
        writeMassFile(mass)
        if (debug): print("in loop2")
        camara.runCamara()
        imgType = readTypeFile()# get type based on photo
        if (imgType!="NONE"):
            print("type read = ", imgType)
            calo=nutritionCalc.getCalo(imgType, mass)
            writeCaloFile(imgType, calo)
            writeAllCalo(imgType, mass, calo)
            if (not (lastmass < mass+10 and lastmass > mass-10)):
                concatAllCalo(imgType, mass, calo)
        if systemState =="on":
            time.sleep(0.05)
        elif systemState =="sleep":
            print("sleeping")
            time.sleep(3)
            #if no wait change, change counter
        if (lastmass < mass+10 and lastmass > mass-10):
            counter+=1
        else:
            print("counter reset")
            systemState ="on"
            counter=0
            #system enter sleep mode after ~20 second, in slow mode
        if (counter > 60):
            systemState ="sleep"
        print("counter", str(counter))
            
def sysState():
    global systemState
    global switchPin
    #while switch at 8th on left is powered, system on, else off
    if GPIO.input(switchPin):
        if (systemState != "sleep"):
            LED.lightLED(LEDonePin)
            systemState="on"
        if systemState == "sleep":
            LED.blinkLED(LEDonePin, 0.5)
            clearFile()
    else:
        systemState="off"
        LED.dimLED(LEDonePin)
        
def boot():
        #if system is on, loop
    # this enables reset, on off, and control server (it on longer see update)
    setup()
    
    while(RFID.runRFID() != 2):
        time.sleep(0.3)
        print("WRONG CARD")
    
    if (systemState =="on" or systemState =="sleep"):
        #codewaXS\A
        loop()
    GPIO.cleanup()
    setup()
    print("system off")
    while (systemState == "off"):
        sysState()
        time.sleep(1)
            
if __name__ == "__main__":
    print("system start")
    while True:
        
        clearFile()
        boot()
        time.sleep(1)
        print("system restart")
    
        