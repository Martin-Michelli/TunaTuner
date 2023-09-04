import board
import digitalio
import time

# Define the number of rows and columns in your button matrix
num_rows = 3
num_cols = 3

binOne = digitalio.DigitalInOut(board.D6)
binTwo = digitalio.DigitalInOut(board.D9)
binFour = digitalio.DigitalInOut(board.D10)

# Define the pins connected to the rows and columns
row_pins = [board.D4, board.D3, board.D2]  # Replace with your pins
col_pins = [board.D8, board. D5, board.D7]  # Replace with your pins

# Create digital input objects for rows and output objects for columns
rows = [digitalio.DigitalInOut(pin) for pin in row_pins]
cols = [digitalio.DigitalInOut(pin) for pin in col_pins]

# Initialize the row pins as inputs with pull-up resistors
for row in rows:
    row.direction = digitalio.Direction.INPUT
    row.pull = digitalio.Pull.UP

# Initialize the column pins as outputs
for col in cols:
    col.direction = digitalio.Direction.OUTPUT

# Define the button matrix layout (use any characters or values you like)
matrix = [
    ['1', '2', '3'],
    ['4', '5', '6'],
    ['7', '8', '9']
]

# Function to scan the button matrix and detect button presses
def scan_matrix():
    pressed_button = None

    for col_index, col in enumerate(cols):
        col.value = False  # Activate one column at a time

        for row_index, row in enumerate(rows):
            if not row.value:
                pressed_button = matrix[row_index][col_index]

        col.value = True  # Disable the column after scanning

    return pressed_button

# Main loop
while True:
    pressed = scan_matrix()

    if pressed:
        print("Button Pressed:", pressed)

    time.sleep(0.1)  # Add a small delay for stability
