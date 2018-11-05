import RPi.GPIO as GPIO
from time import sleep
import datetime
import urllib.request
import json

# Initiate GPIO with breakout pin numbering
GPIO.setmode(GPIO.BCM) 
GPIO.setwarnings(False) 

# Setup GPIO Pins
red = 23
green = 27
orange = 22

GPIO.setup(red, GPIO.OUT)
GPIO.setup(orange, GPIO.OUT)
GPIO.setup(green, GPIO.OUT)

# Bitcoin price-tracking url and header
url = "https://api.coindesk.com/v1/bpi/currentprice.json"
hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}

def set_color_red():
    GPIO.output(red, GPIO.HIGH)
    GPIO.output(green, GPIO.LOW)
    GPIO.output(orange, GPIO.LOW)   

def set_color_green():
    GPIO.output(red, GPIO.LOW)
    GPIO.output(green, GPIO.HIGH)
    GPIO.output(orange, GPIO.LOW)   

def set_color_orange():
    GPIO.output(red, GPIO.LOW)
    GPIO.output(green, GPIO.LOW)
    GPIO.output(orange, GPIO.HIGH)  

def get_price(url, hdr):
    req = urllib.request.Request(url, headers=hdr)
    r = urllib.request.urlopen(req).read()
    price_usd = float(json.loads(r.decode('utf-8'))['bpi']['USD']['rate'].replace(',',''))
    return "{:.2f}".format(price_usd)

# Colorful text
# https://stackoverflow.com/a/34443116/1412635
def prRed(prt):
    print("\033[91m {}\033[00m" .format(prt))

def prGreen(prt):
    print("\033[92m {}\033[00m" .format(prt))

# Initialize Values
opening_price = get_price(url, hdr)
max_price = opening_price
min_price = opening_price
current_price = opening_price
current_day = datetime.datetime.today().day
previous_day = current_day
previous_state = "green"

while True:
    # Check if new day to reset opening price
    current_day = datetime.datetime.today().day
    if (current_day != previous_day):
        previous_day = current_day
        opening_price = get_price(url, hdr)

    # Get current Bitcoin price
    current_price = get_price(url, hdr)

    # Set max and min prices of the day
    if(current_price > max_price):
        max_price = current_price

    if(current_price < min_price):
        min_price = current_price

    # Show prices in terminal
    message = str(current_day) + " - Current Price: $" +  current_price + " - Daily Max: $" + max_price + " - Daily Min: $" + min_price + " - Opening Price: $" + opening_price

    if(current_price >= opening_price):
        if previous_state == "red":
            # If previous state was red, we want to make it orange to show transition
            previous_state = "green"
            set_color_orange()
            sleep(5)

        prGreen(message)
        set_color_green()
    else:
        if previous_state == "green":
            # If previous state was red, we want to make it orange to show transition
            previous_state = "red"
            set_color_orange()
            sleep(5)

        prRed(message)
        set_color_red()

    sleep(60)