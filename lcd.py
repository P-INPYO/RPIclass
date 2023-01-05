import I2C_driver
import smbus
from time import *
import RPi.GPIO as GPIO 
import time

DISPLAY = [0x3F,0x06,0x5B,0x4F,0x66,0x6D,0x7D,0x07,0x7F,0x67]          
PIN = [13,6,16,20,21,19,26]
NUM = [0x01,0x02,0x04,0x08,0x10,0x20,0x40,0x80]

GPIO.setwarnings(False)            
mylcd = I2C_driver.lcd()


def PORT(pin):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(PIN,GPIO.OUT)
    for i in range(7):
        if(pin&NUM[i] == NUM[i]):

            GPIO.output(PIN[i],GPIO.HIGH)            

        else:

            GPIO.output(PIN[i],GPIO.LOW)   


def main(a):
    GPIO.setmode (GPIO.BCM)           
    GPIO.setup(12, GPIO.OUT) 
    Servo=GPIO.PWM(12, 40)
    
    if a <= 18:
        duty_ratio = 1
    elif a == 180:
        duty_ratio = 9
    else:
        duty_ratio = int(a/18)
    
    Servo.start(0)
    print('Wating for 1 sec') 
    time.sleep(1) 
    
    Servo.ChangeDutyCycle(duty_ratio)
    time.sleep(0.5)
        
    
    Servo.stop()
    GPIO.cleanup()
    print('Everythings cleanup')
    

while 1:
    print('1 : FND \n2 : servo')
    sel = int(input())
    
    if sel == 1:
        mylcd.lcd_clear()
        mylcd.lcd_display_string(f"{sel}:FND", 1)
        print('enter 1~9')
        f = int(input())
        mylcd.lcd_display_string(f"{f}", 2)
        pin = DISPLAY[f]       
        PORT(pin)
        
    elif sel == 2:
        mylcd.lcd_clear()
        mylcd.lcd_display_string(f"{sel}:servo", 1)
        print('enter 0~180')
        s = int(input())
        mylcd.lcd_display_string(f"{s}", 2)
        a = int(s)
        main(a)

