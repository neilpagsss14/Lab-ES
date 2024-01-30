import time
import random
import RPi.GPIO as GPIO
import smbus

# LCD Configuration
I2C_ADDR = 0x27
I2C_BUS = 1
LCD_WIDTH = 21

# LCD Commands
LCD_CLEAR = 0x01

# LCD Lines
LCD_LINE_1 = 0x80
LCD_LINE_2 = 0xC0

# Initialize LCD
bus = smbus.SMBus(I2C_BUS)

# Define some device parameters
LCD_CHR = 1
LCD_CMD = 0

LCD_BACKLIGHT = 0x08
ENABLE = 0b00000100

# Timing constants
E_PULSE = 0.0005
E_DELAY = 0.0005


# Function to send commands to the LCD
def lcd_byte(bits, mode):
    bits_high = mode | (bits & 0xF0) | LCD_BACKLIGHT
    bits_low = mode | ((bits << 4) & 0xF0) | LCD_BACKLIGHT

    bus.write_byte(I2C_ADDR, bits_high)
    lcd_toggle_enable(bits_high)

    bus.write_byte(I2C_ADDR, bits_low)
    lcd_toggle_enable(bits_low)

# Function to toggle enable
def lcd_toggle_enable(bits):
    time.sleep(E_DELAY)
    bus.write_byte(I2C_ADDR, (bits | ENABLE))
    time.sleep(E_PULSE)
    bus.write_byte(I2C_ADDR, (bits & ~ENABLE))
    time.sleep(E_DELAY)

# Function to clear the LCD display
def lcd_clear():
    lcd_byte(LCD_CLEAR, LCD_CMD)
    time.sleep(2)

# Initialize LCD
lcd_byte(0x33, LCD_CMD)
lcd_byte(0x32, LCD_CMD)
lcd_byte(0x06, LCD_CMD)
lcd_byte(0x0C, LCD_CMD)
lcd_byte(0x28, LCD_CMD)
lcd_clear()  # Clear the LCD initially

passcode = "6859"
password = ""
serInput = ""

# Keypad
L1 = 17
L2 = 27
L3 = 22
L4 = 23
C1 = 24
C2 = 25
C3 = 5
C4 = 6

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(L1, GPIO.OUT)
GPIO.setup(L2, GPIO.OUT)
GPIO.setup(L3, GPIO.OUT)
GPIO.setup(L4, GPIO.OUT)

GPIO.setup(C1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(C2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(C3, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(C4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

def readLine(line, characters):
    GPIO.output(line, GPIO.HIGH)
    if(GPIO.input(C1) == 1):
        concatPass(characters[0])
        time.sleep(0.5)
    if(GPIO.input(C2) == 1):
        concatPass(characters[1])
        time.sleep(0.5)
    if(GPIO.input(C3) == 1):
        concatPass(characters[2])
        time.sleep(0.5)
    if(GPIO.input(C4) == 1):
        concatPass(characters[3])
        time.sleep(0.5)
    GPIO.output(line, GPIO.LOW)
    
def concatPass(character):
    global password
    password = password + character
    lcd_byte(LCD_LINE_2, LCD_CMD)
    for char in password:
        lcd_byte(ord(char), LCD_CHR)
    
def messageShow(message):
    if len(message) > 16:
        firstMessage = message[:16]
        secondMessage = message[16:]
        lcd_byte(LCD_LINE_1, LCD_CMD)
        for char in firstMessage:
            lcd_byte(ord(char), LCD_CHR)
        lcd_byte(LCD_LINE_2, LCD_CMD)
        for char in secondMessage:
            lcd_byte(ord(char), LCD_CHR)
    else:
        lcd_byte(LCD_LINE_1, LCD_CMD)
        for char in message:
            lcd_byte(ord(char), LCD_CHR)
        
try:
    while True:
        lcd_byte(LCD_LINE_1, LCD_CMD)
        message = "Enter password: "
        for char in message:
            lcd_byte(ord(char), LCD_CHR)
        if len(password) < 4:
            readLine(L1, ["1","2","3","A"])
            readLine(L2, ["4","5","6","B"])
            readLine(L3, ["7","8","9","C"])
            readLine(L4, ["*","0","#","D"])
            time.sleep(0.1)
        elif len(password) == 4:
            if password == passcode:
                lcd_byte(LCD_LINE_2, LCD_CMD)
                message = "Correct Password"
                for char in message:
                    lcd_byte(ord(char), LCD_CHR)
                time.sleep(0.1)
                serInput = input()
                lcd_clear()
                time.sleep(0.1)
                messageShow(serInput)
                time.sleep(2)
            else:
                lcd_byte(LCD_LINE_2, LCD_CMD)
                message = "Try again"
                for char in message:
                    lcd_byte(ord(char), LCD_CHR)
                password = ""
                time.sleep(1)
                lcd_clear()
        else:
            password = ""
            time.sleep(1)
            lcd_clear()
        
except KeyboardInterrupt:
    print("\nApplication stopped!")
