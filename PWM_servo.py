import RPi.GPIO as GPIO 
import time

DISPLAY = [0x3F,0x06,0x5B,0x4F,0x66,0x6D,0x7D,0x07,0x7F,0x67]          
PIN = [13,6,16,20,21,19,26]
NUM = [0x01,0x02,0x04,0x08,0x10,0x20,0x40,0x80]

GPIO.setwarnings(False)            


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
    duty_ratio = a
    
    Servo.start(0)
    print('Wating for 1 sec') 
    time.sleep(1) 
    
    Servo.ChangeDutyCycle(duty_ratio)
    time.sleep(1)
        
    
    Servo.stop()
    GPIO.cleanup()
    print('Everythings cleanup')

while 1:
    print('enter 1~9')
    x = 0
    x = int(input())
    pin = DISPLAY[x]       
    PORT(pin)
    a = int(x)
    main(a)

