import time
import RPi.GPIO as GPIO
from hx711 import HX711

try:
    hx711 = HX711(
        dout_pin=5,
        pd_sck_pin=6,
        channel='A',
        gain=64
    )

    hx711.reset()   # Before we start, reset the HX711 (not obligate)

    while True:
        measures = hx711.get_raw_data(3)
        print("  --  ".join(measures))
        time.sleep(0.2)

finally:
    GPIO.cleanup()  # always do a GPIO cleanup in your scripts!
