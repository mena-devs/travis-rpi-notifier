# hw_leds : Hardware LEDs
# Enum class for mapping the LED colors to the
# connected pins on the rPI Board
#

from enum import IntEnum, unique

@unique
class hwLeds(IntEnum):
    """
    Enumeration of the default pins used per LED color
    """
    RED     = 26
    GREEN   = 19
    BLUE    = 13