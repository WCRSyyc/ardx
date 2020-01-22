# CIRC09 read Analogue in from photo resistor
import time
import board
import digitalio
from analogio import AnalogIn
import pulseio
import adafruit_motor.servo

led = digitalio.DigitalInOut(board.D13)
led.direction = digitalio.Direction.OUTPUT
pwm = pulseio.PWMOut(board.D6, frequency=50)
                    # may have to tweak the min and max to match individual servos
my_servo = adafruit_motor.servo.Servo(pwm, min_pulse=600, max_pulse=2500)

analog_in = AnalogIn(board.A1)

def get_light(pin):
#    print("def "+ str(pin.value))      # pin.value is an integer from 0 to 65535
    return pin.value * 3.3 / 65536

while True:
    lightLevel = get_light(analog_in)
    #    print((lightLevel, ))   #if you are using MU : try the plotter !
#    print((lightLevel * 180/3.3, ))    # 180 degrees of servo rotation
    if(lightLevel > 1.0):         # light the LED if the voltage above threshold
        led.value = True           # 1.0 volts for example
    else:
        led.value = False

    if (lightLevel > 2):        # constrain the levels to 0 -> 2
        lightLevel = 2.0
    if (lightLevel < 0):
        lightlevel = 0

#    print(lightLevel * 180/2.0)
    my_servo.angle = lightLevel * 180/2.0  # 3.3 is A to D reference voltage
                                            # 3.3 Volts is also max voltage on ana pin.
                                            # because there is no seperate reference here
                                            # the Arduino uses the suply voltage

    time.sleep(0.1)