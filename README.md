#**YUBeagle**#


Here are the Python modules to use Beaglebone (or Beaglebone Black) for a few projects.


##**1. Signal Generator**##

Using I2C interfacing with MCP4725 to generate signal.


**Prerequisite:**

1.MICROCHIP MCP4725

2.Beaglebone: I am using rev. A6 and 3.8.13-bone.

( or Beaglebone Black: I am using rev. C and 3.8.13-bone kernel. )




**Wiring:**

1.MCP4725 VSS to BB GND

2.MCP4725 VDD to BB 3.3V

3.MCP4725 SCL to BB P9_19

4.MCP4725 SDA to BB P9_20

5.MCP4725 VOut: output port




**Usage:**
```
python sin_simple.py  ## to generate simple sinusoidal wave
```


##**2. Stepper Motor Control**##



