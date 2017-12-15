#!/usr/bin/env python
# Copyright (c) 2017 Warren Kumari

"""
This small program uses a Raspberry Pi Zero W to drive the display portion
of a Symmetricom ND-4 display.

This replaces the processor board of the ND-4, and powers the Pi from the
internal ND-4 power supply. The original processor board simply drives a
MAX7219 which is conveniently on the power-supply board, to the processor
board just gets unplugged and the Pi connected instead. 

The wiring is as follows:

ND-4  MAX7219  Function    Pi Pin
--------------------------------
VCC            VCC           2
GND            GND           6
PA0  CLK       SPI CLK(11)   23
PA1  LOAD/CS   SPI CE0(8)    24
PA2  DIN       MOSI(10)      19

All the hard work is done by Richard Hull's luma.led_matrix library from: https://github.com/rm-hull/luma.led_matrix
"""

from datetime import datetime
import time

from luma.core.interface.serial import spi, noop
from luma.core.render import canvas
from luma.core.virtual import sevensegment
from luma.led_matrix.device import max7219

# Setup the interface.
serial = spi(port=0, device=0, gpio=noop())
device = max7219(serial, cascaded=1)
seg = sevensegment(device)

# For some reason the LED display ignores the first octet.
# The colons are addressed with a period at position 8 in the string, 
# and the "point" is at 3. 
# For added entertainment, the digits are all reversed as well, so
# 17:28:31 is sent as "0013827.1"

while True:
  timestr = datetime.now().strftime('%H%M%S')
  # Reverse the time string
  revtimestr = timestr[::-1]
  paddedstr = "00" + revtimestr
  # ... and display it.
  seg.text = paddedstr

  # and now sleep around 1/2 second and redisplay with the colon on
  # to makke it "flash"
  time.sleep(0.5)
  # insert a period before last character (to get : on display)
  # Removed: add a period in spot 3 to get period to flash
  revtimestr = revtimestr[:5] + '.' + revtimestr[5:]
  paddedstr = "00" + revtimestr
  seg.text = paddedstr
  time.sleep(0.5)
