import webiopi

GPIO = webiopi.GPIO

LIGHT = 17 # GPIO pin using BCM numbering
MIN = 22
MAX = 27
AUTO = True

# setup function is automatically called at WebIOPi startup
def setup():
    # set the GPIO used by the light to output
    GPIO.setFunction(LIGHT, GPIO.OUT)

# loop function is repeatedly called by WebIOPi 
def loop():
    if (AUTO):
        dht = webiopi.deviceInstance("dht0")

        celsius = dht.getCelsius() # get current temperature
        if (celsius < MIN):
            GPIO.digitalWrite(LIGHT, GPIO.HIGH)
        if (celsius > MAX):
            GPIO.digitalWrite(LIGHT, GPIO.LOW)

    webiopi.sleep(1)

# destroy function is called at WebIOPi shutdown
def destroy():
    GPIO.digitalWrite(LIGHT, GPIO.LOW)

# a simple macro to return heater mode
@webiopi.macro
def getMode():
    if (AUTO):
        return "auto"
    return "manual"

# simple macro to set and return heater mode
@webiopi.macro
def setMode(mode):
    global AUTO
    if (mode == "auto"):
        AUTO = True
    elif (mode == "manual"):
        AUTO = False
    print("mode="+mode)
    return getMode()
