# CIRC05 Shift register


import board
import adafruit_74hc595
import busio
import digitalio
import time

spi = busio.SPI(board.SCK, MOSI=board.MOSI)

latch_pin = digitalio.DigitalInOut(board.D5)
sr = adafruit_74hc595.ShiftRegister74HC595(spi, latch_pin)

pin1 = sr.get_pin(1)

while True:
  pin1.value = True
  time.sleep(1)
  pin1.value = False
  time.sleep(1)
