from luma.led_matrix.device import max7219
from luma.core.interface.serial import spi, noop
from luma.core.render import canvas
from time import sleep



def create_I_pattern():
    heart_pattern = [
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 1, 0, 0, 1, 1, 0],
        [0, 1, 1, 0, 0, 1, 1, 0],
        [0, 1, 1, 1, 1, 1, 1, 0],
        [0, 1, 1, 1, 1, 1, 1, 0],
        [0, 1, 1, 0, 0, 1, 1, 0],
        [0, 1, 1, 0, 0, 1, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0]
    ]
    return heart_pattern

def create_heart_pattern():
    I_pattern = [
        [0, 0, 0, 0, 1, 1, 0, 0],
        [0, 0, 0, 1, 1, 1, 1, 0],
        [0, 0, 1, 1, 1, 1, 1, 0],
        [0, 1, 1, 1, 1, 1, 0, 0],
        [0, 1, 1, 1, 1, 1, 0, 0],
        [0, 0, 1, 1, 1, 1, 1, 0],
        [0, 0, 0, 1, 1, 1, 1, 0],
        [0, 0, 0, 0, 1, 1, 0, 0]
    ]
    return I_pattern

def create_e_pattern():
    creeper_pattern = [
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 1, 1, 1, 1, 1, 0],
        [0, 1, 1, 1, 1, 1, 1, 0],
        [0, 1, 0, 1, 1, 0, 1, 0],
        [0, 1, 0, 1, 1, 0, 1, 0],
        [0, 1, 0, 0, 0, 0, 1, 0],
        [0, 1, 0, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0]
    ]
    return creeper_pattern

def create_s_pattern():
    smiley_pattern = [
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 1, 1, 1, 0],
        [0, 1, 0, 1, 1, 1, 1, 0],
        [0, 1, 0, 1, 1, 0, 1, 0],
        [0, 1, 0, 1, 1, 0, 1, 0],
        [0, 1, 0, 1, 1, 0, 1, 0],
        [0, 1, 1, 1, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0]
    ]
    return smiley_pattern
    
def create_smiley_pattern():
    smiley_pattern = [
        [0, 0, 1, 1, 1, 1, 0, 0],
        [0, 1, 0, 0, 0, 0, 1, 0],
        [1, 0, 0, 1, 0, 1, 0, 1],
        [1, 0, 1, 0, 0, 0, 0, 1],
        [1, 0, 1, 0, 0, 0, 0, 1],
        [1, 0, 0, 1, 0, 1, 0, 1],
        [0, 1, 0, 0, 0, 0, 1, 0],
        [0, 0, 1, 1, 1, 1, 0, 0]
    ]
    return smiley_pattern




def display_pattern(device, pattern, delay=0.5):
    for _ in range(2):  # Blink twice
        with canvas(device) as draw:
            for y, row in enumerate(pattern):
                for x, value in enumerate(row):
                    if value == 1:
                        draw.point((x, y), fill="red")
        sleep(delay)

def main():
    serial = spi(port=0, device=0, gpio=noop())
    device = max7219(serial, cascaded=1, block_orientation=90, rotate=0)

    try:
        patterns = [create_I_pattern(), create_heart_pattern(), create_e_pattern(), create_s_pattern(),
                    create_smiley_pattern()]

        while True:
            for pattern in patterns:
                display_pattern(device, pattern)
                sleep(3)  
    except KeyboardInterrupt:
        pass
    finally:
        device.cleanup()

if __name__ == "__main__":
    main()
