from gpiozero import LED, Button
from time import sleep

led = LED(24)
button = Button(18)

while True:
    button.wait_for_press()
    led.toggle()
    sleep(0.5)

