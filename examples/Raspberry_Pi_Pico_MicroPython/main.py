import time
from machine import I2C, Pin
from LC709203F_CR import LC709203F

print("Make sure LiPoly battery is plugged into the board!")

i2c = I2C(0,scl=Pin(1), sda=Pin(0)) # GP0=SDA GP1=SCL
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

# sleep and operate mode:
# sensor.setSleepMode -> activates the sleep mode to save energy
# sensor.setOperateMode -> deactivates the sleep mode to perform measurements
# sensor.power_mode -> returns 1 -> operate or 2 -> sleep