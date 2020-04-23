from machine import Pin
led=Pin(2,Pin.OUT)
import time
while True:
  time.sleep(1)
  led.value(not led.value())
