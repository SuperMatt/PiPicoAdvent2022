# Imports
from machine import Pin
from time import sleep

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

# turn on a light
def light_on(light):
    all_off()
    pins[light].on()


# start with the first light
current = 0

# loop forever
while True:
    print(current)
    light_on(current)
    sleep(SLEEP)
    # move to the next light, wrapping around
    current = (current + 1) % len(pins)