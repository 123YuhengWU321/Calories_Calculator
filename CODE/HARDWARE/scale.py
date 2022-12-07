
"""
Guan Zheng Huang
March 13
scale driver and logic
"""

import RPi.GPIO as GPIO
import time
import sys
from hx711 import HX711

hx : HX711
'''
Setup with predefined scale offset
calabration value should be taken by running calibration.py
'''
def scaleSetupDEF(DTpin, SCKpin):
    global hx
    hx = HX711(DTpin, SCKpin)
    hx.set_offset(8518972.9375)
    hx.set_scale(-95.42857142857143)
'''
Dynamically set scale offset
calabration value should be taken by running calibration.py
param: offset: offset to set
scale: empty scale mass to set
'''
def scaleSetup(offset, scale):
    global hx
    hx.set_offset(offset)
    hx.set_scale(scale)

'''
Returns the current mass of scale, make a record of this by putting resultto file
'''
def getMass():
    val = hx.get_grams()
    print("Mass is ", str(val))

    hx.power_down()
    time.sleep(.001)
    hx.power_up()
    #if (False == True):
    return val

'''
Returns the current mass of scale, make a record of this by putting resultto file
The result is taken avaerage of vairous values
'''
def getAvgMass():
    val=[]
    i=0
    while i<5:
        val.append(hx.get_grams())
        print("Massls is ", str(val[i]))
        i+=1
    val.sort()
    hx.power_down()
    time.sleep(.001)
    hx.power_up()
    #if (False == True):
    print("Massrt is ", str(val))
    print("Massrt is ", str(val[2]))
    return val[2]
        


# if __name__ == "__main__":

#     setup()
#     while True:
#         getScale()