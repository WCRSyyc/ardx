# CIRC05 Shift register


import board
import adafruit_74hc595
import busio
import digitalio
import time

print("SCK  " + str(board.SCK))    # what pins is this?
print("MOSI " + str(board.MOSI))   # what pins is this?

spi = busio.SPI(board.SCK, MOSI=board.MOSI)
latch_pin = digitalio.DigitalInOut(board.D5)

sr = adafruit_74hc595.ShiftRegister74HC595(spi, latch_pin)

while True:                    # do it forever

  for outval in range(256):    # example data is a count from 0 to 255 (8 bit only)
    sr.gpio = outval           # send it to the shift register
    print(hex(sr.gpio))        # print what we sent for debug
    time.sleep(0.1)            # pause between sends

  print("looping")             # debug info