
import time
import board
import digitalio
from analogio import AnalogIn

inputPin = AnalogIn(board.A1)

THRESHOLD = 2000
DELAY_SECONDS = 0.01
TOTAL_RECORD_TIME = 2.0
elapsedTime = 0.0
oldTime = time.monotonic()
data = []

led = digitalio.DigitalInOut(board.D13)
led.switch_to_output()

def readAnalogPin():
    return inputPin.value

def thresholdValue(value):
    if(value > THRESHOLD):
        return 1
    else:
        return 0


while (elapsedTime < TOTAL_RECORD_TIME):
    currentTime = time.monotonic()
    pinValue = readAnalogPin()
    recordValue = thresholdValue(pinValue)

    print("{0},{1}".format(elapsedTime, recordValue))
    data.append([elapsedTime,recordValue])

    time.sleep(DELAY_SECONDS)
    elapsedTime += currentTime - oldTime
    oldTime = currentTime

    led.value = not led.value
for row in data:
    print("{0},{1}".format(row[0], row[1]))
