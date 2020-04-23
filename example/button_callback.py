
import machine
from machine import Pin
def callback(pin):
    if pin.value()==1:
        print("button pressed")
    else:
        print("button_released")
button = Pin(0, Pin.IN, Pin.PULL_UP)
button.irq(trigger=Pin.IRQ_RISING | Pin.IRQ_FALLING, handler=callback)
# 