import time
from statistics import median

import RPi.GPIO as GPIO
from hx711 import HX711

try:
    hx711_1 = HX711(
        dout_pin=5,
        pd_sck_pin=6,
        channel='A',
        gain=64
    )

    hx711_2 = HX711(
        dout_pin=13,
        pd_sck_pin=19,
        channel='A',
        gain=64
    )

    hx711_1.reset()   # Before we start, reset the HX711 (not obligate)
    hx711_2.reset()   # Before we start, reset the HX711 (not obligate)

    while True:
        measures1 = hx711_1.get_raw_data(3)
        measures2 = hx711_2.get_raw_data(3)
        print('1:', median(measures1), '     2:', median(measures2))
        time.sleep(0.5)

finally:
    GPIO.cleanup()  # always do a GPIO cleanup in your scripts!
