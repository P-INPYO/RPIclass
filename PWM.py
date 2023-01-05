import RPi.GPIO as GPIO
import time


GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(12,GPIO.OUT)
pwm=GPIO.PWM(12,1000)

def PWM():
    pwm.start(1)
    for i in range(99):
        pwm.ChangeDutyCycle(i+1)
        time.sleep(0.01)
    for i in range(99,0,-1):
        pwm.ChangeDutyCycle(i+1)
        time.sleep(0.01)
    pwm.stop()
    
while True:
    PWM()