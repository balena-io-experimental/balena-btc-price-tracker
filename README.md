# Bitcoin Price Tracker

![btc traffic light](https://github.com/balena-io-playground/balena-btc-price-tracker/blob/master/img/combined.jpg?raw=true)

This is a project to analyze the price of bitcoin, comparing if the current price is above or below the opening price at midnight.

### Getting started

* Create a [balena.io](https://balena.io) account following [this tutorial](https://www.balena.io/docs/learn/getting-started/raspberrypi3/python/)
* Clone this repository to your computer: `git clone https://github.com/balena-io-playground/balena-btc-price-tracker.git`
* Go to `balena-btc-price-tracker` directory and add balena reote `git remote add balena <USERNAME>@git.balena.io:<USERNAME>/<APPNAME>.git`
* Push the code live `git push balena master`.

Once our code is up and running on the Raspberry Pi, inside the balena dashboard you will be able to see the current price and if it is higher or lower than the opening price.

### Electronics

This project uses the GPIO pins 22, 23 and 27 from the Raspberry Pi. 

```
22 = Orange
23 = Red
27 = Green
```

The current color will be set as GPIO HIGH while the other pins will be set to LOW. Once the device changes color, it will stay in Orange for 5 seconds and change color.

A more in-depth tutorial about this project can be found here.
