import time
from machine import I2C
from LC709203F_CR import LC709203F
 
print("Make sure LiPoly battery is plugged into the board!")

i2c = I2C(0, I2C.MASTER) # default I2C-Pins on Pycom-Boards: P9=SDA P10=SCL
print(i2c.scan())

sensor = LC709203F(i2c)

# check your NTC thermistor datasheet for the appropriate B-Constant
sensor.thermistor_bconstant = 3950
sensor.thermistor_enable = True

print("IC version:", hex(sensor.ic_version))
while True:
    volt = sensor.cell_voltage
    perc = sensor.cell_percent
    temp = sensor.cell_temperature
    print("Battery: " + str(volt) + " Volts / " + str(perc) + " % Cell Temperature: " + str(temp) + " C")
    time.sleep(2) # seconds
    