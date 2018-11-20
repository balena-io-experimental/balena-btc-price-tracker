# Bitcoin Price Tracker

![btc traffic light](https://github.com/balena-io-playground/balena-btc-price-tracker/blob/master/img/combined.jpg?raw=true)

This is a project to analyze the price of bitcoin, comparing if the current price is above or below the opening price at midnight.

### Getting started

* Create a [balena.io](https://balena.io) account following [this tutorial](https://www.balena.io/docs/learn/getting-started/raspberrypi3/python/)
* Clone this repository to your computer: `git clone https://github.com/balena-io-playground/balena-btc-price-tracker.git`
* Go to `balena-btc-price-tracker` directory and add balena reote `git remote add balena <USERNAME>git.balena-cloud.com:<USERNAME>/<APPNAME>.git`
* Push the code live `git push balena master`.

Once our code is up and running on the Raspberry Pi, inside the balena dashboard you will be able to see the current price and if it is higher or lower than the opening price.

A complete step-by-step tutorial can be found at [https://www.balena.io/blog/build-a-bitcoin-traffic-light-with-balenacloud/](https://www.balena.io/blog/build-a-bitcoin-traffic-light-with-balenacloud/)
