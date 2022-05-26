import board
import analogio


# Set Up light Sensor
light = analogio.AnalogIn(board.LIGHT)

SAMPLE_PERIOD = 0.001 # seconds
SAMPLE_SIZE = 100 # number of measurements to analyze at a time
raw_values = [0]*SAMPLE_SIZE

stop_collecting = false 
start_time = time.monotonic()

while not stop_collecting:
    current_time = time.monotonic()
    
    # Read the raw light value from the sensor
    raw_light = light.value
    # Add the light value to the list of raw values
    raw_values.append(raw_light)
    print (raw_light)
