import time
import board
import digitalio

from transceiver import setup_tx, transmit, wait_for_messages
from words import get_random_word
from display import display_setup_for_sending, display_random_word, display_received_word, display_setup_for_receiving


def _debounce_button(btn):
    while not btn.value:
        time.sleep(0.01)


def receiver_routine():
    display_setup_for_receiving()
    for msg in wait_for_messages():
        print(msg)
        display_received_word(msg)
        time.sleep(1)
        display_setup_for_receiving()


def sender_routine():
    display_setup_for_sending()
    setup_tx()
    blue_button = digitalio.DigitalInOut(board.GP13)
    blue_button.direction = digitalio.Direction.INPUT
    blue_button.pull = digitalio.Pull.UP

    green_button = digitalio.DigitalInOut(board.GP12)
    green_button.direction = digitalio.Direction.INPUT
    green_button.pull = digitalio.Pull.UP

    word = None

    while True:
        if not blue_button.value:  # Button is pressed when pin is LOW (due to pull-up resistor)
            word = get_random_word()
            display_random_word(word)
            print(f"Funny word: {word}")
            _debounce_button(blue_button)

        if not green_button.value:
            print("Sending...")
            display_random_word("Sending...")
            transmit(word)
            time.sleep(0.5)
            display_random_word(word)
            _debounce_button(green_button)


def main(is_sender):
    if is_sender:
        sender_routine()
    else:
        receiver_routine()


if __name__ == "__main__":
    main(is_sender=True)
