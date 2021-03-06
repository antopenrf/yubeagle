import Adafruit_BBIO.GPIO as GPIO
import Adafruit_BBIO.SPI as SPI



GPIO.setup("P9_11", GPIO.OUT)
GPIO.setup("P9_13", GPIO.OUT)
spi = SPI.SPI(0, 0)


def init4159():
    GPIO.output("P9_11", GPIO.LOW)
    GPIO.output("P9_13", GPIO.LOW)
    spi.xfer2([0x00, 0x00, 0x00, 0x07])
    spi.xfer2([0x00, 0x00, 0x3e, 0x86])
    spi.xfer2([0x00, 0x80, 0x3e, 0x86])
    spi.xfer2([0x00, 0x12, 0x8f, 0x75])
    spi.xfer2([0x00, 0x92, 0x8f, 0x75])
    spi.xfer2([0x00, 0x18, 0x00, 0x84])
    spi.xfer2([0x00, 0x18, 0x00, 0xc4])
    spi.xfer2([0x00, 0x63, 0x04, 0x83])
    spi.xfer2([0x00, 0x40, 0x81, 0x92])
    spi.xfer2([0x00, 0x00, 0x00, 0x01])
    spi.xfer2([0xb0, 0x36, 0x60, 0x00])

def set4159():
    GPIO.output("P9_11", GPIO.LOW)
    GPIO.output("P9_13", GPIO.LOW)
    spi.xfer2([0x00, 0x00, 0x00, 0x07])
    spi.xfer2([0x00, 0x00, 0x3e, 0x86])
    spi.xfer2([0x00, 0x12, 0x8f, 0x75])
    spi.xfer2([0x00, 0x78, 0x00, 0x84])
    spi.xfer2([0x00, 0x63, 0x04, 0x83])
    spi.xfer2([0x00, 0x40, 0x81, 0x92])
    spi.xfer2([0x00, 0x00, 0x00, 0x01])
    spi.xfer2([0xf8, 0x36, 0x60, 0x00])

def init4355():
    GPIO.output("P9_11", GPIO.LOW)
    GPIO.output("P9_11", GPIO.HIGH)
    print(spi.xfer2([0x00, 0x01, 0x04, 0x1c]))
    spi.xfer2([0x00, 0x61, 0x30, 0x0b])
    spi.xfer2([0x00, 0xc0, 0x3e, 0xba])
    spi.xfer2([0x3f, 0x40, 0x2c, 0x89])
    spi.xfer2([0x10, 0x2d, 0x04, 0x28])
    spi.xfer2([0x10, 0x00, 0x00, 0x17])
    spi.xfer2([0x15, 0x1f, 0xe0, 0x76])
    spi.xfer2([0x00, 0x80, 0x00, 0x25])
    spi.xfer2([0x30, 0x01, 0x09, 0x84])
    spi.xfer2([0x00, 0x00, 0x00, 0x03])
    spi.xfer2([0x00, 0x00, 0x40, 0x02])
    spi.xfer2([0x00, 0x20, 0x00, 0x01])

def set4355():
    GPIO.output("P9_11", GPIO.LOW) 
    GPIO.output("P9_13", GPIO.HIGH)
    spi.xfer2([0x00, 0x20, 0x06, 0x40])
    spi.xfer2([0x30, 0x00, 0x89, 0x84])
    spi.xfer2([0x00, 0x00, 0x40, 0x02])
    spi.xfer2([0x00, 0x00, 0x00, 0x01])
    spi.xfer2([0x00, 0x20, 0x03, 0x20])

def select8282a():
    GPIO.output("P9_11", GPIO.HIGH)
    GPIO.output("P9_13", GPIO.LOW)

def select8282b():
    GPIO.output("P9_11", GPIO.HIGH)
    GPIO.output("P9_13", GPIO.HIGH)

def set8282():
    spi.xfer2([0x00, 0x00, 0x00])
    spi.xfer2([0x00, 0x10, 0x20])
    spi.xfer2([0x00, 0x11, 0x20])
    spi.xfer2([0x00, 0x14, 0x00])
    spi.xfer2([0x00, 0x15, 0x0f])
    spi.xfer2([0x00, 0x17, 0x03])
    spi.xfer2([0x00, 0x18, 0x00])

def setall():
    init4355()
    set4355()
    init4159()
    set4159()
    select8282a()
    set8282()
    select8282b()
    set8282()
    GPIO.cleanup()
    spi.close()


