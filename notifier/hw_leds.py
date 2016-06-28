# hw_leds : Hardware LEDs
# Enum class for mapping the LED colors to the
# connected pins on the rPI Board
#

from enum import Enum, unique

@unique
class Leds(Enum):
    """
    Enumeration of the default pins used per LED color
    """
    RED     = 26
    GREEN   = 19
    BLUE    = 13

    def __init__(self, red_pin, green_pin, blue_pin):
        self.RED = red_pin
        self.GREEN = green_pin
        self.BLUE = blue_pin

    def channels_list(self):
        """
        List of channel pin numbers
        """
        return [self.RED, self.GREEN, self.BLUE]