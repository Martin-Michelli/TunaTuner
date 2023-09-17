import board
import digitalio
import displayio
import terminalio
import time
import keypad
from adafruit_display_text import label
import adafruit_displayio_ssd1306

'''Display Section'''
displayio.release_displays()
oled_reset = board.D0

i2c = board.STEMMA_I2C()
display_bus = displayio.I2CDisplay(i2c, device_address=0x3d, reset=oled_reset)

WIDTH = 128
WIDTH = 128
HEIGHT = 64
BORDER = 5

display = adafruit_displayio_ssd1306.SSD1306(display_bus, width=WIDTH, height=HEIGHT)

# Make the display context
splash = displayio.Group()
display.show(splash)

color_bitmap = displayio.Bitmap(WIDTH, HEIGHT, 1)
color_palette = displayio.Palette(1)
color_palette[0] = 0xFFFFFF  # White

bg_sprite = displayio.TileGrid(color_bitmap, pixel_shader=color_palette, x=0, y=0)
splash.append(bg_sprite)

# Draw a smaller inner rectangle
inner_bitmap = displayio.Bitmap(WIDTH - BORDER * 2, HEIGHT - BORDER * 2, 1)
inner_palette = displayio.Palette(1)
inner_palette[0] = 0x000000  # Black
inner_sprite = displayio.TileGrid(
    inner_bitmap, pixel_shader=inner_palette, x=BORDER, y=BORDER
)
splash.append(inner_sprite)

'''Button Matrix Section'''
num_rows = 3
num_cols = 3

row_pins = [board.D4, board.D3, board.D2]
col_pins = [board.D6, board. D5, board.D7]

rows = [digitalio.DigitalInOut(pin) for pin in row_pins]
cols = [digitalio.DigitalInOut(pin) for pin in col_pins]

# Initialize the row pins as inputs with pull-up resistors
for row in rows:
    row.direction = digitalio.Direction.INPUT
    row.pull = digitalio.Pull.UP

# Initialize the column pins as outputs
for col in cols:
    col.direction = digitalio.Direction.OUTPUT

# Button Matrix Layout:
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
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

def display_note(key_num):
    inner_bitmap = displayio.Bitmap(WIDTH - BORDER * 2, HEIGHT - BORDER * 2, 1)
    inner_palette = displayio.Palette(1)
    inner_palette[0] = 0x000000  # Black
    inner_sprite = displayio.TileGrid(
    inner_bitmap, pixel_shader=inner_palette, x=BORDER, y=BORDER
    )
    splash.append(inner_sprite)
    if key_num == 1:
        text = 'A'
    if key_num == 2:
        text = 'B'
    if key_num == 3:
        text = 'C'
    if key_num == 4:
        text = 'D'
    if key_num == 5:
        text = 'E'
    if key_num == 6:
        text = 'F'
    if key_num == 7:
        text = 's'
    if key_num == 8:
        text = 'G'
    if key_num == 9:
        text = 'f'
    text_area = label.Label(
    terminalio.FONT, text=text, color=0xFFFFFF, x=WIDTH // 2, y=HEIGHT // 2
    )
    splash.append(text_area)

# Main loop
while True:
    pressed = scan_matrix()

    if pressed:
        display_note(pressed)
        time.sleep(0.5)  # Add a small delay for stability
