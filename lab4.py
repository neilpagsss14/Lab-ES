import busio
import digitalio
import board
import adafruit_mcp3xxx.mcp3008 as MCP
from adafruit_mcp3xxx.analog_in import AnalogIn
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM) # Define LED pins
LED1=21
LED2=22
LED3=24

# Set LED pins as outputs
GPIO.setup(LED1, GPIO.OUT)
GPIO.setup(LED2, GPIO.OUT)
GPIO.setup(LED3, GPIO.OUT)

# create the spi bus
spi = busio.SPI(clock=board.SCK, MISO=board.MISO, MOSI=board.MOSI)

# create the cs (chip select)
cs = digitalio.DigitalInOut(board.D5)

# create the mcp object
mcp = MCP.MCP3008(spi, cs)

# create an analog input channel on pin 0
chan = AnalogIn(mcp, MCP.P1)

def ledstate0():
    GPIO.output(LED1, GPIO.LOW)
    GPIO.output(LED2, GPIO.LOW)
    GPIO.output(LED3, GPIO.LOW)

def ledstate1():
    GPIO.output(LED1, GPIO.HIGH)
    GPIO.output(LED2, GPIO.LOW)
    GPIO.output(LED3, GPIO.LOW)


def ledstate2():
    GPIO.output(LED1, GPIO.HIGH)
    GPIO.output(LED2, GPIO.HIGH)
    GPIO.output(LED3, GPIO.LOW)
    
    
def ledstate3():
    GPIO.output(LED1, GPIO.HIGH)
    GPIO.output(LED2, GPIO.HIGH)
    GPIO.output(LED3, GPIO.HIGH)

while True:
    GPIO.output(LED1, GPIO.HIGH)
    GPIO.output(LED2, GPIO.HIGH)
    GPIO.output(LED3, GPIO.HIGH)
    if chan.voltage < 0.1:
        ledstate0()
        print("ADC Voltage: " + str(chan.voltage) + "V")
        time.sleep(1)
    if 0.1 < chan.voltage < 1.1:
        ledstate1()
        print("ADC Voltage: " + str(chan.voltage) + "V")
        time.sleep(1)
    if 1.1 < chan.voltage < 2.2:
        ledstate2()
        print("ADC Voltage: " + str(chan.voltage) + "V")
        time.sleep(1)
    if chan.voltage > 2.2:
        ledstate3()
        print("ADC Voltage: " + str(chan.voltage) + "V")
        time.sleep(1)
