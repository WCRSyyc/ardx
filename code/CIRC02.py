# ARDX experiment two in Python
import board    #hardware details of the specific board that you are using
import digitalio
import time

leds = []   # create an empty list to contain led objects
#print("eight leds")

# this one for the Grand Central M4
#boardPins = [board.D2, board.D3, board.D4, board.D5,
#    board.D6, board.D7, board.D8, board.D9]  #Board pins 2 through 9

# this one for the Circuit Python Express connected to external LEDs
boardPins = [board.A0, board.A1, board.A2, board.A3,
    board.A4, board.A5, ]  #Board pins

for hardwarePin in boardPins:
    thisPin = digitalio.DigitalInOut(hardwarePin)  # create an object to hold information about a pin
    thisPin.direction = digitalio.Direction.OUTPUT  # a pin must be OUTPUT to drive an led
    leds.append(thisPin)  # add configured pin to the list

while True:    #do it forever
  for thisled in leds:  # for each single led saved in the list
    thisled.value = True  # Tell the led to turn on
    time.sleep(1.0)  # do nothing for 1 second

  for thisled in reversed(leds):
    thisled.value = False  # Turn the single led off
    time.sleep(1.0)