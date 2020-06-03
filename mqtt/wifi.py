import network
class Wifi(object):
    station = network.WLAN(network.STA_IF)
    state="not_connect"
    def __init__(self, *args, **kwargs):
        super(Wifi,self).__init__(*args, **kwargs)
    def connect(self,ssid,password):
        print("connecting. . . .  .")
        if self.station.isconnected() == True:
            self.state="connected"
            return
        self.station.active(True)
        self.station.disconnect()
        self.station.connect(ssid, password)
        print("connecting")
        while self.station.isconnected() == False:
            self.state="connecting"
            pass
        self.state="connected"
        print(self.station.ifconfig())
    def disconnect(self):
        self.station.disconnect()
        print("forget")
    def isconnected(self):
        return self.state
