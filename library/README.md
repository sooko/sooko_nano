# sooko nano board library

untuk membermudah pengunaan board dalam berbagai project internet of
things kami telah membuat beberapa libary
- wifi.py untuk menghubungkan board ke router anda
- umqttsimple untuk membuat kommunikasi dengan protokol mqtt


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


