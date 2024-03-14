import Adafruit_DHT


DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = 4


def temperature():
    h, t = Adafruit_DHT.read(DHT_SENSOR, DHT_PIN)
    return h,t

