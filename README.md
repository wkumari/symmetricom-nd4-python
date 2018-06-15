This small program uses a Raspberry Pi Zero W to drive the display portion
of a Symmetricom ND-4 display ([manual](http://www1.symmetricom.com/media/files/support/ttm/product-manual/ND_um.pdf))

![ND4 Pi Clock](IMG_5100.jpg)
![ND4 with mounted Pi](IMG_5101.jpg)



This replaces the processor board of the ND-4, and powers the Pi from the
internal ND-4 power supply. The original processor board simply drives a
MAX7219 which is conveniently on the power-supply board, to the processor
board just gets unplugged and the Pi connected instead.

The wiring is as follows:

|ND-4 | MAX7219 | Function     |  Pi Pin |
|-----|---------|--------------|---------|
|VCC  |         |  VCC         |  2  |
|GND  |         |  GND         |  6  |
|PA0  |CLK      |  SPI CLK(11) |  23 |
|PA1  |LOAD/CS  |  SPI CE0(8)  |  24 |
|PA2  |DIN      |  MOSI(10)    |  19 |

All the hard work is done by Richard Hull's ```luma.led_matrix``` library from: ```https://github.com/rm-hull/luma.led_matrix```
