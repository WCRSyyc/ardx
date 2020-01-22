## 74hc595 testing
## https://learn.adafruit.com/circuitpython-basics-i2c-and-spi/spi-devices
## https://circuitpython.readthedocs.io/projects/busdevice/en/latest/api.html

import board    #hardware details of the specific board that you are using
import busio
import digitalio
from board import *
from adafruit_bus_device.spi_device import SPIDevice
import time

with busio.SPI(SCK, MOSI, MISO) as spi_bus:
  cs = digitalio.DigitalInOut(D5)    # chip select == Latch_pin == 74hc595 pin 12
  device = SPIDevice(spi_bus, cs)

                         # show which pins are these on
  print("sck  ", SCK)    # 74hc595 pin 11
  print("mosi ", MOSI)   # 74hc595 pin 14
  print("miso ", MISO)   # not used


  bytes_read  = bytearray(4)    # read buffer
  bytes_write = bytearray(1)    # one byte buffer for write data
    # The object assigned to spi in the with statements below
    # is the original spi_bus object. We are using the busio.SPI
    # operations busio.SPI.readinto() and busio.SPI.write().
  while True:
    for testData in range(256):   # for an example lets transmit all values 0 to 255 one at a time.
      bytes_write[0] = testData   # put one byte in the transmit buffer

#    with device as spi:          # this shift register is write only
#      spi.readinto(bytes_read)   # so no read

    # A second transaction

      #print(testData)             # debugging info
      with device as spi:         # the shift register
        spi.write(bytes_write)    # send one byte (bytearray is only one byte long)

      time.sleep(0.1)             # pause after each write

    print("looping")