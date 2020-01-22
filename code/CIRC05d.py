# CIRC05 Shift register


import board
import adafruit_74hc595
import busio
import digitalio
import time

pins = []

print("SCK  " + str(board.SCK))
print("MOSI " + str(board.MOSI))

spi = busio.SPI(board.SCK, MOSI=board.MOSI)
#spi = busio.SPI(board.D3, MOSI=board.D2)

latch_pin = digitalio.DigitalInOut(board.D5)
#latch_pin = digitalio.DigitalInOut(board.D4)
sr = adafruit_74hc595.ShiftRegister74HC595(spi, latch_pin)

for hardwarepin in range(8):
  pin = sr.get_pin(hardwarepin)
  pins.append(pin)

while True:
  for thispin in pins:
    thispin.value = True
    time.sleep(1)

  for thispin in pins:
    thispin.value = False
    time.sleep(1)

  print("looping")