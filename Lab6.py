import busio
import digitalio
import board
import adafruit_mcp3xxx.mcp3008 as MCP
from adafruit_mcp3xxx.analog_in import AnalogIn
import RPi.GPIO as GPIO
import time
from gpiozero import PWMLED
from time import sleep
import numpy as np

GPIO.setmode(GPIO.BCM)
redLed_pin = PWMLED(21)
greenLed_pin = PWMLED(20)
blueLed_pin = PWMLED(19)

spi = busio.SPI(clock=board.SCK, MISO=board.MISO, MOSI=board.MOSI)
cs = digitalio.DigitalInOut(board.D5)
mcp = MCP.MCP3008(spi, cs)
pot = AnalogIn(mcp, MCP.P1)
vry = AnalogIn(mcp, MCP.P2)
vrx = AnalogIn(mcp, MCP.P3)

def map_value(value, vmin, vmax):
    mapped_value = (value - vmin) / (vmax - vmin)
    return np.clip(mapped_value, 0, 1)

while True:
    redLed_pin.value = map_value(pot.voltage, 0, 1)
    greenLed_pin.value = map_value(pot.voltage, 0, 1)
    blueLed_pin.value = map_value(pot.voltage, 0, 1)
    if 3.0 <= vrx.voltage <= 3.3:
        greenLed_pin.value = 0
        redLed_pin.value = 0
    elif 1.0 <= vrx.voltage < 3.0:
        redLed_pin.value = 0
        blueLed_pin.value = 0
    else:
        greenLed_pin.value = 0
        blueLed_pin.value = 0
    print("Hall Effect = {} | Potentiometer = {} | Voltage = {:.2f}v".format(vrx.voltage, pot.value, pot.voltage))
    time.sleep(0.5)
    
