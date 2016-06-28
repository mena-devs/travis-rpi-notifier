# hw_leds : Hardware LEDs
# Enum class for mapping the LED colors to the
# connected pins on the rPI Board
#

from enum import Enum, unique

@unique
class hwLeds(Enum):
    """
    Enumeration of the default pins used per LED color
    """
    RED     = 26
    GREEN   = 19
    BLUE    = 13

    def __init__(self, red_pin=26, green_pin=19, blue_pin=13):
        self.RED = red_pin
        self.GREEN = green_pin
        self.BLUE = blue_pin

    def channels_list(self):
        """
        List of channel pin numbers
        """
        return [self.RED, self.GREEN, self.BLUE]