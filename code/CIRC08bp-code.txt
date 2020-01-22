# CIRC08 read Analogue in
import time
import board
import digitalio
from analogio import AnalogIn
led = digitalio.DigitalInOut(board.D13)
led.direction = digitalio.Direction.OUTPUT

analog_in = AnalogIn(board.A1)


def get_voltage(pin):
#    print("def "+ str(pin.value))      # pin.value is an integer from 0 to 65535
    return (pin.value * 3.3) / 65536    # assumes a 3.3 volt reference_voltage
                                        # calculation returns actual voltage on the pin


while True:
    pot_voltage = get_voltage(analog_in)
    print((pot_voltage,))   #if you are using MU : try the plotter !
    if(pot_voltage > 2.0):      # light the LED if the voltage gets too high
        led.value = True
    else:
        led.value = False
    time.sleep(0.1)