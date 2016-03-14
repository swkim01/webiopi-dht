# webiopi-dht
DHT sensor module for WebIOPi

#### Installation
1. Download and decompress source code on [webiopi homepage](http://webiopi.trouch.com/)
2. You have to install Adafruit Python DHT module.
`
sudo apt-get install build-essential pythn-dev
git clone https://github.com.adafruit/Adafruit_Python_DHT.git
cd Adafruit_Python_DHT
sudo python setup.py install
`
3. Clone my repo onto your pi.
```shell
git clone https://github.com/swkim01/webiopi-dht.git
```
If you use RPi 2, you have to patch the souce as follows.
```shell
cd [WebIOPi's source path]
patch -p1 < [webiopi-dht path]/webiopi-0.7.1-rpi2.diff
```

4. copy __init__.py and dhtXX.py to [WebIOPi's source path]/python/webiopi/devices/sensor directory.

5. Install and start WebIOPi

#### Test
1. To test this module, connect a DHT22 sensor input to gpio port [18] and an LED to port [17] of pi.

2. To enable DHT and GPIO feature on webiopi, modify /etc/webiopi/config.
```
...
[DEVICES]
...
dht0 = DHT22 pin:18
...
[REST]
gpio-export = 17
gpio-get-value = true
gpio-post-value = true
...
```

3. After restarting WebIOPi, you can see the temperature/humidity values on 'device-monitor' page.

4. Then let's control the device via cURL command like below.
```
curl -X GET -u webiopi:raspberry localhost:8000/devices/dht0/sensor/temperature/c
24.40
curl -X GET -u webiopi:raspberry localhost:8000/devices/dht0/sensor/humidity/percent
44
curl -X GET -u webiopi:raspberry localhost:8000/GPIO/17/value
0
curl -X POST -u webiopo:raspberry localhost:8000/GPIO/17/value/1
curl -X POST -u webiopo:raspberry localhost:8000/GPIO/17/value/0
```

#### Custom Web and Python Script Example
Our example consists of a html and python script file. The html includes web content to monitor the DHT sensor and control the LED. The script code is to get/switch operation mode to Auto or Manual. On Auto mode, the LED will turn on and off automatically according to temperature value of the DHT22 sensor.

1. Modify /etc/webiopi/config file to set html and python script file correctly.
```
...
[SCRIPTS]
myproject = [webiopi-dht path]/examples/python/script.py
...
[HTTP]
...
doc-root = [webiopi-dht path]/examples/html
...
```

2. Restart WebIOPi and open web browser. 
