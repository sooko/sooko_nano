from machine import Pin
list_led=[Pin(2,Pin.OUT),Pin(4,Pin.OUT),Pin(5,Pin.OUT)]
import time
while True:
    for i in list_led:
        i.value(1)
        time.sleep(1)
        i.value(0)
