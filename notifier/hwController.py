#
# hwController: Hardware Controller
# a layer of abstraction on top of the gpio
# library that encapsulates all the hardware
# instructions
#

import time
import logging
import RPi.GPIO as GPIO
from notifier.hwLeds import hwLeds as LED

class hwController:

    def __init__(self):
        logging.info('Initializing...')
        # The advantage of using the BOARD system is that 
        # your hardware will always work, regardless of the 
        # board revision of the RPi
        GPIO.setmode(GPIO.BCM)
        self.channels_list = [e.value for e in LED]
        # Set the GPIO pins to OUT mode and low voltage
        GPIO.setup(self.channels_list, GPIO.OUT, initial=GPIO.LOW)
        logging.info('All channels initialized: {}'.format(self.channels_list))

    def __del__(self):
        """
        It's important to cleanup after we're done and reset
        the GPIO pins to their default modes/states. This cleanup is
        for all channels not the set we have specified in the
        contructor
        """
        GPIO.cleanup()
        logging.info('GPIO Cleanup Complete')

    def led_on(self, led_type):
        """
        Turn on LED of the passed led_type
        """
        if not GPIO.input(led_type.value):
            GPIO.output(led_type.value, GPIO.HIGH)
            logging.info('LED: {} - Status: {}'.format(led_type, GPIO.HIGH))

    def led_off(self, led_type):
        """
        Turn off LED of the passed led_type
        """
        if GPIO.input(led_type.value):
            GPIO.output(led_type.value, GPIO.LOW)
            logging.info('LED: {} - Status: {}'.format(led_type, GPIO.LOW))

    def led_blink(self, led_type, interval=1, count=5):
        """
        Blink a given LED for a specific 'count' at the frequency
        specified in 'interval' in seconds
        """
        logging.info('LED: {} - Status: Blinking {} times at {} seconds'
            .format(led_type, 
                    count, 
                    interval))
        for n in range(count):
            self.led_on(led_type)
            time.sleep(interval)
            self.led_off(led_type)
            time.sleep(interval)

    def turn_all_off(self):
        """
        Turn off all available LED colors/types
        """
        for led_type in LED:
            self.led_off(led_type)
        logging.info('LED: ALL - Status: 0')

    def turn_all_on(self):
        """
        Turn on all available LED colors/types
        """
        for led_type in LED:
            self.led_on(led_type)
        logging.info('LED: ALL - Status: 1')
