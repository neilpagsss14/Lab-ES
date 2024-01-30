import RPi.GPIO as GPIO
import time
# GPIO pins for leds
nsg_pin = 22
nsy_pin = 23
nsr_pin = 24
weg_pin = 27
wey_pin = 25
wer_pin = 26
# 7 segment
segments_pins = [1, 2, 3, 4, 5, 6, 7]
# Pin states for each digit to display numbers 0-9
number_map = [
[0, 0, 0, 0, 1, 1, 1], # 7
[1, 1, 1, 1, 1, 0, 1], # 6               
[1, 1, 0, 1, 1, 0, 1], # 5 
[1, 1, 0, 0, 1, 1, 0], # 4
[0, 1, 0, 1, 1, 1, 1], # 3
[0, 1, 1, 1, 0, 1, 1], # 2
[0, 0, 0, 0, 1, 1, 0], # 1

]
# Initialize GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(nsg_pin, GPIO.OUT)
GPIO.setup(nsy_pin, GPIO.OUT)
GPIO.setup(nsr_pin, GPIO.OUT)
GPIO.setup(weg_pin, GPIO.OUT)
GPIO.setup(wey_pin, GPIO.OUT)
GPIO.setup(wer_pin, GPIO.OUT)
segments = [GPIO.setup(pin, GPIO.OUT) for pin in segments_pins]
def display_number(number):
    segments_values = number_map[number]
    for i in range(len(segments)):
        GPIO.output(segments_pins[i], segments_values[i])
def off_lights():
    GPIO.output(nsg_pin, GPIO.LOW)
    GPIO.output(nsy_pin, GPIO.LOW)
    GPIO.output(nsr_pin, GPIO.LOW)
    GPIO.output(weg_pin, GPIO.LOW)
    GPIO.output(wey_pin, GPIO.LOW)
    GPIO.output(wer_pin, GPIO.LOW)
def s0():
    GPIO.output(weg_pin, GPIO.HIGH)
    GPIO.output(wer_pin, GPIO.LOW)
    GPIO.output(wey_pin, GPIO.LOW)
    GPIO.output(nsg_pin, GPIO.LOW)
    GPIO.output(nsy_pin, GPIO.LOW)
    GPIO.output(nsr_pin, GPIO.HIGH)
    display_number(0)
    time.sleep(1)
    display_number(1)
    time.sleep(1)
    display_number(2)
    time.sleep(1)
    display_number(3)
    time.sleep(1)
    display_number(4)
    time.sleep(1)
    display_number(5)
    time.sleep(1)
    display_number(6)
    time.sleep(1)

def s1():
    GPIO.output(weg_pin, GPIO.LOW)
    GPIO.output(wer_pin, GPIO.LOW)
    GPIO.output(wey_pin, GPIO.HIGH)
    GPIO.output(nsg_pin, GPIO.LOW)
    GPIO.output(nsy_pin, GPIO.LOW)

    GPIO.output(nsr_pin, GPIO.HIGH)
    display_number(5)
    time.sleep(1)
    display_number(6)
    time.sleep(1)
def s2():
    GPIO.output(weg_pin, GPIO.LOW)
    GPIO.output(wer_pin, GPIO.HIGH)
    GPIO.output(wey_pin, GPIO.LOW)
    GPIO.output(nsg_pin, GPIO.LOW)
    GPIO.output(nsy_pin, GPIO.LOW)
    GPIO.output(nsr_pin, GPIO.HIGH)
    display_number(5)
    time.sleep(1)
    display_number(6)
    time.sleep(1)

def s3():
    GPIO.output(weg_pin, GPIO.LOW)
    GPIO.output(wer_pin, GPIO.HIGH)
    GPIO.output(wey_pin, GPIO.LOW)
    GPIO.output(nsg_pin, GPIO.HIGH)
    GPIO.output(nsy_pin, GPIO.LOW)
    GPIO.output(nsr_pin, GPIO.LOW)
    display_number(0)
    time.sleep(1)
    display_number(1)
    time.sleep(1)
    display_number(2)
    time.sleep(1)
    display_number(3)
    time.sleep(1)
    display_number(4)
    time.sleep(1)
    display_number(5)
    time.sleep(1)
    display_number(6)
    time.sleep(1)

def s4():
    GPIO.output(weg_pin, GPIO.LOW)
    GPIO.output(wer_pin, GPIO.HIGH)
    GPIO.output(wey_pin, GPIO.LOW)
    GPIO.output(nsg_pin, GPIO.LOW)
    GPIO.output(nsy_pin, GPIO.HIGH)
    GPIO.output(nsr_pin, GPIO.LOW)

    display_number(5)
    time.sleep(1)
    display_number(6)
    time.sleep(1)
def s5():
    GPIO.output(weg_pin, GPIO.LOW)
    GPIO.output(wer_pin, GPIO.HIGH)
    GPIO.output(wey_pin, GPIO.LOW)
    GPIO.output(nsg_pin, GPIO.LOW)
    GPIO.output(nsy_pin, GPIO.LOW)
    GPIO.output(nsr_pin, GPIO.HIGH)
    display_number(5)
    time.sleep(1)
    display_number(6)
    time.sleep(1)
try:
    while True:
        s0()
        s1()
        s2()
        s3()
        s4()
        s5()
except KeyboardInterrupt:
    GPIO.cleanup()
