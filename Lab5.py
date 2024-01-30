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

# GPIO pins for buttons
BUTTONS = [18, 19, 20, 21]

# Initialize buttons
GPIO.setmode(GPIO.BCM)
for button in BUTTONS:
    GPIO.setup(button, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

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

# Generate a random target number between 1 and 4
target_number = random.randint(1, 4)

# Game loop
while True:
    lcd_byte(LCD_LINE_1, LCD_CMD)
    message = "Guess the Button"
    for char in message:
        lcd_byte(ord(char), LCD_CHR)

    # Get player input
    player_guess = None
    for idx, button in enumerate(BUTTONS):
        if GPIO.input(button) == 1:
            player_guess = idx + 1
            break

    # Check player's guess
    if player_guess is not None:
        lcd_clear()
        if player_guess == target_number:
            lcd_byte(LCD_LINE_1, LCD_CMD)
            congratulations_message = "Congratulations!"
            for char in congratulations_message:
                lcd_byte(ord(char), LCD_CHR)
            lcd_byte(LCD_LINE_2, LCD_CMD)
            guessed_message = "You guessed it!"
            for char in guessed_message:
                lcd_byte(ord(char), LCD_CHR)
        else:
            lcd_byte(LCD_LINE_1, LCD_CMD)
            wrong_guess_message = "Wrong guess."
            for char in wrong_guess_message:
                lcd_byte(ord(char), LCD_CHR)
            lcd_byte(LCD_LINE_2, LCD_CMD)
            correct_answer_message = ("Answer is: " + str(target_number)) 
            for char in correct_answer_message:
                lcd_byte(ord(char), LCD_CHR)
            time.sleep(2)
        # Reset player's guess
        player_guess = None

        # Generate a new random target number
        target_number = random.randint(1, 4)

        # Wait for a moment before clearing the LCD
        time.sleep(2)
        lcd_clear()
