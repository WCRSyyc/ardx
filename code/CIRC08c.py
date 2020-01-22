# CIRC08 read Analogue in
import time
import board
import digitalio
from analogio import AnalogIn
import pulseio
import adafruit_motor.servo

#led = digitalio.DigitalInOut(board.D13)
#led.direction = digitalio.Direction.OUTPUT

pwm = pulseio.PWMOut(board.D6, frequency=50)
                    # may have to tweak the min and max to match individual servos
my_servo = adafruit_motor.servo.Servo(pwm, min_pulse=600, max_pulse=2500)

analog_in = AnalogIn(board.A1)


def get_voltage(pin):
#    print("def "+ str(pin.value))      # pin.value is an integer from 0 to 65535
    return (pin.value * 3.3) / 65536    # assumes a 3.3 volt reference_voltage
                                        # calculation returns actual voltage on the pin


while True:
    pot_voltage = get_voltage(analog_in)    # 3.3 volts from the pot max
#    print((pot_voltage, ))   #if you are using MU : try the plotter !
#    print((pot_voltage * 180/3.3, ))    # 180 degrees of servo rotation
#    if(pot_voltage > 2.0):         # light the LED if the voltage gets too high
#        led.value = True           # 2.0 volts for example
#    else:
#        led.value = False
    my_servo.angle = pot_voltage * 180/3.3  # 3.3 is A to D reference voltage
                                            # 3.3 Volts is also pot max voltage.
                                            # because there is no seperate reference here
                                            # the Arduino uses the suply voltage
    time.sleep(0.1)