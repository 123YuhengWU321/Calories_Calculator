# Write your code here :-)
import cv2
import time

#cam = cv2.VideoCapture(0)
while True:
    cam = cv2.VideoCapture(0)
    time.sleep(0.5)
    while True:
        ret, image = cam.read()
        #cv2.imshow('Imagetest',image)
        k = cv2.waitKey(1)
        if k == -1:
            break
    resized = cv2.resize(image, (250,250))
    cv2.imwrite('/home/pi/Desktop/291PROJECT2/target.png', resized)
    cam.release()
    time.sleep(0.5)
    #cv2.destroyAllWindows()