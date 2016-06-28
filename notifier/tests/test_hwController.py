#
# test_hwController: Hardware Controller Unit Test
#

import time
import unittest

from notifier.hwLeds import hwLeds as LED
from notifier.hwController import hwController

class TesthwController(unittest.TestCase):

    def setUp(self):
        self.hwController_inst = hwController()

    def tearDown(self):
        del self.hwController_inst

    def test_leds(self):
        """
        The only test that can be done is to turn on
        all LEDs one and turn them off again
        """
        self.hwController_inst.turn_all_on()
        time.sleep(2)
        self.hwController_inst.turn_all_off()
        time.sleep(2)

if __name__ == '__main__':
    unittest.main()