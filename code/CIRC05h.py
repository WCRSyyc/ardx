## 74hc595 testing
## https://learn.adafruit.com/circuitpython-basics-i2c-and-spi/spi-devices
## https://circuitpython.readthedocs.io/projects/busdevice/en/latest/api.html

import board    #hardware details of the specific board that you are using
import busio
import digitalio
from board import *
#from adafruit_bus_device.spi_device import SPIDevice
import bitbangio
import time

#   (SCK, MOSI, MISO)  sck to 74hc595 pin 11 and mosi to 74hc595 pin 14
#with bitbangio.SPI(board.D52, board.D51, None) as spi_bus:
with bitbangio.SPI(board.D3, board.D2, None) as spi_bus:

  #cs = digitalio.DigitalInOut(D5)    # chip select == Latch_pin == 74hc595 pin 12
  cs = digitalio.DigitalInOut(D4)    # chip select == Latch_pin == 74hc595 pin 12
  cs.direction = digitalio.Direction.OUTPUT
  cs.value = False

  bytes_read  = bytearray(4)    # read buffer
  bytes_write = bytearray(1)    # one byte buffer for write data

  while True:
    for testdata in range(256):   # test data is all bytes 0 to 255
      while not spi_bus.try_lock():   # wait for bus available
        pass

      bytes_write[0] = testdata    #put one byte in transmit buffer
      print(testdata)              # debugging
      spi_bus.configure(baudrate=5000000, phase=0, polarity=0)
      cs.value = False             # cs = latch
#     bytes_read = bytearray(4)    # shift register is write only
      spi_bus.write(bytes_write)
      cs.value = True
      spi_bus.unlock()

      time.sleep(0.1)   # have sent one byte
    time.sleep(2)       # have sent all testdata
    print("looping")     # let's do it again