import board    #hardware details of the specific board that you are using
import digitalio
import time

led = digitalio.DigitalInOut(board.D13)
led.direction = digitalio.Direction.OUTPUT

while True:
    led.value = True
    time.sleep(1.0)
    led.value = False
    time.sleep(1.0)