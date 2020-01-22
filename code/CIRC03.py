"""
CIRC03
control a motor speed

Note the motor goes to 5 volts even though this is a 3.3 volt board.

If you are using a 3.3 volt board, you should drop the base resistor 
from 2.2 K ohm down to a 1.2K ohm resistor 
(or a 1K ohm resistor or two 560 ohm resistors in series whatever you have available).
This because the output from the pin will only go to a 3.3 volt high instead 
of 5 volts the way it would on a 5 volt board, and we want to be sure the 
transistor gets fully turned on (saturated).

"""

import board
import pulseio
import time

pwm = pulseio.PWMOut(board.D9, frequency=50)

while True:                           # cycle up and down then repeat
  for x in range(0, 65535, 2048):     # pwm range is 0 to 65535
                                      # range(start, stop, step)
                                      # 65535 / 2048 = 32 steps
#    print (str(x))                   # print the current speed
    pwm.duty_cycle = x                # set new speed
    time.sleep(0.5)                   # do nothing for time in seconds

  for x in range(65535, 0, -2048):    # step down back to 0
#    print (str(x))
    pwm.duty_cycle = x
    time.sleep(0.5)