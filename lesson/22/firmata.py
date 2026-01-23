from pyfirmata import Arduino, util
import time

# Connect to the board (replace 'COM3' with your port)
board = Arduino('COM3')
print("Arduino connected")

# Start an iterator thread to avoid buffer overflows (essential for analog inputs)
it = util.Iterator(board)
it.start()

# Define the pin as an output
board.digital[13].mode = 'o' 

while True:
    board.digital[13].write(1) # Turn LED on (1)
    time.sleep(0.5)
    board.digital[13].write(0) # Turn LED off (0)
    time.sleep(0.5)
