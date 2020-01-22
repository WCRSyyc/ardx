## CIRC07 read pushbutton  # no pull up resistors required now # two pushbuttons ramp up or down
import time

import board
import digitalio
import pulseio


#button_a = digitalio.DigitalInOut(board.D2) # GrandCentral
button_a = digitalio.DigitalInOut(board.D4) # CPX
button_a.direction = digitalio.Direction.INPUT
button_a.pull = digitalio.Pull.UP   # GrandCentral
button_a.pull = digitalio.Pull.DOWN # CPX

#button_b = digitalio.DigitalInOut(board.D3) # GrandCentral
button_b = digitalio.DigitalInOut(board.D5) # CPX
button_b.direction = digitalio.Direction.INPUT
#button_b.pull = digitalio.Pull.UP # GrandCentral
button_b.pull = digitalio.Pull.DOWN # CPX

#led = digitalio.DigitalInOut(board.D9)
#led.direction = digitalio.Direction.OUTPUT
#pwm = pulseio.PWMOut(board.D9, frequency=50)    # GrandCentral M4
pwm = pulseio.PWMOut(board.D13, frequency=50)    # CPX

pwm.duty_cycle = 0
brightness = 0
step = 2048

while True:
#    print ( str(button_a.value) + ' ' +  str(button_b.value) )
    if (button_a.value == True):  # active high in CPX version
        brightness += step
        if(brightness > 65535):
            brightness = 65535

    if (button_b.value == True):    # active high in CPX version
        brightness -= step
        if(brightness < 0):
            brightness = 0

    pwm.duty_cycle = brightness

#    print (brightness)
    time.sleep(0.1)