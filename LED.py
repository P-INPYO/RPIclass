import RPi.GPIO as GPIO
import time

list = [14,15,18]

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(list,GPIO.OUT)

def LED():
    for i in range(3):
        GPIO.output(list,GPIO.LOW)
        GPIO.output(list[i],GPIO.HIGH)
        time.sleep(1)
    
while True:
    LED()
    
    
    
    
    
    
    
    
