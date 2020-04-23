
import network
import socket
import time
import machine
import time
class TcpServer(object):
    wlan=None
    listenSocket=None
    wlan=network.WLAN(network.AP_IF)         
    wlan.config(essid="sooko",authmode=0)
    wlan.active(True)                         
    conn=None
    while(wlan.ifconfig()[0]=='0.0.0.0'):
        time.sleep(1)
    def __init__(self, *args, **kwargs):
        super(TcpServer,self).__init__(*args, **kwargs)
        self.get_message()
    def get_message(self):
        try:
            self.listenSocket = socket.socket()            
            self.listenSocket.bind(("192.168.4.1",800))              
            self.listenSocket.listen(1)                    
            self.listenSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)    
            while True:
                try:
                    print("accepting.....")
                    self.conn,addr = self.listenSocket.accept()       
                    print(addr,"connected")
                    while True:
                        data = self.conn.recv(1024)     
                        if(len(data) == 0):
                            print("close socket")
                            self.conn.close()                        
                            break
                    str_data=data.decode()
                    print(str_data)
                except:
                    pass
        except:
            if(self.listenSocket):
                self.listenSocket.close()
                self.wlan.active(False)
                machine.reset()
TcpServer()
