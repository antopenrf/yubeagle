import Adafruit_BBIO.PWM as PWM
import Adafruit_BBIO.GPIO as GPIO
import time

##PWM.start(channel, duty, freq=2000, polarity=0)
PWM.cleanup()
PWM.start("P9_14", 0, 1, 1)
PWM.start("P9_16", 0, 1, 1)

##optionally, you can set the frequency as well as the polarity from their defaults:
##PWM.start("P9_14", 50, 1000, 1)



GPIO.setup("P9_15", GPIO.OUT)
GPIO.setup("P9_23", GPIO.OUT)
GPIO.setup("P9_28", GPIO.OUT)
GPIO.setup("P9_27", GPIO.OUT)

sequence = ["P9_15", "P9_23", "P9_28", "P9_27"]

for k in range(200):
    GPIO.output(sequence[     k % 4], GPIO.HIGH)
    GPIO.output(sequence[ (k+1) % 4], GPIO.HIGH)
    GPIO.output(sequence[ (k+2) % 4], GPIO.LOW)
    GPIO.output(sequence[ (k+3) % 4], GPIO.LOW)
    time.sleep(0.5)
    
GPIO.cleanup()
