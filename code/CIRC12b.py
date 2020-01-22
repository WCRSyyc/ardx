"""
CIRC 12
control a three colour LED

*** important Note ***
if you are using a common anode LED on a 3.3 volt board
the LED anode should go to 3.3 volts not 5 volts as shown in the schematic.



Making it better

(1)
the three lines that control the LEDs always are always grouped together
Let's put them in a subroutine that is called from the while loop

(2)
the origional program is only capable of eight colours
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
Try printing the colours in rainbow order (not all colours will be there!)

"""


import board    #hardware details of the specific board that you are using
#import digitalio
import pulseio
import time

# LED pin array colour index values
RED = 0
GREEN = 1
BLUE = 2

#rgbPin = [ board.D3, board.D5, board.D6]  # pin numbers for Red, Green, and Blue GrandCentral
rgbPin = [ board.A1, board.A2, board.A3]  # pin numbers for Red, Green, and Blue CPX

pwmR = pulseio.PWMOut(rgbPin[RED],   frequency=50)
pwmG = pulseio.PWMOut(rgbPin[GREEN], frequency=50)
pwmB = pulseio.PWMOut(rgbPin[BLUE],  frequency=50)

REVERSER = True # reverse depending on common Anode or common cathode type LED

COLOUR_TABLE = {   # use a dictionary to map colour names to RGB values
            'Red'    : [255 , 0  , 0  ],
            'Green'  : [0   , 255, 0  ],
            'Blue'   : [0   , 0  , 255],
			'Yellow' : [255 , 255, 0  ],
			'Purple' : [255 , 0  , 255],
            'Cyan'   : [0   , 255, 255],
            'White'  : [255 , 255, 255],
            'Black'  : [0   , 0  , 0  ],
            'newclr' : [ 64, 128, 192]
            }

def map( x, in_min, in_max, out_min, out_max):
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

def set_colour(oneColour):
    #print (oneColour)
    """
    print (oneColour,
        " red=",   COLOUR_TABLE[oneColour][RED],
        " green=", COLOUR_TABLE[oneColour][GREEN],
        " blue=",  COLOUR_TABLE[oneColour][BLUE]
        )
    """
    """
    print (oneColour,
        " red=",   map(COLOUR_TABLE[oneColour][RED]   , 0,255, 0,65535),
        " green=", map(COLOUR_TABLE[oneColour][GREEN] , 0,255, 0,65535),
        " blue=",  map(COLOUR_TABLE[oneColour][BLUE]  , 0,255, 0,65535)
        )
    """
    print (oneColour,
        " red=",   hex(COLOUR_TABLE[oneColour][RED]  ),
        " green=", hex(COLOUR_TABLE[oneColour][GREEN]),
        " blue=",  hex(COLOUR_TABLE[oneColour][BLUE] )
        )

    if (REVERSER == False) : # backwards depending on common anode or common cathode LED
        pwmR.duty_cycle = int(map(COLOUR_TABLE[oneColour][RED]   , 0,255, 0,65535) )
        pwmG.duty_cycle = int(map(COLOUR_TABLE[oneColour][GREEN] , 0,255, 0,65535) )
        pwmB.duty_cycle = int(map(COLOUR_TABLE[oneColour][BLUE]  , 0,255, 0,65535) )
    else :
        pwmR.duty_cycle = int(map(COLOUR_TABLE[oneColour][RED]   , 0,255, 65535, 0) )
        pwmG.duty_cycle = int(map(COLOUR_TABLE[oneColour][GREEN] , 0,255, 65535, 0) )
        pwmB.duty_cycle = int(map(COLOUR_TABLE[oneColour][BLUE]  , 0,255, 65535, 0) )

#rainbow = ['Red', 'orange', 'Yellow', 'Green', 'Blue', 'indigo', 'violet']
rainbow = ['Red', 'Yellow', 'Green', 'Blue', 'Purple']

while True:

    for myColour in COLOUR_TABLE:
        #print (myColour, COLOUR_TABLE[myColour] )

        set_colour(myColour)
        time.sleep(2.0)

        # some black time between colours.
        set_colour("Black")
        time.sleep(1.0)

    print ('rainbow')
    for myColour in rainbow:
        set_colour(myColour)
        time.sleep(2.0)

    set_colour("Black")
    time.sleep(1.0)