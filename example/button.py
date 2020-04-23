from machine import Pin
button=Pin(0,Pin.IN)
import time
while True:
    print(button.value())
    
