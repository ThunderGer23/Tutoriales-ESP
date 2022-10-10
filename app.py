from machine import Pin
from time import sleep_ms as slms

led = Pin(2, Pin.OUT)

def main():
    led.value(1)
    slms(200)
    led.value(0)
    slms(200)
    led.value(1)


main()