from time import sleep
from webiopi.utils.types import toint
import Adafruit_DHT
from webiopi.devices.sensor import Temperature,Humidity

class DHT11(Temperature, Humidity):
    VAL_RETRIES = 5
    sensor = Adafruit_DHT.DHT11
    pin = 4

    def __init__(self, pin="4"):
        self.pin = toint(pin)
        pass

    def __str__(self):
        return "DHT11(pin=%02d)" % self.pin

    def __family__(self):
        return [Temperature.__family__(self), Humidity.__family__(self)]

    def readRawData(self):
        for i in range(self.VAL_RETRIES):
            raw_h, raw_t = Adafruit_DHT.read_retry(self.sensor, self.pin)
            if raw_h is not None and raw_t is not None:
                return (raw_t, raw_h/100)

        #Stale was never 0, so datas are not actual
        raise Exception("DHT11(pin=%02d): data fetch timeout" % self.pin)

    def __getCelsius__(self):
        (raw_t, raw_h) = self.readRawData()
        return raw_t

    def __getFahrenheit__(self):
        return self.Celsius2Fahrenheit()

    def __getKelvin__(self):
        return self.Celsius2Kelvin()

    def __getHumidity__(self):
        (raw_t, raw_h) = self.readRawData()
        return raw_h

class DHT22(DHT11):
    def __init__(self, pin=4):
        DHT11.__init__(self, pin)
        self.sensor = Adafruit_DHT.DHT22

class AM2302(DHT11):
    def __init__(self, pin=4):
        DHT11.__init__(self, pin)
        self.sensor = Adafruit_DHT.AM2302
