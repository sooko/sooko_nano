# Burn/upload Firmware 
 

## instructions for burn/upload esp8266 micropython firmware

- Install esptool
```
pip install esptool
```
- goto directory folder

```
cd firmware
esptool.py --port /dev/ttyUSB0 erase_flash
esptool.py --port /dev/ttyUSB0 --baud 460800 write_flash --flash_size=detect 0 esp8266-20191220-v1.12.bin
```

### firmware source
you can get the firmware at 

* [micropython firmware](https://micropython.org/download/esp8266/) from micropython.org