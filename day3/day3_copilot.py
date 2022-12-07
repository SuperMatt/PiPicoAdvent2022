# this raspberry pi pico has 3 buttons which trigger 3 LEDS.
# the first button is on pin 3, the second on pin 8 and the third on pin 13
# the first, red light is on pin 18
# the second, amber light is on pin 19
# the third, green light is on pin 20
# pressing a button should toggle an led, and release should turn it off
# the buttons are active high, so when pressed they will read 1

import machine
import utime

# set up the buttons
button1 = machine.Pin(3, machine.Pin.IN, machine.Pin.PULL_DOWN)
button2 = machine.Pin(8, machine.Pin.IN, machine.Pin.PULL_DOWN)
button3 = machine.Pin(13, machine.Pin.IN, machine.Pin.PULL_DOWN)

# set up the LEDs
led1 = machine.Pin(18, machine.Pin.OUT)
led2 = machine.Pin(19, machine.Pin.OUT)
led3 = machine.Pin(20, machine.Pin.OUT)

# set up the LEDs to be off
led1.value(0)
led2.value(0)
led3.value(0)

while True:
    # check the buttons
    if button1.value() == 1:
        led1.value(1)
    else:
        led1.value(0)
    if button2.value() == 1:
        led2.value(1)
    else:
        led2.value(0)
    if button3.value() == 1:
        led3.value(1)
    else:
        led3.value(0)
    utime.sleep(0.1)

