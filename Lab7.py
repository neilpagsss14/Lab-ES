import RPi.GPIO as GPIO
import time

redPin = 22
greenPin = 27
bluePin = 17
sensor = 23
GPIO.setmode(GPIO.BCM)
GPIO.setup(redPin,GPIO.OUT)
GPIO.setup(greenPin,GPIO.OUT)
GPIO.setup(bluePin,GPIO.OUT)
GPIO.setup(sensor, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def turnOff(ev=None):
    GPIO.output(redPin,GPIO.HIGH)
    GPIO.output(greenPin,GPIO.HIGH)
    GPIO.output(bluePin,GPIO.HIGH)
    
def red():
    GPIO.output(redPin,GPIO.LOW)
    GPIO.output(greenPin,GPIO.HIGH)
    GPIO.output(bluePin,GPIO.HIGH)

def green(ev=None):
    GPIO.output(redPin,GPIO.HIGH)
    GPIO.output(greenPin,GPIO.LOW)
    GPIO.output(bluePin,GPIO.HIGH)
    time.sleep(3)

    
GPIO.add_event_detect(sensor, GPIO.BOTH, callback=green, bouncetime=100)

while True:
    red()
    time.sleep(3)
