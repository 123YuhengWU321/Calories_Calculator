from signal import signal, SIGTERM, SIGHUP, pause
from rpi_lcd import LCD  
import time



def runScreen(one, two):
    
    lcd = LCD()

    lcd.text(str(one), 1)
    lcd.text(str(two), 3)
    time.sleep(1)
