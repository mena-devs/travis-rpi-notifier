#!/usr/bin/python
# hwController: Hardware Controller
# a layer of abstraction on top of the gpio
# library that encapsulates all the hardware
# instructions
#

import time
import RPi.GPIO as GPIO
from notifier.hwLeds import hwLeds as LED

class hwController:

    def __init__(self):
        # The advantage of using the BOARD system is that 
        # your hardware will always work, regardless of the 
        # board revision of the RPi
        GPIO.setmode(GPIO.BCM)
        # Blue connected to GPIO.13
        # Green connected to GPIO.19
        # Red connected to GPIO.26
        self.channels_list = [13,19,26]
        # Set the GPIO pins to OUT mode and low voltage
        GPIO.setup(self.channels_list, GPIO.OUT, initial=GPIO.LOW)

    def __del__(self):
        """
        It's important to cleanup after we're done and reset
        the GPIO pins to their default modes/states. This cleanup is
        for all channels not the set we have specified in the
        contructor
        """
        GPIO.cleanup()

    def blue_on(self):
        """
        Turn on the Blue LED
        """
        if not GPIO.input(13):
            GPIO.output(13, GPIO.HIGH)

    def blue_off(self):
        """
        Turn off the Blue LED
        """
        if GPIO.input(13):
            GPIO.output(13, GPIO.LOW)


if __name__ == "__main__":
    hw_controller_inst = hwController()
    hw_controller_inst.blue_on()
    time.sleep(1)
    hw_controller_inst.blue_off()
