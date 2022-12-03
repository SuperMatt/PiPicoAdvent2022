# this is a pi pico projet.
# there are 3 leds on pins 18,19,20
# the leds are red, amber and green
# the pins should be turned on in a random order but never the same pin twice in a row
# the leds should be turned on for 0.5 seconds

# imports

from machine import Pin
from time import sleep
import random

# time between light changes
SLEEP = 0.5

# pin numbers
RED = 18
AMBER = 19
GREEN = 20

# create a list of pins
pins = [
    Pin(RED, Pin.OUT), # Red
    Pin(AMBER, Pin.OUT), # Amber
    Pin(GREEN, Pin.OUT) # Green
]

# turn all lights off
def all_off():
    for pin in pins:
        pin.off()

# turn on a random light
def light_on(current):
    all_off()
    # pick a pin which isn't the current one
    next = current
    while next == current:
        next = random.randint(0, len(pins)-1)
    pins[next].on()
    return next

# start with the first light
current = 0

# loop forever
while True:
    print(current)
    current = light_on(current)
    sleep(SLEEP)