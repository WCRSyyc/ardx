## CIRC07 read pushbutton
import time

import board
import digitalio
import pulseio
from adafruit_debouncer import Debouncer

button_a = digitalio.DigitalInOut(board.D2)
button_a.direction = digitalio.Direction.INPUT
button_a.pull = digitalio.Pull.UP
button_ad = Debouncer(button_a)

button_b = digitalio.DigitalInOut(board.D3)
button_b.direction = digitalio.Direction.INPUT
button_b.pull = digitalio.Pull.UP
button_bd = Debouncer(button_b)

#led = digitalio.DigitalInOut(board.D9)
#led.direction = digitalio.Direction.OUTPUT
pwm = pulseio.PWMOut(board.D9, frequency=50)
pwm.duty_cycle = 0
brightness = 0
step = 2048

while True:
#    print ( str(button_a.value) + ' ' +  str(button_b.value) )
    button_ad.update()
    if (button_ad.value == False):
        brightness += step
        if(brightness > 65535):
            brightness = 65535

    button_bd.update()
    if (button_bd.value == False):
        brightness -= step
        if(brightness < 0):
            brightness = 0

    pwm.duty_cycle = brightness

#    print (brightness)
    time.sleep(0.1)