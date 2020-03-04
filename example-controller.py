import time
import RPi.GPIO as GPIO
from controller import ScalesController


try:
    controller = ScalesController()

    while True:
        print('Controller', controller.readings())
        time.sleep(0.5)

finally:
    GPIO.cleanup()  # always do a GPIO cleanup in your scripts!
