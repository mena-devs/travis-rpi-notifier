#!/usr/bin/python3
#
# service
#

import yaml
import time
import logging
from notifier.hwLeds import hwLeds as LED
from notifier.hwController import hwController

if __name__ == '__main__':
    logging.basicConfig(format='%(asctime)s - %(levelname)s: %(message)s', 
                        datefmt='%H:%M:%S',
                        level=logging.DEBUG)

    hw_controller_inst = hwController()

    hw_controller_inst.led_on(LED.BLUE)
    time.sleep(1)
    hw_controller_inst.led_off(LED.BLUE)
    time.sleep(1)
    hw_controller_inst.led_blink(LED.RED, 0.1, 10)
    time.sleep(1)
    hw_controller_inst.turn_all_on()
    time.sleep(3)
    hw_controller_inst.turn_all_off()
