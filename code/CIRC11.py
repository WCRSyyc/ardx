"""
CIRC 11

use the same code as CIRC01 just change the output pin from D13 to D2 
or whatever pin the resistor on the base of the transistor is connected to.

The change is that instead of controlling a LED, you are using a transistor to control a relay.

Note: The relay should still be connected to 5 volts 
(or whatever the voltage rating of the relay is)
even if you are using a 3.3 volt board.

If you are using a 3.3 volt board, you should drop the base resistor 
from 2.2 K ohm down to a 1.2K ohm resistor 
(or a 1K ohm resistor or two 560 ohm resistors in series whatever you have available).
This because the output from the pin will only go to a 3.3 volt high instead 
of 5 volts the way it would on a 5 volt board, and we want to be sure the 
transistor gets fully turned on (saturated).

"""