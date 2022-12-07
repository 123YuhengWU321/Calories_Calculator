"""
Domi (Daijun) Wang
March 20
code for camara, uses cv2 library, resizes images for faster uploading time to server
"""

import cv2
import time

def runCamara():
    cam = cv2.VideoCapture(0)
    ret, image = cam.read()
    resized = cv2.resize(image, (250,250))
    cv2.imwrite('/home/pi/Desktop/291PROJECT2/target.png', resized)
    cam.release()