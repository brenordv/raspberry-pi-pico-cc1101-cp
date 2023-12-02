# Based on this script: https://github.com/educ8s/CircuitPython-SSD1306-OLED-display-Examples/tree/main

import board, busio, displayio, os, terminalio
import adafruit_displayio_ssd1306
from adafruit_display_text import label

displayio.release_displays()
sda, scl = board.GP14, board.GP15
i2c = busio.I2C(scl, sda)
display_bus = displayio.I2CDisplay(i2c, device_address=0x3C)
display = adafruit_displayio_ssd1306.SSD1306(display_bus, width=128, height=64)

# Make the display context
splash = displayio.Group()
display.show(splash)

color_bitmap = displayio.Bitmap(128, 64, 1)
color_palette = displayio.Palette(1)
color_palette[0] = 0xFFFFFF  # White

bg_sprite = displayio.TileGrid(color_bitmap, pixel_shader=color_palette, x=0, y=0)
splash.append(bg_sprite)

# Draw a smaller inner rectangle
inner_bitmap = displayio.Bitmap(118, 54, 1)
inner_palette = displayio.Palette(1)
inner_palette[0] = 0x000000  # Black
inner_sprite = displayio.TileGrid(inner_bitmap, pixel_shader=inner_palette, x=5, y=5)
splash.append(inner_sprite)
random_word_label = None
rx_waiting_label = None
rx_count = 0


def display_setup_for_receiving():
    global rx_waiting_label

    text = "waiting"
    if rx_waiting_label is not None:
        rx_waiting_label.text = text
        return

    rx_waiting_label = label.Label(terminalio.FONT, text=text, color=0xFFFF00, x=28, y=12)
    rx_waiting_label.anchor_point = (0.5, 0.5)
    splash.append(rx_waiting_label)


def display_setup_for_sending():
    # Draw a label
    text = "Blue: Random word"
    text_area = label.Label(terminalio.FONT, text=text, color=0xFFFF00, x=12, y=12)
    splash.append(text_area)

    text = "Green: Send word"
    text_area2 = label.Label(terminalio.FONT, text=text, color=0xFFFF00, x=12, y=22)
    splash.append(text_area2)


def display_received_word(word):
    global rx_waiting_label
    global rx_count
    rx_count += 1
    rx_waiting_label.text = f"received! ({str(rx_count)})"
    display_random_word(word)


def display_random_word(word):
    global random_word_label
    if word is None:
        return

    if random_word_label is not None:
        random_word_label.text = word
        return
    random_word_label = label.Label(terminalio.FONT, text=word, color=0xFFFF00, x=12, y=42)
    random_word_label.anchor_point = (0.5, 0.5)  # Change anchor point to center
    #random_word_label.scale = 2
    splash.append(random_word_label)


