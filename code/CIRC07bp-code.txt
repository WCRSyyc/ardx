## CIRC07 read pushbutton # one to turn on and one to turn off # pull up resistors needed
import time

import board
import digitalio

button_a = digitalio.DigitalInOut(board.D2)
button_a.direction = digitalio.Direction.INPUT
#button_a.pull = digitalio.Pull.DOWN

button_b = digitalio.DigitalInOut(board.D3)
button_b.direction = digitalio.Direction.INPUT
#button_b.pull = digitalio.Pull.DOWN

led = digitalio.DigitalInOut(board.D13)
led.direction = digitalio.Direction.OUTPUT

while True:
#    print ( str(button_a.value) + ' ' +  str(button_b.value) )
    if (button_a.value == False):
        led.value = True

    if (button_b.value == False):
        led.value = False
    time.sleep(0.1)