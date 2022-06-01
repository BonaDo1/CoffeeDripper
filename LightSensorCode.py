import time
import board
from analogio import AnalogIn

THRESHOLD = 62000
DELAY_SECONDS = 0.01
TOTAL_RECORD_TIME = 2.0
elapsedTime = 0.0
oldTime = time.monotonic()
data = []

# Connect an analog sensor to the A1 port of the board you are using. This means a 3V, GND, and signal pin must all be connected.
analog_in = AnalogIn(board.A1)

# This function turns the analog reading of the sensor (a number from 0 - 65536) to a voltage.
def readAnalogPin():
    return analog_in.value
    
def thresholdValue(value):
    if(value > THRESHOLD):
        return 1
    else:
        return 0
    
while (elapsedTime < TOTAL_RECORD_TIME):
    currentTime = time.monotonic()
    pinValue = readAnalogPin()
    recordValue = thresholdValue(pinValue)
    #print("{0},{1}".format(elapsedTime, recordValue))
    data.append([elapsedTime,recordValue])
    
    time.sleep(DELAY_SECONDS)
    elapsedTime += currentTime - oldTime
    oldTime = currentTime
for row in data:
    print("{0},{1}".format(row[0],row[1]))
