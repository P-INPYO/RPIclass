import RPi.GPIO as IO           
import time                             


DISPLAY = [0x3F,0x06,0x5B,0x4F,0x66,0x6D,0x7D,0x07,0x7F,0x67]          
PIN = [13,6,16,20,21,19,26,12]
NUM = [0x01,0x02,0x04,0x08,0x10,0x20,0x40,0x80]

IO.setwarnings(False)            
IO.setmode (IO.BCM)           
IO.setup(PIN,IO.OUT)          


def PORT(pin):                    
    for i in range(8):
        if(pin&NUM[i] == NUM[i]):

            IO.output(PIN[i],1)            

        else:

            IO.output(PIN[i],0)            
        

while 1:

    for x in range(10):            

        pin = DISPLAY[x]       

        PORT(pin);              

        time.sleep(1)

