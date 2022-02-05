"""
================================================================================
MicroPython Library for I2C LC709203F battery status and fuel gauge
* Author(s): Christian Reichl
* This library was adapted to MicroPython by Christian Reichl based on the CircuitPython library from ladyada (Limor Fried) Adafruit Industries.

Implementation Notes
--------------------
**Hardware:**
* `Adafruit LC709203F LiPoly / LiIon Fuel Gauge and Battery Monitor
  <https://www.adafruit.com/product/4712>`_ (Product ID: 4712)

* Compatible with Pycom boards and Raspberry Pi Pico

* Tested with the following boards:  
    * Pycom WiPy 3.0
        Pycom MicroPython 1.20.2.r4 [v1.11-ffb0e1c] on 2021-01-12; WiPy with ESP32
        https://pycom.io/product/wipy-3-0/
    * Pycom FiPy
        Pycom MicroPython 1.20.2.r4 [v1.11-ffb0e1c] on 2021-01-12; FiPy with ESP32
        https://pycom.io/product/fipy/
    * Raspberry Pi Pico
        MicroPython v1.17 on 2021-09-02; Raspberry Pi Pico with RP2040
        https://www.raspberrypi.com/products/raspberry-pi-pico/
"""

from micropython import const
from time import sleep

LC709203F_I2CADDR_DEFAULT = const(0x0B)
LC709203F_CMD_ICVERSION = const(0x11)
LC709203F_CMD_BATTPROF = const(0x12)
LC709203F_CMD_POWERMODE = const(0x15) 
LC709203F_CMD_APA = const(0x0B)
LC709203F_CMD_INITRSOC = const(0x07)
LC709203F_CMD_CELLVOLTAGE = const(0x09)
LC709203F_CMD_CELLITE = const(0x0F)
LC709203F_CMD_CELLTEMPERATURE = const(0x08)
LC709203F_CMD_THERMISTORB = const(0x06)
LC709203F_CMD_STATUSBIT = const(0x16)


class CV:
    """struct helper"""

    @classmethod
    def add_values(cls, value_tuples):
        """Add CV values to the class"""
        cls.string = {}
        cls.lsb = {}

        for value_tuple in value_tuples:
            name, value, string, lsb = value_tuple
            setattr(cls, name, value)
            cls.string[value] = string
            cls.lsb[value] = lsb

    @classmethod
    def is_valid(cls, value):
        """Validate that a given value is a member"""
        return value in cls.string


class PowerMode(CV):
    """Options for ``power_mode``"""
    pass


PowerMode.add_values(
    (
        ("OPERATE", 0x0001, "Operate", None),
        ("SLEEP", 0x0002, "Sleep", None),
    )
)


class PackSize(CV):
    """Options for ``pack_size``"""
    pass


PackSize.add_values(
    (
        ("MAH100", 0x08, "100 mAh", 100),
        ("MAH200", 0x0B, "200 mAh", 200),
        ("MAH500", 0x10, "500 mAh", 500),
        ("MAH1000", 0x19, "1000 mAh", 1000),
        ("MAH2000", 0x2D, "2000 mAh", 2000),
        ("MAH2500", 0x33, "2500 mAh", 2500),
        ("MAH3000", 0x36, "3000 mAh", 3000),
    )
)


class LC709203F:
    """Interface library for LC709203F battery monitoring and fuel gauge sensors
    :param ~busio.I2C i2c_bus: The I2C bus the device is connected to
    :param int address: The I2C device address. Defaults to :const:`0x0B`
    """
    
    def __init__(self, i2c_bus, address=LC709203F_I2CADDR_DEFAULT):
        print("inizializing LC709203F...")
        self.i2c_device = i2c_bus
        self.addr = address
        self._buf = bytearray(10)
        self.power_mode = PowerMode.OPERATE  # pylint: disable=no-member
        self.pack_size = PackSize.MAH2500  # pylint: disable=no-member
        self.battery_profile = 1
        self.init_RSOC()
        print("LC709203F sucessfully inizialized!")


    def init_RSOC(self):  # pylint: disable=invalid-name
        """ Initialize the state of charge calculator """
        sleep(0.1) # increase time.sleep in case of problems with i2c bus!
        self._write_word(LC709203F_CMD_INITRSOC, 0xAA55)
        sleep(0.1) # increase time.sleep in case of problems with i2c bus!

    @property
    def cell_voltage(self):
        """Returns floating point voltage"""
        try:
            cell_voltage = self._read_word(LC709203F_CMD_CELLVOLTAGE) / 1000
            return round(cell_voltage, 3) 
        except:
            print("cell_voltage read error")
            return None
        
    @property
    def cell_percent(self):
        """Returns percentage of cell capacity"""
        try:
            cell_percentage = self._read_word(LC709203F_CMD_CELLITE) / 10
            if cell_percentage <= 100.0:
                return round(cell_percentage, 3)
            else:
                print("percentage read error")
                return None  
        except:
            print("percentage read error")
            return None
    
    @property   
    def cell_temperature(self):
        """Returns the temperature of the cell"""
        try:
            cell_temperature = self._read_word(LC709203F_CMD_CELLTEMPERATURE) / 10 - 273.15
            if cell_temperature <= 200.0:
                return round(cell_temperature, 3)  
            else:
                print("cell_temperature read error")
                return None  
        except:
            print("cell_temperature read error")
            return None
       
    @cell_temperature.setter
    def cell_temperature(self, value):
        """Sets the temperature in the LC709203F"""
        if self.thermistor_enable:
            raise AttributeError("temperature can only be set in i2c mode")
        self._write_word(LC709203F_CMD_CELLTEMPERATURE, int(value + 273.15) * 10)     

    @property
    def ic_version(self):
        """Returns read-only chip version"""
        return self._read_word(LC709203F_CMD_ICVERSION)

    @property
    def setSleepMode(self):
        """Returns floating point voltage"""
        # sleep power_mode = 2
        global powermode
        global counter
        powermode = 0
        counter = 0
        tryCounter = 5
        def setFunction():
            global powermode
            global counter
            try:
                counter = counter + 1
                self.power_mode = PowerMode.SLEEP
                powermode = self.power_mode
                if powermode == 2: print("LC709203F - sleeping state active")
            except:
                return None
        while powermode is not 2 and counter < tryCounter:
            setFunction()
        if counter >= tryCounter: print("Error set sleep")


    @property
    def setOperateMode(self):
        """Returns floating point voltage"""
        # operate power_mode = 1
        global powermode
        global counter
        powermode = 0
        counter = 0
        tryCounter = 5
        def setFunction():
            global powermode
            global counter
            try:
                counter = counter + 1
                self.power_mode = PowerMode.OPERATE
                powermode = self.power_mode
                if powermode == 1: print("LC709203F - operating state active")
            except:
                
                return None
        while powermode is not 1 and counter < tryCounter:
            setFunction()
        if counter >= tryCounter: print("Error set operate")

    @property
    def power_mode(self):
        """Returns current power mode (operating or sleeping)"""
        return self._read_word(LC709203F_CMD_POWERMODE)

    @power_mode.setter
    def power_mode(self, mode):
        if not PowerMode.is_valid(mode):
            raise AttributeError("power_mode must be a PowerMode")
        self._write_word(LC709203F_CMD_POWERMODE, mode)

    @property
    def battery_profile(self):
        """Returns current battery profile (0 or 1)"""
        return self._read_word(LC709203F_CMD_BATTPROF)

    @battery_profile.setter
    def battery_profile(self, mode):
        if not mode in (0, 1):
            raise AttributeError("battery_profile must be 0 or 1")
        self._write_word(LC709203F_CMD_BATTPROF, mode)

    @property
    def pack_size(self):
        """Returns current battery pack size"""
        return self._read_word(LC709203F_CMD_APA)

    @pack_size.setter
    def pack_size(self, size):
        if not PackSize.is_valid(size):
            raise AttributeError("pack_size must be a PackSize")
        self._write_word(LC709203F_CMD_APA, size)

    @property
    def thermistor_bconstant(self):
        """Returns the thermistor B-constant"""
        return self._read_word(LC709203F_CMD_THERMISTORB)

    @thermistor_bconstant.setter
    def thermistor_bconstant(self, bconstant):
        """Sets the thermistor B-constant"""
        self._write_word(LC709203F_CMD_THERMISTORB, bconstant)

    @property
    def thermistor_enable(self):
        """Returns the current temperature source"""
        return self._read_word(LC709203F_CMD_STATUSBIT)

    @thermistor_enable.setter
    def thermistor_enable(self, status):
        """Sets the temperature source to Tsense"""
        if not status in (True, False):
            raise AttributeError("thermistor_enable must be True or False")
        self._write_word(LC709203F_CMD_STATUSBIT, status)

    def _generate_crc(self, data):
        """8-bit CRC algorithm for checking data"""
        crc = 0x00
        # calculates 8-Bit checksum with given polynomial
        for byte in data:
            crc ^= byte
            for _ in range(8):
                if crc & 0x80:
                    crc = (crc << 1) ^ 0x07
                else:
                    crc <<= 1
                crc &= 0xFF
        return crc

    def _read_word(self, regAddress):
        data = int.from_bytes(self.i2c_device.readfrom_mem(LC709203F_I2CADDR_DEFAULT, regAddress, 2), 'little') & 0xFFFF
        return data   
        
    def _write_word(self, command, data):
        self._buf[0] = LC709203F_I2CADDR_DEFAULT * 2  # write byte
        self._buf[1] = command  # command / register
        self._buf[2] = data & 0xFF
        self._buf[3] = (data >> 8) & 0xFF
        self._buf[4] = self._generate_crc(self._buf[0:4])
        self.i2c_device.writeto(LC709203F_I2CADDR_DEFAULT, self._buf[1:5])
        

