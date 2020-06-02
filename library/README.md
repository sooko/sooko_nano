# sooko nano board library

libary yang sering digunakan dalam membuat project internet of things
wifi.py

### put library file to board
using adafruit-ampy


```
ampy put wifi.py
ampy put umqttsimple.py
```

### wify.py USAGE
connecting wifi
```
from wifi import Wifi
Wifi().connect("your ssid","your password")
```

check wifi state 
```
Wifi().isconnected()

```
disconnect wifi 
```
Wifi().disconnect()

```