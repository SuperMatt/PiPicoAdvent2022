# Imports
from machine import Pin
import time

# Set up our button names and GPIO pin numbers
# Also set pins as inputs and use pull downs
button1 = Pin(13, Pin.IN, Pin.PULL_DOWN)

# Set up our LED names and GPIO pin numbers
red = Pin(18, Pin.OUT)

while True: # Loop forever

    time.sleep(0.5) # Short delay
            
    if button1.value() == 1: #If button 1 is pressed
        
        print("Button 1 pressed")
        
        red.toggle() # Toggle Red LED on/off
