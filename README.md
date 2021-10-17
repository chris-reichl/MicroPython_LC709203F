<div id="top"></div>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <!-- <a href="https://github.com/othneildrew/Best-README-Template">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a> -->

  <h3 align="center">MicroPython Library for I2C LC709203F battery status and fuel gauge</h3>

  <!-- <p align="center">
    With these sample codes you can receive and send data between a computer and a MicroPython microcontroller via USB connection.
    <br />
    <a href="https://github.com/othneildrew/Best-README-Template"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/othneildrew/Best-README-Template">View Demo</a>
    ·
    <a href="https://github.com/othneildrew/Best-README-Template/issues">Report Bug</a>
    ·
    <a href="https://github.com/othneildrew/Best-README-Template/issues">Request Feature</a>
  </p> -->
</div>



<!-- TABLE OF CONTENTS -->
<!-- <details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details> -->



<!-- ABOUT THE PROJECT -->
## About The Project

MicroPython Library for I2C LC709203F battery status and fuel gauge.

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

<!-- ### Built With

This section should list any major frameworks/libraries used to bootstrap your project. Leave any add-ons/plugins for the acknowledgements section. Here are a few examples.

* [Next.js](https://nextjs.org/)
* [React.js](https://reactjs.org/)
* [Vue.js](https://vuejs.org/)
* [Angular](https://angular.io/)
* [Svelte](https://svelte.dev/)
* [Laravel](https://laravel.com)
* [Bootstrap](https://getbootstrap.com)
* [JQuery](https://jquery.com)

<p align="right">(<a href="#top">back to top</a>)</p> -->


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


<!-- USAGE EXAMPLES -->
<!-- ## Usage

Use this space to show useful examples of how a project can be used. Additional screenshots, code examples and demos work well in this space. You may also link to more resources.

_For more examples, please refer to the [Documentation](https://example.com)_

<p align="right">(<a href="#top">back to top</a>)</p>
 -->


<!-- ROADMAP -->
<!-- ## Roadmap

- [x] Add Changelog
- [x] Add back to top links
- [] Add Additional Templates w/ Examples
- [] Add "components" document to easily copy & paste sections of the readme
- [] Multi-language Support
    - [] Chinese
    - [] Spanish

See the [open issues](https://github.com/othneildrew/Best-README-Template/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#top">back to top</a>)</p> -->



<!-- CONTRIBUTING -->
<!-- ## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#top">back to top</a>)</p> -->



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- CONTACT -->
<!-- ## Contact

Your Name - [@your_twitter](https://twitter.com/your_username) - email@example.com

Project Link: [https://github.com/your_username/repo_name](https://github.com/your_username/repo_name)

<p align="right">(<a href="#top">back to top</a>)</p> -->



<!-- ACKNOWLEDGMENTS -->
<!-- ## Acknowledgments

Use this space to list resources you find helpful and would like to give credit to. I've included a few of my favorites to kick things off!

* [Choose an Open Source License](https://choosealicense.com)
* [GitHub Emoji Cheat Sheet](https://www.webpagefx.com/tools/emoji-cheat-sheet)
* [Malven's Flexbox Cheatsheet](https://flexbox.malven.co/)
* [Malven's Grid Cheatsheet](https://grid.malven.co/)
* [Img Shields](https://shields.io)
* [GitHub Pages](https://pages.github.com)
* [Font Awesome](https://fontawesome.com)
* [React Icons](https://react-icons.github.io/react-icons/search)

<p align="right">(<a href="#top">back to top</a>)</p> -->



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
<!-- [contributors-shield]: https://img.shields.io/github/contributors/othneildrew/Best-README-Template.svg?style=for-the-badge
[contributors-url]: https://github.com/othneildrew/Best-README-Template/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/othneildrew/Best-README-Template.svg?style=for-the-badge
[forks-url]: https://github.com/othneildrew/Best-README-Template/network/members
[stars-shield]: https://img.shields.io/github/stars/othneildrew/Best-README-Template.svg?style=for-the-badge
[stars-url]: https://github.com/othneildrew/Best-README-Template/stargazers
[issues-shield]: https://img.shields.io/github/issues/othneildrew/Best-README-Template.svg?style=for-the-badge
[issues-url]: https://github.com/othneildrew/Best-README-Template/issues
[license-shield]: https://img.shields.io/github/license/othneildrew/Best-README-Template.svg?style=for-the-badge
[license-url]: https://github.com/othneildrew/Best-README-Template/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/othneildrew
[product-screenshot]: images/screenshot.png -->
