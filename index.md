## MicroPython Library for I2C LC709203F battery status and fuel gauge

This library was adapted to MicroPython by Christian Reichl based on the CircuitPython library from ladyada (Limor Fried) Adafruit Industries.

### Tested with the following boards:
<ul>
  <li>Pycom WiPy 3.0
    <ul>
      <li>Pycom MicroPython 1.20.2.r4 [v1.11-ffb0e1c] on 2021-01-12; WiPy with ESP32</li>
      <li>https://pycom.io/product/wipy-3-0/ </li>
    </ul>
  </li>
  <li>Pycom FiPy
    <ul>
      <li>Pycom MicroPython 1.20.2.r4 [v1.11-ffb0e1c] on 2021-01-12; FiPy with ESP32</li>
      <li>https://pycom.io/product/fipy/ </li>
    </ul>
  </li>
  <li>Raspberry Pi Pico
    <ul>
      <li>MicroPython v1.17 on 2021-09-02; Raspberry Pi Pico with RP2040</li>
      <li>https://www.raspberrypi.com/products/raspberry-pi-pico/</li>
    </ul>
  </li>
</ul>

## Raspberry Pi Pico with Adafruit LC709203F and 10kΩ Thermistor
#### Please note: 
Don't forget to connect a battery to one of the JST connectors on the Adafruit LC709203F. If no battery is connected it will cause an I2C error and the program will stop!
![Raspberry Pi Pico with Adafruit LC709203F and 10kΩ Thermistor](https://github.com/chris-reichl/MicroPython_LC709203F/blob/main/pictures/Raspberry_Pi_Pico_Adafruit_LC709203F_Thermistor.PNG?raw=true)

## Pycom Board with Adafruit LC709203F and 10kΩ Thermistor
#### Please note: 
Don't forget to connect a battery to one of the JST connectors on the Adafruit LC709203F. If no battery is connected it will cause an I2C error and the program will stop!
![Pycom Board with Adafruit LC709203F and 10kΩ Thermistor](https://github.com/chris-reichl/MicroPython_LC709203F/blob/main/pictures/Pycom_WiPy_Adafruit_LC709203F_Thermistor.PNG?raw=true)

<!-- Usage Example -->
## Usage Example
Examples of using this module are in examples folder. There is a separate example for Pycom and Pico, because the commandos of the boards are slightly different.

Load the `main.py` script with the library `LC709203F_CR.py` on a microcontroller with MicroPython and execute the `main.py` script.
Don't forget to connect a battery to one of the JST connectors on the Adafruit LC709203F. If no battery is connected it will cause an I2C error and the program will stop!

If everything works correctly, then you should get the following output:
![output](https://github.com/chris-reichl/MicroPython_LC709203F/blob/main/pictures/output.png?raw=true)

#### Please note: 
It is normal that the temperature is not correct in the first few seconds. If everything is connected correctly, the sensor will output a temperature of 25.05 °C for the first few seconds. If the transistor is not connected, it will output -41.95 °C. The sensor updates the temperature about every 10 seconds.


## License

Distributed under the MIT License. See `LICENSE.txt` for more information.
