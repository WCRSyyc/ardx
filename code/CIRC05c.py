# CIRC05 Shift register


import board
import adafruit_74hc595
import busio
import digitalio
import time

print("SCK  " + str(board.SCK))     # to chip pin 11
print("MOSI " + str(board.MOSI))    # to chip pin 14
print("MISO " + str(board.MISO))    # not used this time

spi = busio.SPI(board.SCK, MOSI=board.MOSI)

#latch_pin = digitalio.DigitalInOut(board.D5)  #GrandCentral    to chip pin 4
latch_pin = digitalio.DigitalInOut(board.A4)   #CPX             to chip pin 4
sr = adafruit_74hc595.ShiftRegister74HC595(spi, latch_pin)

pin0 = sr.get_pin(0)
pin1 = sr.get_pin(1)
pin2 = sr.get_pin(2)
pin3 = sr.get_pin(3)
pin4 = sr.get_pin(4)
pin5 = sr.get_pin(5)
pin6 = sr.get_pin(6)
pin7 = sr.get_pin(7)

while True:
  pin0.value = True
  time.sleep(1)
  pin1.value = True
  time.sleep(1)
  pin2.value = True
  time.sleep(1)
  pin3.value = True
  time.sleep(1)
  pin4.value = True
  time.sleep(1)
  pin5.value = True
  time.sleep(1)
  pin6.value = True
  time.sleep(1)
  pin7.value = True
  time.sleep(1)

  pin0.value = False
  time.sleep(1)
  pin1.value = False
  time.sleep(1)
  pin2.value = False
  time.sleep(1)
  pin3.value = False
  time.sleep(1)
  pin4.value = False
  time.sleep(1)
  pin5.value = False
  time.sleep(1)
  pin6.value = False
  time.sleep(1)
  pin7.value = False
  time.sleep(1)

  print("looping")