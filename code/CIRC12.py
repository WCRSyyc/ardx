"""
CIRC 12
control a three colour LED

*** important Note ***
if you are using a common anode LED on a 3.3 volt board
the LED anode should go to 3.3 volts not 5 volts as shown in the schematic.

"""

import board    #hardware details of the specific board that you are using
import digitalio
import time

# LED pin array colour index values
RED = 0
GREEN = 1
BLUE = 2

rgbPin = [ board.D3, board.D5, board.D6]  # pin numbers for Red, Green, and Blue GrandCentral
#rgbPin = [ board.A1, board.A2, board.A3]  # pin numbers for Red, Green, and Blue CPX


ledR = digitalio.DigitalInOut(rgbPin[RED])
ledR.direction = digitalio.Direction.OUTPUT
ledG = digitalio.DigitalInOut(rgbPin[GREEN])
ledG.direction = digitalio.Direction.OUTPUT
ledB = digitalio.DigitalInOut(rgbPin[BLUE])
ledB.direction = digitalio.Direction.OUTPUT

COLOUR_ON  = False  # reverse these depending on common Anode or common cathode type LED
COLOUR_OFF = True

COLOUR_TABLE = {   # use a dictionary to map colour names to RGB values
            'Red'    : [COLOUR_ON  , COLOUR_OFF , COLOUR_OFF],
            'Green'  : [COLOUR_OFF , COLOUR_ON  , COLOUR_OFF],
            'Blue'   : [COLOUR_OFF , COLOUR_OFF , COLOUR_ON] ,
			'Yellow' : [COLOUR_ON  , COLOUR_ON  , COLOUR_OFF],
			'Purple' : [COLOUR_ON  , COLOUR_OFF , COLOUR_ON] ,
            'Cyan'   : [COLOUR_OFF , COLOUR_ON  , COLOUR_ON] ,
            'White'  : [COLOUR_ON  , COLOUR_ON  , COLOUR_ON] ,
            'Black'  : [COLOUR_OFF , COLOUR_OFF , COLOUR_OFF]
			}

while True:

    for myColour in COLOUR_TABLE:
        #print (myColour, COLOUR_TABLE[myColour] )
        print (myColour,
            " red=", COLOUR_TABLE[myColour][RED],
            " green=", COLOUR_TABLE[myColour][GREEN],
            " blue=", COLOUR_TABLE[myColour][BLUE] )
        ledR.value = COLOUR_TABLE[myColour][RED]
        ledG.value = COLOUR_TABLE[myColour][GREEN]
        ledB.value = COLOUR_TABLE[myColour][BLUE]
        time.sleep(2.0)

        # some black time between colours.
        ledR.value = COLOUR_TABLE['Black'][RED]
        ledG.value = COLOUR_TABLE['Black'][GREEN]
        ledB.value = COLOUR_TABLE['Black'][BLUE]
        time.sleep(1.0)
		
		
"""
CIRC 12 control a three colour LED
Making it better

(1)
the three lines that control the LEDs always are always grouped together
Let's put them in a subroutine that is called from the while loop

(2)
this program is only capable of eight colours 
what if we were to:
  change the colour values from True and False the way it is here
  to zero and 255, and then
  change the led.value lines in the subroutine to something like this 
  pwm.duty_cycle = x 
  like in the LAB for motor control (CIRC03) ?
  Note: because this function expects a value between 0 and 65535, we will have to
  convert the colour values from 0-255 to 0-65535 .
    So far no difference right?
  now
  can you use values like 64, 128, and 192 ( 1/4, 1/2, and 3/4 of 255 ) 
  in the dictionary colour list to
  invent several new colours and add them to the table?
  Theoretically you have 2 to the power of 3*8 colours ! 
  The hard part is that you have to think of a new name 
  for each colour to be able to add it to the dictionary :)
  
(3)
The order the colours will be displayed in the for loop is not known 
because the order in a dictionary is not known.
How could we get the colours to come out in the order we want? Would you do it 
like we did in the pizeo LAB?
  
"""
