

"""
Guan Zheng Huang
March 20
main file for machine 1, also main template for all machines
"""

from re import L
import RPi.GPIO as GPIO
import time
import sys
import scale
import nutritionCalc
import priceCalc
import SCREEN
import LED
import camara
import RFID

# this is GPIO pins by default
LEDonePin = 13#bottom xth pin from left
LEDtwoPin = 6#bottom xth pin from left
scaleDTpin = 17#bottom 6th pin from left
scaleSCKpin = 27#bottom 7th pin from left
switchPin = 26 #bottom 8th pin from left

systemState = "on"
debug = True

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
    if (debug): print("setup scale")
    scale.scaleSetupDEF(scaleDTpin, scaleSCKpin)
    if (debug):print("setup LED")
    LED.LEDSetUp(LEDonePin, LEDtwoPin)
    if (debug): print("setup switch")
    GPIO.setup(switchPin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    
'''
Overwrite input to predefined exsisting file (mass record)
param: mass: input to write to file, not not contain EOF signal
modifies: a file called ms.txt by overwriting its result
'''
def writeMassFile(mass):
    file = open("ms.txt", "w")
    file.write(str(mass))
    file.close()
    if (debug):print("wrote to mass")
    
'''
read from file and if the input is valid Overwrite file to predefined string
return: NONE if nothing is found, vegetable type in string if match
modifies: a file called pred_result.txt by overwriting its result
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
param: type: input to write to file, not not contain EOF signal
modifies: a file called tpcalo.txt by overwriting its result
'''
def writeCaloFile(type, calo):
    file = open("tpcalo.txt", "w")
    file.write(type)
    file.write('|')
    file.write(str(calo))
    file.close()
    
'''
Overwrite input to predefined exsisting file (calories record)
param: type: input to write to file, not not contain EOF signal
param: calo: input to write to file, not not contain EOF signal
param: mass: input to write to file, not not contain EOF signal
modifies: a file called allInfoCalo.txt by overwriting its result
'''
def writeAllCalo(type, mass, calo):
    file = open("allInfoCalo.txt", 'w')
    file.write(type)
    file.write("=   =")
    file.write(str(mass))
    file.write("g")
    file.write("=   =")
    file.write(str(calo))
    file.write("Calories")
    file.close()
    
'''
concat input to predefined exsisting file (calories record)
param: type: input to write to file, not not contain EOF signal
param: calo: input to write to file, not not contain EOF signal
param: mass: input to write to file, not not contain EOF signal
modifies: a file called history.txt by adding to its result
'''
def concatAllCalo(type, mass, calo):
    file = open("history.txt", 'a')
    file.write(type)
    file.write("     ")
    file.write(str(mass))
    file.write("g")
    file.write("     ")
    file.write(str(calo))
    file.write("Calories")
    file.write("\n")
    file.close()
    
'''
Overwrite input to predefined exsisting file (calories record)
param: type: input to write to file, not not contain EOF signal
param: price: input to write to file, not not contain EOF signal
param: mass: input to write to file, not not contain EOF signal
modifies: a file called allInfoPrice.txt by overwriting its result
'''
def writeAllPrice(type, mass, price):
    file = open("allInfoCalo.txt", 'w')
    file.write(str(type))
    file.write("=   =")
    file.write(str(mass))
    file.write("g")
    file.write("=   =")
    file.write(str(price))
    file.write("$")
    file.close()
'''
Overwrite input to predefined exsisting file (calories record)
param: type: input to write to file, not not contain EOF signal
param: price: input to write to file, not not contain EOF signal
param: mass: input to write to file, not not contain EOF signal
modifies: a file called receipt.txt by adding to its its result
'''
def concatAllPrice(type, mass, price):
    file = open("receipt.txt", 'a')
    file.write(type)
    file.write("     ")
    file.write(str(mass))
    file.write("g")
    file.write("     ")
    file.write(str(price))
    file.write("$")
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
main body of logic, each loop represent one scan-upload cycle of calories calculation
requires: the correct system State to function, will not run is set to false
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
        LED.lightLED(LEDtwoPin)
        mass=scale.getAvgMass()
        SCREEN.runScreen("MASS", mass)
        LED.dimLED(LEDtwoPin)
        writeMassFile(mass)
        if (debug): print("in loop2")
        camara.runCamara()
        imgType = readTypeFile()# get type based on photo
        if (imgType!="NONE"):
            if (debug): print("type read = ", imgType)
            calo=nutritionCalc.getCalo(imgType, mass)
            
            writeCaloFile(imgType, calo)
            writeAllCalo(imgType, mass, round(calo, 4))
            concatAllCalo(imgType, mass, calo)
        if systemState =="on":
            time.sleep(0.05)
        elif systemState =="sleep":
            if (debug): print("sleeping")
            time.sleep(3)
            #if no wait change, change counter
        if (lastmass < mass+10 and lastmass > mass-10):
            counter+=1
        else:
            if (debug): print("counter reset")
            systemState ="on"
            counter=0
            #system enter sleep mode after ~20 second, in slow mode
        if (counter > 5):
            systemState ="sleep"
        if (debug): print("counter", str(counter))
        sysState()
'''
main body of logic, each loop represent one scan-upload cycle and calculation of price
requires: the correct system State to function, will not run is set to false
'''
def loopPrice():
    counter=0
    mass:float=0
    lastmass:float=0
    global systemState
    if (debug): print("bf loop P")
    while (systemState =="on" or systemState =="sleep"):
        if (debug): print("in loopP")
        sysState()
        lastmass=mass
        LED.lightLED(LEDtwoPin)
        mass=scale.getAvgMass()
        SCREEN.runScreen("MASS", mass)
        LED.dimLED(LEDtwoPin)
        writeMassFile(mass)
        if (debug): print("in loop2P")
        camara.runCamara()
        imgType = readTypeFile()# get type based on photo
        if (imgType!="NONE"):
            if (debug): print("type read = ", imgType)
            price=priceCalc.getPrice(imgType, mass)
            
            #writePriceFile(imgType, calo)
            writeAllPrice(imgType, mass, round(price, 2))

            concatAllPrice(imgType, mass, price)
        if systemState =="on":
            time.sleep(0.05)
        elif systemState =="sleep":
            if (debug):print("sleeping")
            time.sleep(3)
            #if no wait change, change counter
        if (lastmass < mass+10 and lastmass > mass-10):
            counter+=1
        else:
            if (debug):print("counter reset")
            systemState ="on"
            counter=0
            #system enter sleep mode after ~20 second, in slow mode
        if (counter > 5):
            systemState ="sleep"
        if (debug): print("counter", str(counter))

'''
determines the current swith position,
based on the positions update system status and indicate such with led
'''
def sysState():
    global systemState
    global switchPin
    #while switch at 8th on left is powered, system on, else off
    if GPIO.input(switchPin):
        if (systemState != "sleep"):
            LED.lightLED(LEDonePin)
            systemState="on"
        if systemState == "sleep":
            LED.blinkLED(LEDonePin)
            clearFile()
    else:
        systemState="off"
        LED.dimLED(LEDonePin)
        
'''
Logic control of machine
changes mode between calories calculation and price calculation in each cycle
'''
def boot():
        #if system is on, loop
    # this enables reset, on off, and control server (it on longer see update)
    setup()
    
    while(RFID.runRFID() != 2):
        
        print("WRONG CARD")
        LED.dimLED(LEDonePin)
        time.sleep(0.3)
        LED.lightLED(LEDonePin)
        
    LED.lightLED(LEDtwoPin)
    time.sleep(0.3)
    LED.dimLED(LEDtwoPin)
    time.sleep(0.4)
    
        
    if (systemState =="on" or systemState =="sleep"):
        #codewaXS\A
        sysState()
        loop()
    GPIO.cleanup()
    setup()
    if (debug): print("calco system off")
    while (systemState == "off"):
        sysState()
        time.sleep(0.3)
    #enter price mode
    setup()
    if (systemState =="on" or systemState =="sleep"):
        #codewaXS\A
        sysState()
        loopPrice()
    GPIO.cleanup()
    setup()
    if (debug): print("price system off")
    while (systemState == "off"):
        sysState()
        time.sleep(0.3)
            
if __name__ == "__main__":
    print("System Start")
    while True:
        
        clearFile()
        boot()
        if (debug):print("system restarting")
    
         