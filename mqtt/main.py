import machine
from wifi import Wifi
Wifi().connect("Suko","sooko9999")
from mqtt import MQTTClient
import ubinascii
from machine import Pin
class Iot(object):
    client_id = ubinascii.hexlify(machine.unique_id())
    client=None
    def __init__(self,*args,**kwargs):
        super(Iot,self).__init__(*args,**kwargs)
        try:
            self.client=MQTTClient(self.client_id,"mqtt.eclipse.org",keepalive=0)
            self.client.connect()
            self.client.set_callback(self.on_message)
            self.client.subscribe(b"switch")
            self.client.subscribe(b"push_button")
            while True:
                self.client.wait_msg()
        except:
            Wifi().disconnect()
            machine.reset()
    def on_message(self,topic,msg):
        print(topic,msg)
        if msg==b"on":
            self.grenn_on()
            self.client.publish(b"loger",b"saya hidup")
        elif msg==b"off":
            self.grenn_off()
            self.client.publish(b"loger", b"saya mati")
    def grenn_on(self):
        Pin(2,Pin.OUT).value(0)
    def grenn_off(self):
        Pin(2,Pin.OUT).value(1)
Iot()