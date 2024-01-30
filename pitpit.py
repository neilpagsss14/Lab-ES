import time
import RPi.GPIO as GPIO
import matplotlib.pyplot as plt
from Adafruit_ADS1x15 import ADS1115

# Define constants
FS = 1000  # Sampling frequency (samples per second)
DURATION = 10  # Duration of the ECG signal in seconds

# Set up ADS1115 ADC
ads = ADS1115()

# Set up GPIO for pulse detection using AD8232
pulse_pin = 27
GPIO.setmode(GPIO.BCM)
GPIO.setup(pulse_pin, GPIO.IN)

def read_analog_data():
    return ads.read_adc(0, gain=1)  # Adjust gain if needed

def generate_ecg_waveform():
    # Simple square wave for demonstration
    t = [i / FS * 9000 + 1000 for i in range(int(FS * DURATION))]  # p
    ecg_signal = [0 if i % 200 < 100 else 1 for i in range(len(t))]  # q
    return t, ecg_signal  # r

def monitor_heartbeat():
    try:
        plt.ion()
        fig, axs = plt.subplots(2, 1, sharex=True, figsize=(10, 6))
        axs[0].set_title('Live Heart Monitoring')

        time_values = []
        analog_values = []

        t, ecg_signal = generate_ecg_waveform()

        # Use a rolling window for pulse detection
        window_size = 20
        analog_window = [read_analog_data() for _ in range(window_size)]

        for i in range(len(t)):
            pulse_start = time.time()
            GPIO.wait_for_edge(pulse_pin, GPIO.RISING, timeout=10)
            pulse_end = time.time()
            pulse_duration = pulse_end - pulse_start

            analog_data = read_analog_data()

            time_values.append(t[i])
            analog_values.append(analog_data)

            # Update the rolling window
            analog_window.pop(0)
            analog_window.append(analog_data)

            # Check for a significant change in average analog value
            if abs(analog_data - sum(analog_window) / window_size) > 1500 and (min_heartrate < analog_data < max_heartrate):
                print("Heartbeat detected - Analog Data:", analog_data)
                print("Abnormality Detected!")
            else:
                print("Heartbeat detected - Analog Data:", analog_data)
                print("Normal Hearrate")



            axs[0].plot(time_values, analog_values, color='b')
            axs[0].set_ylabel('ECG Signal')

            axs[1].axvline(t[i] + 0.04, color='r', linestyle='--', linewidth=2)  # T wave

            plt.draw()
            plt.pause(0.01)  # Adjust the duration if needed

    except KeyboardInterrupt:
        print("Monitoring stopped by user")
    finally:
        plt.ioff()
        plt.show(block=True)
        GPIO.cleanup()

def min_max_heartrate(age):
	max_heartrate = 220 - age
	min_heartrate = max_heartrate * 0.65

if __name__ == "__main__":
    print("Monitoring Heartbeat. Press Ctrl+C to exit.")
    print("Please input your age: ")
    age = int(input())
    min_max_heartrate(age)
    monitor_heartbeat()
    

