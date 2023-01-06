import I2C_driver
import smbus
from time import *
import RPi.GPIO as GPIO 
import time
PinTrig=14
PinEcho=15
DISPLAY = [0x3F,0x06,0x5B,0x4F,0x66,0x6D,0x7D,0x07,0x7F,0x67]          
PIN = [13,6,16,20,21,19,26]
NUM = [0x01,0x02,0x04,0x08,0x10,0x20,0x40,0x80]

GPIO.setwarnings(False)            
mylcd = I2C_driver.lcd()

def FND(pin):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(PIN,GPIO.OUT)
    for i in range(7):
        if(pin&NUM[i] == NUM[i]):

            GPIO.output(PIN[i],GPIO.HIGH)            

        else:

            GPIO.output(PIN[i],GPIO.LOW)

            
def ultra():
    motor(1)
    mylcd.lcd_clear()
    mylcd.lcd_display_string(f"DOOR close", 2)
    mylcd.lcd_display_string(f"{sel}:ultra", 1)
    while 1:
        GPIO.setmode(GPIO.BCM)  
        GPIO.setup(PinTrig, GPIO.OUT)           
        GPIO.setup(PinEcho, GPIO.IN)
        startTime=0
        stopTime=0
        GPIO.output(PinTrig, False)    
        time.sleep(2)
        GPIO.output(PinTrig, True)          
        time.sleep(0.00001)            
        GPIO.output(PinTrig, False)         

        while GPIO.input(PinEcho) == 0:   
            startTime = time.time()
        while GPIO.input(PinEcho) == 1:   
            stopTime = time.time()

        Time_interval= stopTime - startTime     
        Distance = Time_interval * 17000
        Distance = round(Distance, 2)
        mylcd.lcd_display_string(f"{Distance}", 2)
        print ('Distance => ', Distance, 'cm')
        if int(Distance) >= 30:
            pin = DISPLAY[3]       
            FND(pin)
        elif int(Distance) >= 20:
            pin = DISPLAY[2]       
            FND(pin)
        elif int(Distance) >= 10:
            pin = DISPLAY[1]       
            FND(pin)
        elif int(Distance) < 10:
            mylcd.lcd_display_string("Door OPEN", 2)
            motor(180)
            break

def motor(a):
    
    GPIO.setmode (GPIO.BCM)           
    GPIO.setup(12, GPIO.OUT) 
    Servo=GPIO.PWM(12, 40)
    if a <= 18:
        duty_ratio = 1
    elif a == 180:
        duty_ratio = 9
    else:
        duty_ratio = float(a/18)
    
    Servo.start(0)
    print('Wating for 1 sec') 
    
    Servo.ChangeDutyCycle(duty_ratio)
    time.sleep(0.5)
        
    
    Servo.stop()
    

while 1:
    print('1 : FND \n2 : servo \n3 : Ultra')
    sel = int(input())
    
    if sel == 1:
        mylcd.lcd_clear()
        mylcd.lcd_display_string(f"{sel}:FND", 1)
        print('enter 1~9')
        f = int(input())
        mylcd.lcd_display_string(f"{f}", 2)
        pin = DISPLAY[f] 
        FND(pin)
    elif sel == 2:
        mylcd.lcd_clear()
        mylcd.lcd_display_string(f"{sel}:servo", 1)
        print('enter 0~180')
        a = int(input())
        mylcd.lcd_display_string(f"{a}", 2)
        motor(a)
    elif sel == 3:
        ultra()

        
